 #include <conio.h>
 #include <stdio.h>
 #include <memory.h>
 #include <string.h>

 #define fi "A-small.in"
 #define fo "A-small.out"

 int T,i,j;
 char s[62];
 signed char d[36],e[36];

  /*****************************/
 long long solve(char st[62]){
      int len=strlen(st)-1,base=0,i,j;
      long long num=0,*b;

      for (i=0;i<36;i++) d[i]=0;
      for (i=0;i<len;i++){
	  if (st[i]>='a' && st[i]<='z') st[i]=st[i]-39;
	  if (d[st[i]-48]==0){
			      base++;
			      d[st[i]-48]=1;
			      }
	  }
  //    printf("%s\n",st);
	if (base<=1) base=2;
      for (i=0;i<36;i++) {
	  d[i]=-1;
	  e[i]=0;
      }
      b=new long long[len];

      d[st[0]-48]=1;
      e[1]=1;
      for (i=1;i<len;i++){
	  if (d[st[i]-48]<0){
		    j=0;
		    while ((e[j]!=0)&& (j<36)) {
			  j++;
			  }
		    d[st[i]-48]=j;
		    e[j]=1;
	  }
      }
      b[len-1]=1;
      for (i=len-2;i>=0;i--) b[i]=b[i+1]*base;
      for (i=0;i<len;i++) {
//	  printf("%3d",d[st[i]-48]);
	  num=num+d[st[i]-48]*b[i];
      }
//      printf("\n");
     return num;
 }

 void readfile(){
      long long M;
      FILE *f=fopen(fi,"rt");
      FILE *g=fopen(fo,"wt");
      fscanf(f,"%d",&T);
      fgetc(f);
      for (i=0;i<T;i++){
	  fgets(s,62,f);
//	  printf("%s",s);
	  M=solve(s);
	  fprintf(g,"Case #%d: %ld\n",i+1,M);
      }
      fclose(f);
      fclose(g);
 }

 /*****************************/
 void writefile(){
 }

 /***************************/
 int main(){
 clrscr();
     readfile();
//     getch();
     return 0;
 }

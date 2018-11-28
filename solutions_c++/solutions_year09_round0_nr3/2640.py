 #include <conio.h>
 #include <stdio.h>
 #include <string.h>
 #define fi "welcome1.in"
 #define fo "welcome1.out"

 typedef char string500[500];
 int d[500],N,m;
 string500 str;
 char *w="welcome to code jam";
 /***************************/
 void init(string500 s){
	for (int i=0;i<strlen(s);i++)
		d[i]=0;
 }
 /**************************/
 int max(int a,int b){
	if (a>b) return a;
	else return b;
 }
 /***************************/
 void readfile(){
	int k,i,j;
	FILE *f=fopen(fi,"rt");
	FILE *g=fopen(fo,"wt");
	fscanf(f,"%d",&N);
	fgetc(f);
	for (k=0;k<N;k++){
	    fgets(str,500,f);
//	    printf("%s",str);
	    init(str);
	    if (str[0]=='w') d[0]=1;else d[0]=0;
	    for (i=1;i<strlen(str)-1;i++)
		if (str[i]=='w') d[i]=d[i-1]+1;
		else d[i]=d[i-1];

	    for (j=1;j<strlen(w);j++){
		d[j-1]=0;
		for (i=j;i<strlen(str)-1;i++)
			if (str[i]==w[j])
				d[i]=d[i]+d[i-1];
			else d[i]=d[i-1];
	    }
	    m=d[strlen(str)-2];
	    fprintf(g,"Case #%d: ",k+1);
	    if (m>1000) fprintf(g,"%d\n",m % 10000);
	    else {
		   if (m>99) fprintf(g,"0");
		   else if (m>9) fprintf(g,"00");
		   else fprintf(g,"000");
		   fprintf(g,"%d\n",m);
	    }
	}//end for i
	fclose(f);
	fclose(g);
 }
 /********************/

 void main()
 {
 clrscr();
 readfile();
 }
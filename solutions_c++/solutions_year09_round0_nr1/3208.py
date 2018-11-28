 #include <conio.h>
 #include <stdio.h>
 #include <string.h>
 #define fi "alien2.in"
 #define fo "alien2.out"

 typedef char string15[15];

 int i,j,h,D,L,K,N,o;
 string15 *s;
 char dd[15][26],str[420];
 /**********************/
 void init(int L){
 int i,j;
	for (i=0;i<L;i++)
		for (j=0;j<26;j++)
			dd[i][j]=0;
 }
 /**********************/
 void readfile(){
 int j;
 FILE *f=fopen(fi,"rt");
 FILE *g=fopen(fo,"wt");
 fscanf(f,"%d %d %d",&L,&D,&N);
 s=new string15[D];
 for (i=0;i<D;i++){
	fscanf(f,"%s",&s[i]);
 }
 for (i=0;i<N;i++){
	fscanf(f,"%s",str);
	init(L);
	j=0;
	o=0;
	h=0;
	 while (h<strlen(str)){
	    if (str[h]=='(') o=1;
	    if ( (str[h]!='(') && (str[h]!=')') )
		dd[j][str[h]-'a']=1;
	    if (o==0) j++; else
	    if (str[h]==')')  {j++;o=0;}
	    h++;
	}

	K=0;
	for (j=0;j<D;j++){
		o=1;
		for (h=0;h<strlen(s[j]);h++)
		     if (dd[h][s[j][h]-'a']==0) {
			o=0;
			break;
		     }
		if (o) K++;
	}
      printf("%d\n",K);
      fprintf(g,"Case #%d: %d\n",i+1,K);
 }
 fclose(g);
 fclose(f);
 }

/**************/
 void main()
 {
 clrscr();
 readfile();
 }
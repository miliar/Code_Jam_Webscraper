 #include <conio.h>
 #include <stdio.h>
 #define fi "B-large.in"
 #define fo "B-large.out"

 int h[101][101],H,W,T,top=0;
 char m[100][100],dd[10000];
 int dh[4]={-1,0,0,1},dw[4]={0,-1,1,0};

 /***************************/
 void init(){
 int i,j;
 for (i=0;i<H;i++)
	for (j=0;j<W;j++)
		m[i][j]=0;
 }
 /***************************/
 int smallest(int i,int j){
	int k,mink=-1,tmp=h[i][j];
	for (k=0;k<4;k++)
	     if ( (i+dh[k]>=0)&&(j+dw[k]>=0) )
		if (h[i+dh[k]][j+dw[k]]<tmp){
			tmp=h[i+dh[k]][j+dw[k]];
			mink=k;
		}
	return mink;
 }
 /***************************/
 int find_path(int i,int j){
   int k;
       if (m[i][j]!=0) return m[i][j];
       k=smallest(i,j);
       if (k>=0){
	 dd[top]=k;
	 top++;
	 return find_path(i+dh[k],j+dw[k]);
       }
	 else return -1;
 }
 /***************************/
 void readfile(){
 FILE *f=fopen(fi,"rt"),*g=fopen(fo,"wt");
 int i,j,k,k1,i1,j1;
 char c,e;

 fscanf(f,"%d",&T);
 for (i=0;i<T;i++){
      fscanf(f,"%d %d",&H,&W);
      for (j=0;j<H;j++)
	for (k=0;k<W;k++){
		fscanf(f,"%d",&h[j][k]);
	}
      init();
      for (j=0;j<H;j++) h[j][W]=32000;
      for (k=0;k<W;k++) h[H][k]=32000;

      c='a';
      for (j=0;j<H;j++)
	for (k=0;k<W;k++)
	     if (m[j][k]==0){
		top=0;
		e=find_path(j,k);
		if (e==-1) e=c++;
		m[j][k]=e;
		i1=j;
		j1=k;
		for (k1=0;k1<top;k1++){
		    i1=i1+dh[dd[k1]];
		    j1=j1+dw[dd[k1]];
		    m[i1][j1]=e;
		}
	     }

      fprintf(g,"Case #%d: \n",i+1);
      for (j=0;j<H;j++){
	for (k=0;k<W;k++)
	    fprintf(g,"%c ",m[j][k]);
	    fprintf(g,"\n");
      }
 } // end for i
 fclose(g);
 }
 /**************************/

 void main()
 {
 clrscr();
 readfile();
 }
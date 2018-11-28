 #include <conio.h>
 #include <stdio.h>
 #define fi "water1.in"
 #define fo "water1.out"

 int h[101][101],H,W,T;
 char m[100][100];
 int dh[4]={-1,0,0,1},dw[4]={0,-1,1,0};

 /***************************/
 void init(){
 int i,j;
 for (i=0;i<H;i++)
	for (j=0;j<W;j++)
		m[i][j]=0;
// m[0][0]='a';
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
 void spread(int i,int j,char c){
      int k,h,i1,j1;
      for (k=0;k<4;k++){
	  i1=i+dh[k];
	  j1=j+dw[k];
	  if ( (i1>=0)&&(j1>=0) ){
		h=smallest(i1,j1);
		if (h>-1)
			if ((i1+dh[h]==i)&&(j1+dw[h]==j) ){
			  if (m[i1][j1]==0){
			      m[i1][j1]=c;
			      spread(i1,j1,c);
			  }
			}
	  }
      }//end for

      k=smallest(i,j);
      if (k>-1)
	    if (m[i+dh[k]][j+dw[k]]==0)
		{
			m[i+dh[k]][j+dw[k]]=c;
			spread(i+dh[k],j+dw[k],c);
		}
 }
 /***************************/
 void readfile(){
 FILE *f=fopen(fi,"rt"),*g=fopen(fo,"wt");
 int i,j,k;
 char c;

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
		 m[j][k]=c;
		 spread(j,k,c);
		 c++;
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
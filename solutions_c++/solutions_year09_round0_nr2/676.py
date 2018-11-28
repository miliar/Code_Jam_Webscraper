#include <stdio.h>
#include <stdlib.h>
int now;
int chk;
char tmp;
int A[101][101];
int B[101][101];
 int h,w;
void walk(int a,int b)
{
int att=20000;
int num=0;
 if(a>1)
 {
  if(A[a][b]>A[a-1][b]&&A[a-1][b]<att)
  {
   att=A[a-1][b];	
   num=1;
  }
 }
 if(b>1)
 {
	 if(A[a][b]>A[a][b-1]&&A[a][b-1]<att)
  {
   att=A[a][b-1];	
   num=2;
  }
 }
 if(b<w)
 {
   	 if(A[a][b]>A[a][b+1]&&A[a][b+1]<att)
  {
   att=A[a][b+1];	
   num=3;
  }
 }
 if(a<h)
 {
   	 if(A[a][b]>A[a+1][b]&&A[a+1][b]<att)
  {
   att=A[a+1][b];	
   num=4;
  }
 }
 if(num==0)
 {
	if(B[a][b]==0)
	{
	chk=-1;
	B[a][b]=now;
	}
	else
	{
	chk=B[a][b];
	}
 }
 else if(num==1)
 {
	walk(a-1,b);
 }
 else if(num==2)
 {
	walk(a,b-1);
 }
 else if(num==3)
 {
	walk(a,b+1);
 }
 else if(num==4)
 {
	walk(a+1,b);
 }
}
void walk2(int a,int b,int c)
{
int att=20000;
int num=0;
B[a][b]=c;
 if(a>1)
 {
  if(A[a][b]>A[a-1][b]&&A[a-1][b]<att)
  {
   att=A[a-1][b];	
   num=1;
  }
 }
 if(b>1)
 {
	 if(A[a][b]>A[a][b-1]&&A[a][b-1]<att)
  {
   att=A[a][b-1];	
   num=2;
  }
 }
 if(b<w)
 {
   	 if(A[a][b]>A[a][b+1]&&A[a][b+1]<att)
  {
   att=A[a][b+1];	
   num=3;
  }
 }
 if(a<h)
 {
   	 if(A[a][b]>A[a+1][b]&&A[a+1][b]<att)
  {
   att=A[a+1][b];	
   num=4;
  }
 }
 if(num==1)
 {
	walk2(a-1,b,c);
 }
 else if(num==2)
 {
	walk2(a,b-1,c);
 }
 else if(num==3)
 {
	walk2(a,b+1,c);
 }
 else if(num==4)
 {
	walk2(a+1,b,c);
 }
}
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 int t;
 now=1;
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
	now=1;
	 for(int j=1;j<=100;j++)
	 {
	  for(int k=1;k<=100;k++)
	  {
	  A[j][k]=0;
	  B[j][k]=0;	
	  }	
	 }
	scanf("%d%d",&h,&w);
//	printf("%d %d\n",h,w);
	for(int j=1;j<=h;j++)
	{
	 for(int k=1;k<=w;k++)
	 {
		scanf("%d",&A[j][k]);
	 }
	}
	for(int j=1;j<=h;j++)
	{
	 for(int k=1;k<=w;k++)
	 {
		chk=0;
	  if(B[j][k]==0)
	  {
	  walk(j,k);	
	  if(chk==(-1)){B[j][k]=now;/*walk2(j,k,now);*/now++;}
	  else{B[j][k]=chk;/*walk2(j,k,chk);*/}
	  }
	 }
	}
	printf("Case #%d:\n",i);
	for(int j=1;j<=h;j++)
	{
	 for(int k=1;k<w;k++)
	 {
		tmp=B[j][k]+'a'-1;
	  printf("%c ",tmp);
	 }
	 tmp=B[j][w]+'a'-1;
	 printf("%c\n",tmp);
	}
 }
 return 0;
}

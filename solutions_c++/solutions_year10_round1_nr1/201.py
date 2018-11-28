#include <iostream>
#include <cstring>
using namespace std;
char map[55][55],tmp;
int fr,fb,t,n,k;
const int towt[8][2]={{0,1},{1,0},{0,-1},{-1,0},{1,1},{-1,-1},{1,-1},{-1,1}};

bool ok(int r,int c,int md)
{
 int i,rr,cc;
 for (i=1;i<k;i++)
  {
   rr=r+i*towt[md][0];
   cc=c+i*towt[md][1];
   if (rr<0||cc<0||rr>=n||cc>=n)
    return false;
   if (map[rr][cc]!=map[r][c]) 
    return false;
  }
  return true;
}

int main()
{
 int i,j,l,st,kk;
 freopen("out.txt","w",stdout);
 scanf("%d",&t);
 for (l=1;l<=t;l++)
  {	
  	fr=fb=0;
   	scanf("%d%d",&n,&k);
   	for (i=0;i<n;i++)
   	scanf("%s",map[i]);
	for (i=0;i<n;i++)
	 {
	  st=n-1;
	  j=n-1;
	  while (j>=0)
	  {
	   while (map[i][j]=='.'&&j>=0)
	   j--;
	   if (j>=0)
	    {
	    tmp=map[i][j];
	    map[i][j]=map[i][st];
	    map[i][st]=tmp;
	    st--;
	    j--;
	    }
	  }
	 }
	for (i=0;i<n;i++)
	 for (j=0;j<n;j++)
	  if (map[i][j]=='R')
	  {
	   for (kk=0;kk<8;kk++)
	    if (ok(i,j,kk)) fr++;
	  }
	  else if (map[i][j]=='B')
	  {
	    for (kk=0;kk<8;kk++)
	     if (ok(i,j,kk)) fb++;
	  }  
   printf("Case #%d: ",l);
   if (fr==0&&fb==0)
    printf("Neither\n");
   else if (fr>0&&fb>0)
    printf("Both\n");
   else if (fr>0)
    printf("Red\n");
   else 
    printf("Blue\n");	
	
  }	
 return 0;	
}

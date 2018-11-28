#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define in(x) (x>=0 && x<n)
#define lim 51

int cs,c,i,j,k,p,K,n,x,y;
char A[lim][lim],B[lim][lim];
int dx[]={-1,-1,0,1},dy[]={0,1,1,1};

bool f(char c)
{
  for(i=0;i<n;i++)
	for(j=0;j<n;j++)
	  for(k=0;k<4;k++)
	  {
		x=i;
		y=j;
		p=0;
		while(p<K && in(x) && in(y) && B[x][y]==c)
		{
		  x+=dx[k];
		  y+=dy[k];
		  p++;
		}
		if(p==K)
		  return 1;
	  }
  return 0;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&K);
	for(i=0;i<n;i++)
	  scanf("%s",A[i]);
	for(i=0;i<n;i++)
	  for(j=0;j<n;j++)
	    B[j][n-1-i]=A[i][j];
	for(i=0;i<n;i++)
	{
	  for(j=k=n-1;j>=0;j--)
	    if(B[j][i]!='.')
		  B[k--][i]=B[j][i];
	  while(k>=0)
	    B[k--][i]='.';
	}
	printf("Case #%d: ",c);
	if(f('R'))
	  if(f('B'))
	    printf("Both\n");
	  else
	    printf("Red\n");
	else
	  if(f('B'))
	    printf("Blue\n");
	  else
	    printf("Neither\n");
  }
  return 0;
}

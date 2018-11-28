#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define mod 10007
#define lim 110

int cs,c,n,m,r,i,x,y;
int M[lim][lim];
bool B[lim][lim];

int solve(int x,int y)
{
  int &res=M[x][y];
  
  if(res==-1)
  {
    if(x==n && y==m)
	  res=1;
	else
	{
	  res=0;
	  if(x+1<=n && y+2<=m && !B[x+1][y+2])
	    res=(res+solve(x+1,y+2))%mod;
	  if(x+2<=n && y+1<=m && !B[x+2][y+1])
	    res=(res+solve(x+2,y+1))%mod;
	}
  }
  return res;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d %d %d",&n,&m,&r);
	memset(B,0,sizeof B);
	memset(M,-1,sizeof M);
	for(i=0;i<r;i++)
	{
	  scanf("%d %d",&x,&y);
      B[x][y]=1;
	}
	printf("Case #%d: %d\n",c+1,solve(1,1));
  }
  return 0;
}

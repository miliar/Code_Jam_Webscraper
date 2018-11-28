#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define inf 1000000000
#define lim 10001
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,m,v,i;
int G[lim],C[lim],I[lim],M[lim][3];

int solve(int i,int j)
{
  int &res=M[i][j];
  
  if(res==-1)
  {
    if(i<=(m-1)/2)
	{
	  res=inf;
	  if(G[i]==0)
	  {
		if(j==0)
		  res=min(res,solve(2*i,0)+solve(2*i+1,0));
		else
		{
		  res=min(res,solve(2*i,1)+solve(2*i+1,0));
		  res=min(res,solve(2*i,0)+solve(2*i+1,1));
		  res=min(res,solve(2*i,1)+solve(2*i+1,1));
		}
	  }
	  else
		if(j==0)
		{
		  res=min(res,solve(2*i,1)+solve(2*i+1,0));
		  res=min(res,solve(2*i,0)+solve(2*i+1,1));
		  res=min(res,solve(2*i,0)+solve(2*i+1,0));
		}
		else
		  res=min(res,solve(2*i,1)+solve(2*i+1,1));
	  if(C[i]==1)
	    if(G[i]==0)
		{
		  if(j==0)
		  {
		    res=min(res,1+solve(2*i,1)+solve(2*i+1,0));
		    res=min(res,1+solve(2*i,0)+solve(2*i+1,1));
		    res=min(res,1+solve(2*i,0)+solve(2*i+1,0));
		  }
		  else
		  {
		    res=min(res,1+solve(2*i,1)+solve(2*i+1,1));
		  }
		}
	    else
		{
		  if(j==0)
		  {
		    res=min(res,1+solve(2*i,1)+solve(2*i+1,0));
		    res=min(res,1+solve(2*i,0)+solve(2*i+1,1));
		    res=min(res,1+solve(2*i,0)+solve(2*i+1,0));
		  }
		  else
		  {
		    res=min(res,1+solve(2*i,1)+solve(2*i+1,0));
		    res=min(res,1+solve(2*i,0)+solve(2*i+1,1));
		    res=min(res,1+solve(2*i,1)+solve(2*i+1,1));
		  }
		}
	}
	else
	  if(j==I[i])
	    res=0;
	  else
	    res=inf;
  }
  return res;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d %d",&m,&v);
	for(i=1;i<=(m-1)/2;i++)
	  scanf("%d %d",&G[i],&C[i]);
	for(i=(m-1)/2+1;i<=m;i++)
	  scanf("%d",&I[i]);
	memset(M,-1,sizeof M);
	if(solve(1,v)==inf)
	  printf("Case #%d: IMPOSSIBLE\n",c+1);
	else
	{
	  printf("Case #%d: %d\n",c+1,solve(1,v));
	}
  }
  return 0;
}

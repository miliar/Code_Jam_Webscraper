#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 210
#define inf 1000000000

int cs,c,i,j,k,n,m,res,s,t,x;
int A[lim][lim],M[lim][lim],P[lim],I[lim],O[lim];
queue <int> Q;

int bfs()
{
  int x,i,mn;

  while(!Q.empty())
    Q.pop();
  Q.push(s);
  memset(P,-1,sizeof P);
  P[s]=s;
  while(!Q.empty() && P[t]==-1)
  {
    x=Q.front();
//	printf("%d\n",x);
    Q.pop();
	for(i=0;i<=t;i++)
	{
	  if(M[x][i]>0 && P[i]==-1)
	  {
	    P[i]=x;
		Q.push(i);
	  }
	}
  }
  if(P[t]==-1)
    return 0;
  x=t;
  mn=M[P[x]][x];
  while(x!=s)
  {
    mn=min(mn,M[P[x]][x]);
	x=P[x];
  }
  x=t;
  while(x!=s)
  {
    M[P[x]][x]-=mn;
    M[x][P[x]]+=mn;
	x=P[x];
  }
  return mn;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)
	  for(j=0;j<m;j++)
	  {
	    scanf("%d",&A[i][j]);
	  }
	memset(M,0,sizeof M);
	memset(I,0,sizeof I);
	memset(O,0,sizeof O);
	s=2*n;
	t=s+1;
    for(i=0;i<n;i++)
	{
	  for(j=0;j<n;j++)
	  {
	    for(k=0;k<m;k++)
	      if(A[i][k]>=A[j][k])
		    break;
		if(k==m)
		{
		  M[2*i][2*j+1]=1;
//		  M[2*i+1][2*j]=1;
		  I[j]++;
		  O[i]++;
		}
	  }
	  M[s][2*i]=1;
	  M[2*i+1][t]=1;
	}
	res=0;
	while(1)
	{
	  x=bfs();
	  if(!x)
	    break;
	  res+=x;
	}
	printf("Case #%d: %d\n",c,n-res);
  }  
  return 0;
}



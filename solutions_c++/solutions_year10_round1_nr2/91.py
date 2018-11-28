#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 101
#define lim2 257

int cs,c,d,t,m,n,i,j,mn,s,mx;
int A[lim],M[lim][lim2],C[lim2];

int solve(int i,int j)
{
  int &res=M[i][j],k,p,s,dist;
  
  if(res==-1)
  {
    if(i==n-1)
	  res=0;
	else
	{
	  res=(n-1-i)*d;
	  res=min(res,solve(i+1,j)+d);
	  for(k=i+1;k<=i+1;k++)
	    for(p=0;p<256;p++)
	    {
          dist=abs(j-p);
		  if(!m && p!=j)
		    continue;
	      s=(k-1-i)*d+abs(p-A[k]);
		  if(m)
		    s+=max((dist-1)/m*t,0);
		  if(s<res)
		    res=min(res,s+solve(k,p));
	    }
	}
//    printf("%d %d %d\n",i,j,res);
  }
  return res;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d%d%d",&d,&t,&m,&n);
	for(i=mx=0;i<n;i++)
	  scanf("%d",&A[i]);
	memset(M,-1,sizeof M);
	mn=n*d;
	for(i=0;i<n;i++)
	  for(j=0;j<256;j++)
	  {
		s=i*d+abs(j-A[i]);
	    mn=min(mn,s+solve(i,j));
	  }
	printf("Case #%d: %d\n",c,mn);
  }  
  return 0;
}

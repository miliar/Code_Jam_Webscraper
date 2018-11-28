#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <string>
using namespace std;
#define lim 101
#define lim2 1001
#define print(x) cout<<#x<<":"<<x<<"\n"

int cs,c,s,q,i,j,mn;
char A[lim][lim],B[lim2][lim];
int M[lim2][lim];

int solve(int i,int j)
{
  int &res=M[i][j],k,m;
  
  if(res==-1)
  {
    if(i==q)
	  res=0;
	else
	{
	  k=i;
	  while(k<q && strcmp(B[k],A[j])!=0)
	    k++;
	  if(k==q)
	    res=0;
	  else
	    for(m=0;m<s;m++)
		  if(m!=j)
		  {
		    if(res==-1)
			  res=1+solve(k,m);
			res=min(res,1+solve(k,m));
		  }
	}
  }
  return res;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&s);
	gets(A[0]);
	for(i=0;i<s;i++)
	  gets(A[i]);
	scanf("%d",&q);
	gets(B[0]);
	for(i=0;i<q;i++)
	{
	  gets(B[i]);
	}
	memset(M,-1,sizeof M);
	for(i=q-1;i>=0;i--)
	  for(j=0;j<s;j++)
	    solve(i,j);
	mn=solve(0,0);
	for(i=0;i<s;i++)
	  mn=min(mn,solve(0,i));
	printf("Case #%d: %d\n",c+1,mn);
  }  
  return 0;
}

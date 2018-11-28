#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define lim 11
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,len,i;
char A[lim][lim];
int M[lim][(1<<10)+1];

int solve(int k,int mask)
{
  int &res=M[k][mask],m2,i,cnt;
  
  if(res==-1)
  {
    if(k==n)
	  res=0;
	else
	{
	  res=0;
	  for(m2=0;m2<(1<<len);m2++)
	  {
	    cnt=0;
	    for(i=0;i<len;i++)
		  if((m2 & (1<<i))!=0)
		  {
		    if(A[k][i]=='x' || (i-1>=0 && (m2 & (1<<(i-1)))!=0) || (i+1<len && (m2 & (1<<(i+1)))!=0) || (i-1>=0 && (mask & (1<<(i-1)))!=0) || (i+1<len && (mask & (1<<(i+1)))!=0))
		      break;
		    cnt++;
		  }
	    if(i>=len-1 && ((m2 & (1<<0))==0 || A[k][0]!='x') && ((m2 & (1<<(len-1)))==0 || A[k][len-1]!='x'))
		{
		  res=max(res,solve(k+1,m2)+cnt);
	    }
	  }  
	}
//	printf("%d %d %d\n",k,mask,res);
  }
  return res;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d %d",&n,&len);
	for(i=0;i<n;i++)
	  scanf("%s",A[i]);
	memset(M,-1,sizeof M);
	printf("Case #%d: %d\n",c+1,solve(0,0));
  }
  return 0;
}

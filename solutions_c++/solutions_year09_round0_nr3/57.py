#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 501

int cs,c,n;
char str[lim];
int M[lim][20];

int solve(int i,int j)
{
  int &res=M[i][j];
  
  if(res==-1)
    if(j==19)
	  res=1;
	else if(i==n)
	  res=0;
	else
	{
	  res=solve(i+1,j);
	  if(str[i]=="welcome to code jam"[j])
	    res=(res+solve(i+1,j+1))%10000;
	}
  return res;
}
int main()
{
  scanf("%d ",&cs);
  for(c=1;c<=cs;c++)
  {
    gets(str);
	n=strlen(str);
	memset(M,-1,sizeof M);
	printf("Case #%d: %04d\n",c,solve(0,0));
  }  
  return 0;
}

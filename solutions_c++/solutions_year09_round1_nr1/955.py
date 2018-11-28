#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <sstream>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim2 11
#define lim 10000

int i,j,n,res,mx,s,c,cs;
bool B[2*lim],M[lim2][lim];
int A[lim2];
char str[1000000];

int next(int n,int b)
{
  int res=0;

  s++;
  while(n!=0)
  {
    res+=(n%b)*(n%b);
    n/=b;
  }
  return res;
}
bool happy(int n,int b)
{
  int x=n;

  memset(B,0,sizeof B);
  while(1)
  {
    mx=max(mx,n);
    if(n==1)
	  return 1;
	B[n]=1;
	n=next(n,b);
	if(B[n])
	  return 0;
  }
}
int main()
{
  scanf("%d ",&cs);
  for(c=1;c<=cs;c++)
  {
    gets(str);
	stringstream ss(str);
	n=0;
	while(ss>>A[n])
	  n++;
	for(res=2;;res++)
	{
	  for(j=0;j<n;j++)
	  {
	    if(!happy(res,A[j]))
		  break;
	  } 
	  if(j==n)
	    break;
	}
	printf("Case #%d: %d\n",c,res);
  } 
  return 0;
}

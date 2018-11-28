#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 41

int cs,c,n,i,j,k,res;
int R[lim];
char str[lim];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	  scanf("%s",str);
      R[i]=n-1;
	  while(R[i]>=0 && str[R[i]]=='0')
	    R[i]--;
	  R[i]++;
	}
	for(i=1,res=0;i<=n;i++)
	{
	  for(j=i;j<=n && R[j]>i;j++);
	  for(k=j-1;k>=i;k--)
	    R[k+1]=R[k];
	  res+=j-i;
	}
	printf("Case #%d: %d\n",c,res);
  }
  return 0;
}



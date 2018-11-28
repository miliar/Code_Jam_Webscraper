#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 10001

int c,cs,i,j,n,d;
int M[lim],D[lim],L[lim];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d%d",&D[i],&L[i]);
    scanf("%d",&d);
    memset(M,-1,sizeof M);
    M[0]=0;
    for(i=0;i<n && M[i]!=-1;i++)
      for(j=i+1;j<n && D[i]-M[i]+D[i]>=D[j];j++)
        if(M[j]==-1)
          M[j]=max(D[i],D[j]-L[j]);
    for(i=0;i<n;i++)
      if(M[i]!=-1 && D[i]-M[i]+D[i]>=d)
        break;
    printf("Case #%d: %s\n",c,i==n?"NO":"YES");
  }
  return 0;
}

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,i,j,m,n,d,a,z;
double ll,rr,t,x;
int A[1000001];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&d);
    for(i=m=0;i<n;i++)
    {
      scanf("%d%d",&a,&z);
      while(z--)
        A[m++]=a;
    }
    sort(A,A+m);
    ll=0;
    rr=1e9;
    for(j=0;j<333;j++)
    {
      t=(ll+rr)/2;
      for(i=1,x=A[0]-t;i<m;i++)
      {
        x=max(x+d,A[i]-t);
        if(x>A[i]+t)
          break;
      }
      if(i==m)
        rr=t;
      else
        ll=t;
    }
    printf("Case #%d: %.10lf\n",c,t);
  }
  return 0;
}

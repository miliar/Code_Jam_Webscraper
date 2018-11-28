#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,i,x[5],y[5],r[5];
double d,R;
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d",&n); R=0;
    for (i=1; i<=n; i++) {
      scanf("%d%d%d",&x[i],&y[i],&r[i]);
      if (r[i]>R) R=r[i];
    }
    if (n==3) {
      d=sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]))+r[2]+r[1];
      R=max(d/2.0,double(r[3]));
      d=sqrt((x[3]-x[1])*(x[3]-x[1])+(y[3]-y[1])*(y[3]-y[1]))+r[3]+r[1];
      R=min(R,max(d/2.0,double(r[2])));
      d=sqrt((x[2]-x[3])*(x[2]-x[3])+(y[2]-y[3])*(y[2]-y[3]))+r[2]+r[3];
      R=min(R,max(d/2.0,double(r[1])));
    }
    printf("Case #%d: %.7lf\n",tt,R);
  }
  return 0;
}

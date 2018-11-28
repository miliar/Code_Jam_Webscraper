#include <stdio.h>
int t,tt,i,j,a,n,m;
long double p,x,f[1010],r[1010],z[1010];
int main() {
  freopen("Dl.in","r",stdin);
  freopen("Dl.out","w",stdout);
  f[0]=f[1]=z[0]=z[2]=1;
  for (i=2; i<1005; i++) {
    z[i+1]=(z[i]+z[i-1])*i;
    f[i]=f[i-1]*i;
  }
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d",&n); m=n;
    for (i=0; i<n; i++) {
      scanf("%d",&a);
      if (a==i+1) m--;
    }
    for (i=2; i<=m; i++) {
      r[i]=p=0;
      for (j=1; j<=i; j++) { x=z[i-j]/f[j]/f[i-j]; p+=x; r[i]+=r[i-j]*x; }
      r[i]=(r[i]+1.0)/p;
    }
    printf("Case #%d: %.8lf\n",tt,double(r[m]));
  }
  return 0;
}

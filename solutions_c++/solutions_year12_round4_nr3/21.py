#include <stdio.h>
const int MX=2020,INF=1000000000;
int t,tt,n,i,j,k,a[MX],b[MX];
bool q;
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    q=true;
    for (i=1; i<=n; i++) b[i]=INF;
    for (i=1; i<n; i++) {
      scanf("%d",&a[i]);
      if (a[i]<=i) q=false;
      for (j=1; j<i; j++) if (a[j]>i && a[j]<a[i]) q=false;
    }
    printf("Case #%d:",t);
    if (q) {
      for (i=1; i<n; i++) for (j=a[i], k=0; j>i; j--, k++) b[j]-=k;
      for (i=1; i<=n; i++) if (b[i]<0) break;
      if (i>n) {
        for (i=1; i<=n; i++) printf(" %d",b[i]);
        puts("");
      } else puts(" Impossible");
    } else puts(" Impossible");
  }
  return 0;
}

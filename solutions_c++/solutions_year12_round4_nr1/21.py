#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,i,j,x,a[10010],b[10010],c[10010];
bool q;
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (i=0; i<n; i++) {
      scanf("%d%d",&a[i],&b[i]);
      if (i) {
        for (c[i]=j=0; j<i; j++) if (a[j]+c[j]>=a[i]) c[i]=max(c[i],a[i]-a[j]);
        c[i]=min(c[i],b[i]);
      } else c[i]=a[i];
    }
    scanf("%d",&x);
    for (q=i=0; i<n; i++) if (a[i]+c[i]>=x) q=true;
    printf("Case #%d: ",t);
    puts(q?"YES":"NO");
  }
  return 0;
}

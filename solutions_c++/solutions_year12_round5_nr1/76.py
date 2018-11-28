#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,i,n,l[1010],p[1010],k[1010];
bool cmp(int i, int j) {
  return p[i]*l[j]>p[j]*l[i] || (p[i]*l[j]==p[j]*l[i] && i<j);
}
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (i=0; i<n; i++) scanf("%d",&l[i]);
    for (i=0; i<n; i++) { scanf("%d",&p[i]); k[i]=i; }
    sort(k,k+n,cmp);
    printf("Case #%d:",t);
    for (i=0; i<n; i++) printf(" %d",k[i]);
    puts("");
  }
  return 0;
}

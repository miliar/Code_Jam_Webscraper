#include <stdio.h>
int t,tt,n,m,r,s,i,a;
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d",&n);
    m=1000100; r=s=0;
    for (i=0; i<n; i++) {
      scanf("%d",&a);
      if (a<m) m=a;
      r^=a; s+=a;
    }
    printf("Case #%d: ",tt);
    if (r==0) printf("%d\n",s-m); else puts("NO");
  }
  return 0;
}

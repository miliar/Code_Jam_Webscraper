#include <stdio.h>
int v[105];
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<= casn; ++cas) {
    int n, l, h;
    scanf("%d%d%d", &n, &l, &h);
    for(int i=0; i<n; ++i) {
      scanf("%d", v+i);
    }
    for(int i=l; i<=h; ++i) {
      int f=1;
      for(int j=0; j<n && f; ++j) {
        if(v[j]%i!=0 && i%v[j]!=0) f=0;
      }
      if(f==1) {
        printf("Case #%d: %d\n", cas, i);
        goto con;
      }
    }
    printf("Case #%d: NO\n", cas);
    con: continue;
  }
  return 0;
}

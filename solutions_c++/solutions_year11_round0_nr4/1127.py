#include <stdio.h>
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    int n, cnt=0;
    scanf("%d", &n);
    for(int i=1; i<=n; ++i) {
      int t;
      scanf("%d", &t);
      if(i != t) ++cnt;
    }
    printf("Case #%d: %.10f\n", cas, cnt*1.0);
  }
  return 0;
}

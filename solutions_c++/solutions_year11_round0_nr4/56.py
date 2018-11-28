#include <stdio.h>

int main() {
  int tests; scanf("%d",&tests);
  for (int t=1;t<=tests;++t) {
    int n; scanf("%d",&n);
    int r = 0;
    for(int i=1;i<=n;++i) {
      int x; scanf("%d",&x);
      r += (x!=i);
    }
    printf("Case #%d: %d\n",t,r);
  }
}

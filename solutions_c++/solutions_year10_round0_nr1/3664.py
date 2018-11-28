#include <cstdio>
#include <cassert>

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; tt++) {
    int n, k;
    assert(scanf("%d%d", &n, &k) == 2);
    printf("Case #%d: %s\n", tt, ((k + 1) % (1 << n) == 0) ? "ON" : "OFF");
  }
  return 0;
}

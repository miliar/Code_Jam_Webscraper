#include <cassert>
#include <cstdio>

int main() {
  int t, n, k;
  assert(scanf("%d", &t) == 1);
  for (int i = 0; i < t; i++) {
    assert(scanf("%d%d", &n, &k) == 2);
    printf("Case #%d: %s\n", i + 1, (k & ((1 << n) - 1)) == (1 << n) - 1 ? "ON" : "OFF");
  }
  return 0;
}


#include <cstdio>

int main() {
  int T;

  scanf(" %d", &T);
  for (int cases = 1; cases <= T; cases++) {
    int n, k, f;
    scanf(" %d%d", &n, &k);
    f = 1 << n;
    printf("Case #%d: %s\n", cases, k % f == f - 1 ? "ON" : "OFF");
  }

  return 0;
}

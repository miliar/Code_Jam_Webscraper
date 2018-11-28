#include <stdio.h>

int main() {
  int T;
  int n, k;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &n, &k);
    bool f = true;
    for (int i = 0; i < n; i++) if (((1<<i) & k) == 0) { f = false; break; }
    printf("Case #%d: %s\n", t, f ? "ON" : "OFF");
  }
  return 0;
}

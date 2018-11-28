#include <stdio.h>

int T, N, K;

int main() {
  freopen("snapper.in", "r", stdin);
  freopen("snapper.out", "w", stdout);

  scanf("%d ", &T);

  for (int i = 1; i <= T; i++) {
    scanf("%d %d ", &N, &K);
    if (K % (1 << N) == (1 << N) - 1) {
      printf("Case #%d: ON\n", i);
    } else {
      printf("Case #%d: OFF\n", i);
    }
  }

  return 0;
}

#include <stdio.h>

int N, K;

int main() {
  int tc;
  scanf("%d", &tc);
  for (int __t = 1; __t <= tc; ++__t) {
    scanf("%d %d", &N, &K);
    ++K;

    int res = __builtin_ctz(K);
    printf("Case #%d: %s\n", __t, res >= N ? "ON" : "OFF");
  }
}

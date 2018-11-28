#include <cstdio>

int main(void) {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i) {
    long long N, K;
    scanf("%lld%lld", &N, &K);
    printf("Case #%d: O%s\n", i, K % (1LL<<N) == (1LL<<N)-1 ? "N" : "FF");
  }
  return 0;
}

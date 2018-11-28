#include <cstdio>

int main() {
  int T; long long N, K;
  scanf ("%d", &T);
  for (int i=0; i<T; ++i) {
    scanf ("%lld %lld", &N, &K);
    long long M = (1 << N) - 1;
    printf ("Case #%d: %s\n", i+1, ((K & M) == M) ? "ON" : "OFF");
  }
  return 0;
}

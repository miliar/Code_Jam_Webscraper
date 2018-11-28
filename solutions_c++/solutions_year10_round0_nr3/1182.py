#include <stdio.h>

const int MAXN = 1 << 10;
const int MAXNN = MAXN * 2;

long long R, K, N, NN;
long long vec[MAXNN];
long long sum[MAXNN];

int main() {
  int tc;
  scanf("%d", &tc);
  for (int __t = 1; __t <= tc; ++__t) {
    printf("Case #%d: ", __t);

    scanf("%lld %lld %lld", &R, &K, &N); NN = N * 2;
    for (int i = 0; i < N; ++i)
      scanf("%lld", vec + i);
    for (int i = N; i < NN; ++i) {
      vec[i] = vec[i-N];
    }
    sum[NN] = 0;
    for (int i = NN-1; i >= 0; --i)
      sum[i] = sum[i+1] + vec[i];

    if (sum[N] <= K) {
      printf("%lld\n", sum[N] * R);
      continue;
    }
    int cidx = 0;
    long long res = 0;
    for (int r = 0; r < R; ++r) {
      int l = cidx, r = cidx + N, m;
      while (l + 1 < r) {
        m = (l + r) / 2;
        if (sum[cidx] - sum[m+1] <= K)
          l = m;
        else
          r = m;
      }
      res += sum[cidx] - sum[r];
      cidx = r % N;
    }
    printf("%lld\n", res);
  }

  return 0;
}

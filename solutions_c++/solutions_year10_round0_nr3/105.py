#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;

const int kMaxN = 1000 + 24;

int R, k, N;
int g[kMaxN];
int p[kMaxN];
ll psum[kMaxN];

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d %d %d", &R, &k, &N);
    ll sum = 0, result;
    for (int i = 0; i < N; ++i) {
      scanf("%d", g + i);
      sum += g[i];
    }
    if (sum <= k) {
      result = R * sum;
    } else {
      ll seg = 0;
      for (int i = 0, j = 0; i < N; ++i) {
        for (; seg + g[j] <= k; j = (j + 1) % N)
          seg += g[j];
        psum[i] = seg;
        p[i] = j;
        seg -= g[i];
      }
      int u, v;
      for (u = p[0], v = p[p[0]]; u != v; u = p[u], v = p[p[v]]);
      for (u = 0; u != v; u = p[u], v = p[v]);
      int Tl = 1;
      ll Tsum = psum[u];
      for (int i = p[u]; i != u; ++Tl, i = p[i])
        Tsum += psum[i];
      result = 0;
      for (int i = 0; i != u && R > 0; i = p[i], --R)
        result += psum[i];
      result += (R / Tl) * Tsum;
      R %= Tl;
      for (int i = u; p[i] != u && R > 0; i = p[i], --R)
        result += psum[i];
    }
    printf("%lld\n", result);
  }
  return 0;
}

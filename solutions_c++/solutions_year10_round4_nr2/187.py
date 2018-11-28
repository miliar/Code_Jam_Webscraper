#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;

const int kMaxN = 4096;
const ll kInf = 100000000;

int P, N;
int m[kMaxN];
int cost[kMaxN];
ll f[kMaxN][kMaxN];

ll Find(int i, int j) {
  if (f[i][j] != -1) {
    return f[i][j];
  }
  if (i >= N) {
    if (j >= m[i - N + 1]) return f[i][j] = 0;
    else return f[i][j] = kInf;
  }
  ll t1 = Find(2 * i, j + 1) + Find(2 * i + 1, j + 1) + cost[i];
  ll t2 = Find(2 * i, j) + Find(2 * i + 1, j);
  return f[i][j] = min(t1, t2);
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d", &P);
    N = (1 << P);
    for (int i = N; i >= 1; --i) {
      scanf("%d", m + i);
      m[i] = P - m[i];
    }
    for (int i = N - 1; i >= 1; --i)
      scanf("%d", cost + i);
    //for (int i = 1; i <= N; ++i)
    //  printf("%d ", m[i]);
    //printf("\n");
    //for (int i = 1; i <= N; ++i)
    //  printf("%d ", cost[i]);
    //printf("\n");
    for (int i = 1; i <= 2 * N; ++i)
      fill(f[i], f[i] + P + 1, -1);
    printf("%lld\n", Find(1, 0));
    //for (int i = 1; i <= N; ++i) {
    //  for (int j = 0; j <= P; ++j)
    //    printf("%d ", f[i][j]);
    //  printf("\n");
    //}
  }
  return 0;
}

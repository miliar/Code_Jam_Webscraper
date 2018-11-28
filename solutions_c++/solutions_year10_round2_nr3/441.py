#include <cstring>
#include <cstdio>
using namespace std;

const int maxn = 501, mod = 100003;
typedef long long ll;
ll f[maxn + 1][maxn + 1], g[maxn + 1];

ll calc(int n, int m) {
  if (n < 0) return 0;
  if (f[n][m] != -1) return f[n][m];

  ll ret = 0;
  if (n == 0) ret = 1;
  else {
    for (int i = 1; i <= m; ++i)
      ret = (ret + calc(n - i, m)) % mod;
  }

  return f[n][m] = ret;
}

int main() {
  int cases;

  memset(f, -1, sizeof(f));
  g[0] = 0;
  for (int i = 1; i <= maxn; ++i) {
    g[i] = 0;
    for (int j = 0; j <= i; ++j)
      g[i] = (g[i] + calc(i - j, j)) % mod;
  }

  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    int n;
    scanf("%i", &n);
    printf("Case #%i: %lli\n", numcase, g[n - 1]);
  }
  return 0;
}

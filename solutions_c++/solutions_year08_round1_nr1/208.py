# include <cstdio>
# include <cstring>
# include <algorithm>

using namespace std;

const int maxn = 1000;

# define long long long

int a[maxn], b[maxn], n;
long res;

void init() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%d", a + i);
  for (int i = 0; i < n; ++i) scanf("%d", b + i);
}

void solve() {
  sort(a, a + n);
  sort(b, b + n);

  long res = 0;
  for (int i = 0; i < n; ++i) res += (long)a[i] * b[n - i - 1];

  printf("%I64d\n", res);
}

int main() {
  int tt, i;
  for (scanf("%d", &tt), i = 1; i <= tt; ++i) {
    init();
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

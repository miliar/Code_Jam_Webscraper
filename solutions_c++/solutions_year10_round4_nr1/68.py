#include <cassert>
#include <cstdio>

#include <algorithm>

const int maxn = 100;
int n, a[2 * maxn][2 * maxn];

bool is( int x, int y ) {
  using std::abs;
  using std::min;
  return !(y < 0 || y >= 2 * n - 1 || x < abs(n - 1 - y) || x > min(n - 1 + y, 3 * n - 3 - y));
}

bool test( int x, int y, int ta ) {
  if (!is(x, y))
    return false;
  return a[y][x] != ta;
}

int main() {
  using std::min;
  using std::max;
  using std::abs;
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    assert(scanf("%d", &n) == 1);
    for (int y = 0; y < 2 * n - 1; y++)
      for (int x = abs(n - 1 - y); is(x, y); x += 2)
        assert(scanf("%d", &a[y][x]));
    int ans = (int)1e9;
    for (int cy = 0; cy < 2 * n - 1; cy++)
      for (int cx = 0; cx < 2 * n - 1; cx++) {
        int k = 0;
        for (int y = 0; y < 2 * n - 1; y++)
          for (int x = abs(n - 1 - y); is(x, y); x += 2)
            k = max(k, abs(y - cy) + abs(x - cx) + 1);
        bool ok = true;
        for (int y = 0; y < 2 * n - 1 && ok; y++)
          for (int x = abs(n - 1 - y); is(x, y) && ok; x += 2)
            if (test(x, y, a[y][x]) || test(2 * cx - x, y, a[y][x]) ||
                test(x, 2 * cy - y, a[y][x]) || test(2 * cx - x, 2 * cy - y, a[y][x]))
              ok = false;
        if (ok)
          ans = min(ans, k);
//        fprintf(stderr, "cx = %d, cy = %d, ok = %d, k = %d\n", cx, cy, ok, k);
      }
    printf("Case #%d: %d\n", tt, ans * ans - n * n);
  }
  return 0;
}


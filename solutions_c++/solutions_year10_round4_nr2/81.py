#include <cassert>
#include <cstdio>
#include <algorithm>

using std::min;
using std::max;

int main() {
  int tn, p;
  assert(scanf("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    assert(scanf("%d", &p));
    int m[(1 << p)], c[(1 << p)], d[(2 << p)][p + 1];
    for (int i = 0; i < (1 << p); i++)
      assert(scanf("%d", &m[i]) == 1), m[i] = min(m[i], p);
    for (int i = 0; i < (1 << p) - 1; i++)
      assert(scanf("%d", &c[(1 << p) - 2 - i]) == 1);
    for (int i = 0; i < (1 << p); i++)
      for (int j = 0; j <= p; j++)
        if (j <= m[(1 << p) - 1 - i])
          d[i + (1 << p)][j] = 0;
        else
          d[i + (1 << p)][j] = (int)1e9;
    for (int i = (1 << p) - 1; i > 0; i--) {
      for (int j = 0; j < p; j++) {
        d[i][j] = min(d[i * 2][j + 1] + d[i * 2 + 1][j + 1], (int)1e9);
        d[i][j] = min(d[i][j], c[i - 1] + d[i * 2][j] + d[i * 2 + 1][j]);
      }
      d[i][p] = (int)1e9;
    }
    /*
    for (int i = (2 << p) - 1; i > 0; i--)
      for (int j = 0; j <= p; j++)
        fprintf(stderr, "d[i=%d][j=%d] = %d\n", i, j, d[i][j]);
    */
    printf("Case #%d: %d\n", tt, d[1][0]);
  }
  return 0;
}


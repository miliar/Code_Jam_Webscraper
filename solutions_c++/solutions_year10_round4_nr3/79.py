#include <cassert>
#include <cstdio>
#include <cstring>

const int maxr = 100;
int c[2][maxr + 1][maxr + 1];

int main() {
  int tn, n;
  assert(scanf("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    assert(scanf("%d", &n) == 1);
    memset(c, 0, sizeof(c));
    for (int i = 0; i < n; i++) {
      int x1, y1, x2, y2;
      assert(scanf("%d%d%d%d", &x1, &y1, &x2, &y2) == 4);
      for (int x = x1; x <= x2; x++)
        for (int y = y1; y <= y2; y++)
          c[0][x][y] = 1;
    }
    int ans = 0, t = 0;
    while (true) {
      bool ok = false;
      for (int x = 1; x <= maxr && !ok; x++)
        for (int y = 1; y <= maxr && !ok; y++)
          if (c[t][x][y])
            ok = true;
      if (!ok)
        break;
      ans++;
      for (int x = 1; x <= maxr; x++)
        for (int y = 1; y <= maxr; y++)
          if (c[t][x - 1][y] && c[t][x][y - 1])
            c[t ^ 1][x][y] = 1;
          else if (!c[t][x - 1][y] && !c[t][x][y - 1])
            c[t ^ 1][x][y] = 0;
          else
            c[t ^ 1][x][y] = c[t][x][y];
      t ^= 1;
    }
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}


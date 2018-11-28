#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

const int maxN = 500;

int s[maxN][maxN];
int sx[maxN][maxN];
int sy[maxN][maxN];
char a[maxN][maxN + 1];
int w, h;

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d: ", tt);
    assert(scanf("%d%d%*d", &h, &w) == 2);
    for (int i = 0; i < h; i++) {
      assert(scanf("%s", a[i]) == 1);
    }
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        s[i][j] = a[i][j] - '0';
        sx[i][j] = j * (a[i][j] - '0');
        sy[i][j] = i * (a[i][j] - '0');
        if (i > 0) {
          s[i][j] += s[i - 1][j];
          sx[i][j] += sx[i - 1][j];
          sy[i][j] += sy[i - 1][j];
        }
        if (j > 0) {
          s[i][j] += s[i][j - 1];
          sx[i][j] += sx[i][j - 1];
          sy[i][j] += sy[i][j - 1];
        }
        if (i > 0 && j > 0) {
          s[i][j] -= s[i - 1][j - 1];
          sx[i][j] -= sx[i - 1][j - 1];
          sy[i][j] -= sy[i - 1][j - 1];
        }
      }
    }
    int ans = -1;
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        for (int l = 3; i + l <= h && j + l <= w; l++) {
          int tx = sx[i + l - 1][j + l - 1];
          int ty = sy[i + l - 1][j + l - 1];
          int ts = s[i + l - 1][j + l - 1];
          if (i > 0) {
            tx -= sx[i - 1][j + l - 1];
            ty -= sy[i - 1][j + l - 1];
            ts -= s[i - 1][j + l - 1];
          }
          if (j > 0) {
            tx -= sx[i + l - 1][j - 1];
            ty -= sy[i + l - 1][j - 1];
            ts -= s[i + l - 1][j - 1];
          }
          if (i > 0 && j > 0) {
            tx += sx[i - 1][j - 1];
            ty += sy[i - 1][j - 1];
            ts += s[i - 1][j - 1];
          }
          tx -= j * (a[i][j] + a[i + l - 1][j] - 2 * '0') + (j + l - 1) * (a[i][j + l - 1] + a[i + l - 1][j + l - 1] - 2 * '0');
          ty -= i * (a[i][j] + a[i][j + l - 1] - 2 * '0') + (i + l - 1) * (a[i + l - 1][j] + a[i + l - 1][j + l - 1] - 2 * '0');
          ts -= (a[i][j] + a[i][j + l - 1] - 2 * '0') + (a[i + l - 1][j] + a[i + l - 1][j + l - 1] - 2 * '0');
//          fprintf(stderr, "l=%d y=%lf x=%lf w=%lf yy=%lf xx=%lf\n", l, (i + i + l - 1) * 0.5, (j + j + l - 1) * 0.5, ts * 1.0, ty * 1.0 / ts, tx * 1.0 / ts);
          if (ty * 2 == (i + i + l - 1) * ts && tx * 2 == (j + j + l - 1) * ts) {
            ans = max(ans, l);
          }
        }
      }
    }
    if (ans == -1) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}

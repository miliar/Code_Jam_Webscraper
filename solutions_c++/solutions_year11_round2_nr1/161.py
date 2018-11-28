#include <cstdio>
#include <cassert>

const int maxN = 100;

int n;
char a[maxN][maxN + 1];
double wp[maxN], owp[maxN], oowp[maxN];

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d:\n", tt);

    assert(scanf("%d", &n) == 1);
    for (int i = 0; i < n; i++) {
      assert(scanf("%s", a[i]));
    }

    for (int i = 0; i < n; i++) {
      int cnt = 0, cntW = 0;
      for (int j = 0; j < n; j++) {
        if (a[i][j] != '.') {
          cnt++;
          if (a[i][j] == '1') {
            cntW++;
          }
        }
      }
      wp[i] = (double)cntW / cnt;

      int cntO = 0;
      double sumWP = 0.0;
      for (int j = 0; j < n; j++) {
        if (a[i][j] == '.') {
          continue;
        }
        int cnt = 0, cntW = 0;
        for (int k = 0; k < n; k++) {
          if (k == i) {
            continue;
          }
          if (a[j][k] != '.') {
            cnt++;
            if (a[j][k] == '1') {
              cntW++;
            }
          }
        }
        cntO++;
        sumWP += (double)cntW / cnt;
      }
      owp[i] = sumWP / cntO;
    }
    for (int i = 0; i < n; i++) {
      int cntO = 0;
      double sumOWP = 0.0;
      for (int j = 0; j < n; j++) {
        if (a[i][j] == '.') {
          continue;
        }
        cntO++;
        sumOWP += owp[j];
      }
      oowp[i] = sumOWP / cntO;
    }
    for (int i = 0; i < n; i++) {
      printf("%.9lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
    }
  }
  return 0;
}

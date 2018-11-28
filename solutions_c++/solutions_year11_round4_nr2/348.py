#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

const int kMaxN = 500;

char mat[kMaxN][kMaxN + 1];
double t_mass[kMaxN][kMaxN], t_x[kMaxN][kMaxN], t_y[kMaxN][kMaxN];
int n, m, d;
int ret;

inline double val(int x, int y) { return d + mat[x][y] - '0'; }
inline int sgn(double x) {
  if (abs(x) < 1e-9) return 0;
  return x < 0 ? -1 : 1;
}

void dec(int i, int j, double &mass_t, double &x_t, double &y_t) {
  mass_t -= val(i, j);
  x_t -= val(i, j) * i;
  y_t -= val(i, j) * j;
}

void update(int i, int j, int size, double mass_t, double x_t, double y_t) {
  dec(i, j, mass_t, x_t, y_t);
  dec(i, j + size - 1, mass_t, x_t, y_t);
  dec(i + size - 1, j, mass_t, x_t, y_t);
  dec(i + size - 1, j + size - 1, mass_t, x_t, y_t);
  x_t /= mass_t;
  y_t /= mass_t;
  double cx = i + (size - 1) / 2.0, cy = j + (size - 1) / 2.0;
  if (sgn(cx - x_t) == 0 && sgn(cy - y_t) == 0) {
    ret = max(ret, size);
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d%d%d", &n, &m, &d);
    for (int i = 0; i < n; ++i) {
      scanf("%s", mat[i]);
    }
    ret = 0;
    for (int i = 3; i <= min(n, m); ++i) {
      for (int j = 0; j < n; ++j) {
        t_mass[j][0] = val(j, 0);
        t_x[j][0] = val(j, 0) * j;
        t_y[j][0] = val(j, 0) * 0;
        for (int k = 1; k < i; ++k) {
          t_mass[j][k] = t_mass[j][k - 1] + val(j, k);
          t_x[j][k] = t_x[j][k - 1] + val(j, k) * j;
          t_y[j][k] = t_y[j][k - 1] + val(j, k) * k;
        }
        for (int k = i; k < m; ++k) {
          t_mass[j][k] = t_mass[j][k - 1] + val(j, k) - val(j, k - i);
          t_x[j][k] = t_x[j][k - 1] + val(j, k) * j - val(j, k - i) * j;
          t_y[j][k] = t_y[j][k - 1] + val(j, k) * k - val(j, k - i) * (k - i);
        }
      }
      for (int j = i - 1; j < m; ++j) {
        double tmass = 0, tx = 0, ty = 0;
        for (int k = 0; k < i; ++k) {
          tmass += t_mass[k][j];
          tx += t_x[k][j];
          ty += t_y[k][j];
        }
        update(0, j - (i - 1), i, tmass, tx, ty);
        for (int k = i; k < n; ++k) {
          tmass += t_mass[k][j] - t_mass[k - i][j];
          tx += t_x[k][j] - t_x[k - i][j];
          ty += t_y[k][j] - t_y[k - i][j];
          update(k - (i - 1), j - (i - 1), i, tmass, tx, ty);
        }
      }
    }
    printf("Case #%d: ", tt);
    if (ret == 0) puts("IMPOSSIBLE");
    else printf("%d\n", ret);
  }
  return 0;
}

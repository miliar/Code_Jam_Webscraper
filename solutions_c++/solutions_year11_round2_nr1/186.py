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

const int kMaxN = 100;

char mat[kMaxN][kMaxN + 1];
double wp[kMaxN], owp[kMaxN], oowp[kMaxN];
int wpc[kMaxN], owpc[kMaxN], oowpc[kMaxN];

int main() {
  int T, n;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s", mat[i]);
    }
    for (int i = 0; i < n; ++i) {
      int w = 0, l = 0;
      for (int j = 0; j < n; ++j) {
        if (mat[i][j] == '1') ++w;
        else if (mat[i][j] == '0') ++l;
      }
      wp[i] = w / (double) (w + l);
      wpc[i] = w + l;
    }
    for (int i = 0; i < n; ++i) {
      owp[i] = 0.0;
      owpc[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (mat[i][j] != '.') {
          owp[i] += (wp[j] * wpc[j] - (mat[i][j] == '0')) / (wpc[j] - 1);
          ++owpc[i];
        }
      }
      owp[i] /= owpc[i];
    }
    for (int i = 0; i < n; ++i) {
      oowp[i] = 0.0;
      int cnt = 0;
      for (int j = 0; j < n; ++j) {
        if (mat[i][j] != '.') {
          oowp[i] += owp[j];
          ++cnt;
        }
      }
      oowp[i] /= cnt;
    }
    printf("Case #%d:\n", t);
    for (int i = 0; i < n; ++i) printf("%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
  return 0;
}

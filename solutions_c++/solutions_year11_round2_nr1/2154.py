#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

char line[100 + 1];

char t[100][100];
char w[100][100];
char p[100][100];
char cw[100];
char cp[100];

double wp[100];
double owp[100];
double oowp[100];

int main() {
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    // solve
    int n = 0;
    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s\n", line);
      cw[i] = 0;
      cp[i] = 0;
      for (int j = 0; j < n; ++j) {
        int k = (line[j] == '0') ? 0 : (line[j] == '1') ? 1 : -1;
        t[i][j] = k;
        if (k >= 0) p[i][cp[i]++] = j;
        if (k == 1) w[i][cw[i]++] = j;
      }
      wp[i] = (double)cw[i] / cp[i];
      owp[i] = 0.0;
      oowp[i] = 0.0;
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < cp[i]; ++j) {
        int k = p[i][j];
        owp[i] += (double)(cw[k] - t[k][i]) / (cp[k] - 1);
      }
      owp[i] /= cp[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < cp[i]; ++j) {
        int k = p[i][j];
        oowp[i] += owp[k];
      }
      oowp[i] /= cp[i];
    }
    // output
    printf("Case #%d:\n", Ti);
    for (int i = 0; i < n; ++i) {
      //fprintf(stderr, "i = %d, wp = %g, owp = %g, oowp = %g\n", i, wp[i], owp[i], oowp[i]);
      printf("%g\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
  }
  return 0;
}

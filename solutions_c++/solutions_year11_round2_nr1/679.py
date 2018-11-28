/* Google Code Jam 2011, Round 1B, Problem A: "RPI". */
/* Sat. May. 21, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Sat. May. 21, 2011.
#include <cstdio>

char game[128][128];
int ng[128], nw[128];
double wp[128], owp[128], oowp[128];

int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int n;
    scanf ("%d", &n);
    for (int i = 0; i < n; ++ i) scanf ("%127s", game[i]);
    for (int i = 0; i < n; ++ i) {
      ng[i] = nw[i] = 0;
      for (int j = 0; j < n; ++ j) {
        if (game[i][j] != '.') ++ ng[i];
        if (game[i][j] == '1') ++ nw[i];
      }
      wp[i] = nw[i] / (double) ng[i];
    }
    for (int i = 0; i < n; ++ i) {
      double v = 0;
      for (int j = 0; j < n; ++ j) {
        if (game[i][j] != '.') v += (nw[j] - (game[j][i] - '0')) / (double) (ng[j] - 1);
      }
      owp[i] = v / ng[i];
    }
    for (int i = 0; i < n; ++ i) {
      double v = 0;
      for (int j = 0; j < n; ++ j) {
        if (game[i][j] != '.') v += owp[j];
      }
      oowp[i] = v / ng[i];
      //printf ("%f\t%f\t%f\n", wp[i], owp[i], oowp[i]);
    }
    printf ("Case #%d:\n", ca);
    for (int i = 0; i < n; ++ i) {
      printf ("%.12f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
  }
  return 0;
}

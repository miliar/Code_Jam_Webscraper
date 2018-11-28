#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

typedef pair <double, double> pnt;
#define x first
#define y second

typedef long long ll;

ll s[610][610][3], a[610][610][3];

int main (void) {
  int tn;
  scanf ("%d", &tn);
  for (int tt = 1; tt <= tn; tt++) {
    int h, w, d;
    scanf ("%d%d%d", &h, &w, &d);
    for (int i = 0; i < h; i++) {
      char s[1000];
      scanf ("%s", s);
      for (int j = 0; j < w; j++) {
        a[i][j][2] = s[j] - '0';
        a[i][j][0] = i * a[i][j][2];
        a[i][j][1] = j * a[i][j][2];
      }
    }
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        for (int t = 0; t < 3; t++) {
          s[i + 1][j + 1][t] = s[i + 1][j][t] + s[i][j + 1][t] - s[i][j][t] + a[i][j][t];
        }
      }
    }
    int res = 0;
    for (int k = 3; k <= h && k <= w; k++) {
      for (int i = k; i <= h; i++) {
        for (int j = k; j <= w; j++) {
          int tmp[3] = {0};
          for (int t = 0; t < 3; t++) {
            tmp[t] = s[i][j][t] - s[i - k][j][t] - s[i][j - k][t] + s[i - k][j - k][t];
            tmp[t] -= a[i - 1][j - 1][t];
            tmp[t] -= a[i - k][j - 1][t];
            tmp[t] -= a[i - 1][j - k][t];
            tmp[t] -= a[i - k][j - k][t];
          }
          if (tmp[0] * 2 == tmp[2] * (i - 1 + i - k) && tmp[1] * 2 == tmp[2] * (j - 1 + j - k)) {
            res = k;
          }
        }
      }
    }
    printf ("Case #%d: ", tt);
    fprintf (stderr, "%d : %d\n", tt, res);
    if (res) {
      printf ("%d\n", res);
    } else {
      printf ("IMPOSSIBLE\n");
    }
                                
  }
  return 0;
}
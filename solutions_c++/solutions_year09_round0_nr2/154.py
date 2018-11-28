/* Google Code Jam 2009, Qualification Round, Problem B: "Watersheds". */
/* Wed. Sept. 2, 2009, By: Samuel Tien-Chieh Huang. */
// Last update: Wed. Sept. 2, 2009.
#include <cstdio>
#include <vector>
using namespace std;
#define INF 0x3FFFFFFF

int dy [] = {-1, 0, 0, 1};
int dx [] = {0, -1, 1, 0};
int inv [] = {3, 2, 1, 0};

int elev [120][120];
int con [120][120];
char res [120][120];

int nc, ca, h, w;
char cur_v;

void paint (int y, int x) {
  if ((y < 0) || (x < 0) || (y >= h) || (x >= w)) return;
  if (res [y][x] != 0) return;
  res [y][x] = cur_v;
  for (int d = 0; d < 4; d ++) {
    if (((con [y][x] >> d) & 1) != 0) {
      paint (y + dy [d], x + dx [d]);
    }
  }
}

int main (void) {
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    printf ("Case #%d:\n", ca);
    scanf ("%d%d", &h, &w);
    for (int i = 0; i < h; i ++) {
      for (int j = 0; j < w; j ++) {
        scanf ("%d", &elev [i][j]);
        con [i][j] = 0;
        res [i][j] = 0;
      }
    }
    for (int i = 0; i < h; i ++) {
      for (int j = 0; j < w; j ++) {
        int d_min = -1, val_min = INF, y_min = -1, x_min = -1;
        for (int d = 0; d < 4; d ++) {
          int y = i + dy [d], x = j + dx [d];
          if ((y < 0) || (x < 0) || (y >= h) || (x >= w)) continue;
          if (elev [i][j] <= elev [y][x]) continue;
          if (val_min > elev [y][x]) {
            val_min = elev [y][x];
            d_min = d;
            y_min = y;
            x_min = x;
          }
        }
        if (val_min < INF) {
          con [i][j] |= 1 << d_min;
          con [y_min][x_min] |= 1 << inv [d_min];
        }
      }
    }
    cur_v = 'a';
    for (int i = 0; i < h; i ++) {
      for (int j = 0; j < w; j ++) {
        if (res [i][j] != 0) continue;
        paint (i, j);
        cur_v ++;
      }
    }
    for (int i = 0; i < h; i ++) {
      for (int j = 0; j < w; j ++) {
        printf ("%c%c", res [i][j], (j < w - 1) ? ' ' : '\n');
      }
    }
  }
  return 0;
}

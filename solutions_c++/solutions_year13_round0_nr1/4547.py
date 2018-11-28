#include <cstdio>

char b[16][16];

int main () {
  int tn;
  scanf ("%d", &tn);
  for (int t = 1; t <= tn; t++) {
    for (int i = 0; i < 4; i++)
      scanf ("%s", b[i]);
    int xwon = 0, owon = 0, dots = 0;
    for (int i = 0; i < 4; i++) {
      int curx = 0, curo = 0;
      for (int j = 0; j < 4; j++) {
	if (b[i][j] == 'X' || b[i][j] == 'T') ++curx;
	if (b[i][j] == 'O' || b[i][j] == 'T') ++curo;
	if (b[i][j] == '.') ++dots;
      }
      if (curx == 4) xwon = 1;
      if (curo == 4) owon = 1;
    }
    for (int j = 0; j < 4; j++) {
      int curx = 0, curo = 0;
      for (int i = 0; i < 4; i++) {
	if (b[i][j] == 'X' || b[i][j] == 'T') ++curx;
	if (b[i][j] == 'O' || b[i][j] == 'T') ++curo;
      }
      if (curx == 4) xwon = 1;
      if (curo == 4) owon = 1;
    }
    int curx = 0, curo = 0;
    for (int j = 0; j < 4; j++) {
      if (b[j][3 - j] == 'X' || b[j][3 - j] == 'T') ++curx;
      if (b[j][3 - j] == 'O' || b[j][3 - j] == 'T') ++curo;
    }
    if (curx == 4) xwon = 1;
    if (curo == 4) owon = 1;
    curx = 0, curo = 0;
    for (int j = 0; j < 4; j++) {
      if (b[j][j] == 'X' || b[j][j] == 'T') ++curx;
      if (b[j][j] == 'O' || b[j][j] == 'T') ++curo;
    }
    if (curx == 4) xwon = 1;
    if (curo == 4) owon = 1;
    printf ("Case #%d: ", t);
    if (xwon) printf ("X won"); else
    if (owon) printf ("O won"); else
    if (!dots) printf ("Draw"); else
      printf ("Game has not completed");
    puts ("");
  }
  return 0;
}

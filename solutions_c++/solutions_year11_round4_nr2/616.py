#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define eps 1e-9

int R, C;
long long D;

long long mass[512][512];

bool ok(int r, int c, int k) {
  if (r+k > R || c+k > C)
    return false;

  double cm = ((double)k-1)/2;
  double x = 0.0, y = 0.0;
  for (int i = 0; i < k; ++i)
    for (int j = 0; j < k; ++j) {
      if ((i == 0 && j == 0) ||
	  (i == 0 && j == k-1) ||
	  (i == k-1 && j == 0) || 
	  (i == k-1 && j == k-1))
	continue;
      x += (i-cm) * (D+mass[r+i][c+j]);
      y += (j-cm) * (D+mass[r+i][c+j]);
    }

  // printf("x: %lf y: %lf %d\n", x, y, k);

  return fabs(x) <= eps && fabs(y) <= eps;
}

int main() {
  int nt, cases = 1;
  scanf(" %d", &nt);
  while (nt--) {
    scanf(" %d%d%lld", &R, &C, &D);
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j) {
	char c;
	scanf(" %c", &c);
	mass[i][j] = c-'0';
      }
    int res = 0;
    // printf("%d %d %lld\n", R, C, D);
    for (int k = 3; k <= min(R,C); ++k)
      for (int i = 0; i < R; ++i)
	for (int j = 0; j < C; ++j)
	  if (ok(i, j, k))
	    res = k;
    printf("Case #%d: ", cases++);
    if (res >= 3)
      printf("%d\n", res);
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}

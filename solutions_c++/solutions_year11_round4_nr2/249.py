#define _ABS(x) ((x)>0?(x):(-(x)))
#define EPS .00000001

#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <vector>

using namespace std;

int T;
int R,C,D;

int grid[501][501];
double mgrid[501][501][2];
int sgrid[501][501];
char line[502];

int getsum(int x, int y, int z, int t) {
  int ans = sgrid[z][t];
  if (x > 0)
    ans -= sgrid[x-1][t];
  if (y > 0)
    ans -= sgrid[z][y-1];
  if (x > 0 && y > 0)
    ans += sgrid[x-1][y-1];
  ans -= grid[z][t]+grid[x][y]+grid[x][t]+grid[z][y];
  return ans;
}

double getmx(int x, int y, int z, int t) {
  double ans = mgrid[z][t][0];
  if (x > 0)
    ans -= mgrid[x-1][t][0];
  if (y > 0)
    ans -= mgrid[z][y-1][0];
  if (x > 0 && y > 0)
    ans += mgrid[x-1][y-1][0];
  ans -= (z+.5)*grid[z][t]+(x+.5)*grid[x][y]+(x+.5)*grid[x][t]+(z+.5)*grid[z][y];
  return ans;
}

double getmy(int x, int y, int z, int t) {
  double ans = mgrid[z][t][1];
  if (x > 0)
    ans -= mgrid[x-1][t][1];
  if (y > 0)
    ans -= mgrid[z][y-1][1];
  if (x > 0 && y > 0)
    ans += mgrid[x-1][y-1][1];
  ans -= (t+.5)*grid[z][t]+(y+.5)*grid[x][y]+(t+.5)*grid[x][t]+(y+.5)*grid[z][y];
  return ans;
}

int solve(int W) {
  if (W < 3) return -1;
  int cnt = W*W - 4;
  for (int ri = W-1; ri < C; ++ri)
    for (int lj = W-1; lj < R;++lj) {
      double x = getmx(ri-W+1,lj-W+1,ri,lj);
      double y = getmy(ri-W+1,lj-W+1,ri,lj);
      double s = getsum(ri-W+1,lj-W+1,ri,lj);
      double cx = (2*ri + 2 - W)*1.0/2;
      double cy = (2*lj + 2 - W)*1.0/2;
      if (_ABS(s * cx - x) < EPS && _ABS(s * cy - y) < EPS) {
	//	printf("%d %d\n", ri, lj);
	return 1;
      }
    }
  return 0;
}

int main() {
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    memset(grid, 0, sizeof grid);
    memset(mgrid, 0, sizeof mgrid);
    memset(sgrid, 0, sizeof sgrid);
    scanf("%d %d %d", &R, &C, &D);
    for (int i=0;i<R;++i) {
      scanf("%s", line);
      for (int j=0;j<C;++j)
	grid[i][j] = line[j]-'0' + D;
    }
    sgrid[0][0] = grid[0][0];
    for (int i=0;i<C;++i)
      sgrid[0][i] = sgrid[0][i-1]+grid[0][i];
    for (int i=1;i<R;++i) {
      sgrid[i][0] = sgrid[i-1][0] + grid[i][0];
      for (int j=1;j<C;++j)
	sgrid[i][j] = sgrid[i-1][j]+sgrid[i][j-1] + grid[i][j] - sgrid[i-1][j-1];
    }
    mgrid[0][0][0] = .5*grid[0][0];
    mgrid[0][0][1] = .5*grid[0][0];
    for (int i=0;i<C;++i) {
      mgrid[0][i][0] = mgrid[0][i-1][0] + .5*grid[0][i];
      mgrid[0][i][1] = mgrid[0][i-1][1] + (i+.5)*grid[0][i];
    }
    for (int i=1;i<R;++i) {
      mgrid[i][0][0] = mgrid[i-1][0][0] + (i+.5)*grid[i][0];
      mgrid[i][0][1] = mgrid[i-1][0][1] + .5*grid[i][0];
      for (int j=1;j<C;++j) {
	mgrid[i][j][0] = mgrid[i-1][j][0] + mgrid[i][j-1][0] + (i+.5)*grid[i][j]
	  - mgrid[i-1][j-1][0];
	mgrid[i][j][1] = mgrid[i-1][j][1] + mgrid[i][j-1][1] + (j+.5)*grid[i][j]
	  - mgrid[i-1][j-1][1];
      }
    }
    int W = R;
    if (C<W)
      W = C;
    while (W >= 3 && !solve(W)) {
      --W;
    }
    /*    for (int i=0;i<R;++i) {
      for (int j=0;j<C;++j) 
	printf("%d ", grid[i][j]);
      printf("\n");
    }
    printf("\n");
    for (int i=0;i<R;++i) {
      for (int j=0;j<C;++j) 
	printf("%d ", sgrid[i][j]);
      printf("\n");
    }
    for (int i=0;i<R;++i) {
      for (int j=0;j<C;++j) 
	printf("(%lf,%lf) ", mgrid[i][j][0], mgrid[i][j][1]);
      printf("\n");
    }
    printf("%d\n", getsum(1,1,5,5));*/
    if (W < 3) {
      printf("Case #%d: IMPOSSIBLE\n", TT);
      continue;
    }
    printf("Case #%d: %d\n", TT, W);
  }
  return 0;
}

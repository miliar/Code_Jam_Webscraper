
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool appx_eq(double a, double b) {
  return abs(a-b) < 1e-10;
}

long double area(vector<long double> mat[512], int x, int y, int k) {
  // ULeft
  --k; // Hehe.
  return mat[y-1][x] + mat[y][x-1] - mat[y][x]
    // BLeft
    - mat[y+k][x] + mat[y+k-1][x] - mat[y+k-1][x-1]
    // URight
    - mat[y][x+k] + mat[y][x+k-1] - mat[y-1][x+k-1]
    // BRight
    + mat[y+k-1][x+k] + mat[y+k][x+k-1] - mat[y+k-1][x+k-1];
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  int grid[512][512];
  vector<long double> total_mat[512];
  vector<long double> sumx_mat[512];
  vector<long double> sumy_mat[512];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    memset(grid, 0, sizeof(grid));
    int r;
    int c;
    int d;
    scanf("%d %d %d", &r, &c, &d);
    for (int i = 0; i <= r; ++i) {
      total_mat[i].clear();
      sumx_mat[i].clear();
      sumy_mat[i].clear();
      total_mat[i].resize(c+5);
      sumx_mat[i].resize(c+5);
      sumy_mat[i].resize(c+5);
    }
    getchar();
    for (int i = 1; i <= r; ++i) {
      for (int j = 1; j <= c; ++j) {
        grid[i][j] = getchar() - '0';
      }
      getchar();
    }
    for (int i = 1; i <= r; ++i) {
      for (int j = 1; j <= c; ++j) {
        long double w = d + grid[i][j];
        total_mat[i][j] = w + total_mat[i][j-1] + total_mat[i-1][j] -
          total_mat[i-1][j-1];
        sumx_mat[i][j] = w*(j + 0.5) + sumx_mat[i][j-1] + sumx_mat[i-1][j] -
          sumx_mat[i-1][j-1];
        sumy_mat[i][j] = w*(i + 0.5) + sumy_mat[i][j-1] + sumy_mat[i-1][j] -
          sumy_mat[i-1][j-1];
      }
    }
    int best = 0;
    for (int k = min(r, c); k >= 3; --k) {
      // UL point (center can be inbetween cells -.-)
      for (int uly = 1; uly+k <= r+1; ++uly) {
        for (int ulx = 1; ulx+k <= c+1; ++ulx) {
          long double total = area(total_mat, ulx, uly, k);
          long double sumx = area(sumx_mat, ulx, uly, k);
          long double sumy = area(sumy_mat, ulx, uly, k);
          if (appx_eq(ulx+(k/(long double)2), sumx/(long double)total) &&
              appx_eq(uly+(k/(long double)2), sumy/(long double)total)) {
            best = k;
            goto out;
          }
        }
      }
    }
  out:
    printf("Case #%d: ", ctr+1);
    if (best == 0) {
      printf("IMPOSSIBLE\n");
    } else printf("%d\n", best);
  }
  
  return 0;
}

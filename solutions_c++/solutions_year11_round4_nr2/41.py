#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int XD[501][501];
int YD[501][501];
int D[501][501];
int d[500][500];

int main(void)
{
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    int R, C, _D; cin >> R >> C >> _D;
    for (int r = 0; r < R; r++) {
      string s; cin >> s;
      for (int c = 0; c < C; c++)
	d[r][c] = s[c]-'0';
    }
    int ans = 0;
    
    for (int r = 1; r <= R; r++) {
      int row_XD = 0, row_YD = 0, row_D = 0;
      for (int c = 1; c <= C; c++) {
	row_XD += (r-1) * d[r-1][c-1];
	row_YD += (c-1) * d[r-1][c-1];
	row_D += d[r-1][c-1];
	XD[r][c] = XD[r-1][c] + row_XD;
	YD[r][c] = YD[r-1][c] + row_YD;
	D[r][c] = D[r-1][c] + row_D;	
      }
    }

    for (int r = 0; r < R; r++)
      for (int c = 0; c < C; c++)
	for (int k = 3; (r+k <= R && c+k <= C); k++) {
	  int blade_XD = XD[r+k][c+k] - XD[r+k][c] - XD[r][c+k] + XD[r][c]
	    - (r+k-1)*d[r+k-1][c+k-1] - (r+k-1)*d[r+k-1][c]
	    - r*d[r][c+k-1] - r*d[r][c];
	  int blade_YD = YD[r+k][c+k] - YD[r+k][c] - YD[r][c+k] + YD[r][c]
	    - (c+k-1)*d[r+k-1][c+k-1] - c*d[r+k-1][c]
	    - (c+k-1)*d[r][c+k-1] - c*d[r][c];
	  int blade_D = D[r+k][c+k] - D[r+k][c] - D[r][c+k] + D[r][c]
	    - d[r+k-1][c+k-1] - d[r+k-1][c] - d[r][c+k-1] - d[r][c];
	  if (2*blade_XD == (2*r+k-1)*blade_D &&
	      2*blade_YD == (2*c+k-1)*blade_D)
	    ans >?= k;
	}
    
    if (ans > 0)
      printf("Case #%d: %d\n", test, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", test);
  }
}

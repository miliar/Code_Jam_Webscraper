#include <iostream>
#include <algorithm>
#include <complex>
#include <cmath>
using namespace std;
typedef complex<double> P;
int H, W, D, M[500][500];
const double eps = 1e-8;
bool equals(double a, double b) {
  return fabs(a-b) < eps;
}
bool calc(P c, int x, int y, int s) {
  P sum(0,0);
  for(int i = 0; i < s; ++i) {
    for(int j = 0; j < s; ++j) {
      if(i == 0 && j == 0) continue;
      if(i == 0 && j+1 == s) continue;
      if(i+1 == s && j == 0) continue;
      if(i+1 == s && j+1 == s) continue;
      P p = (P(x+j+0.5, y+i+0.5) - c) * (double)(M[y+i][x+j]+D);
      sum = sum + p;
    }
  }
  return equals(sum.real(), 0.0) && equals(sum.imag(), 0.0);
}

int solve() {
  for(int s = min(H, W); s >= 3; --s) {
    for(int i = 0; i+s-1 < H; ++i) {
      for(int j = 0; j+s-1 < W; ++j) {
	if(calc(P(j+s/2.0, i+s/2.0), j, i, s)) return s;
      }
    }
  }
  return 0;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cin >> H >> W >> D;
    for(int i = 0; i < H; ++i) {
      for(int j = 0; j < W; ++j) {
	char c;
	cin >> c;
	M[i][j] = c - '0';
      }
    }
    int ans = solve();
    cout << "Case #" << tc << ": ";
    if(ans == 0) cout << "IMPOSSIBLE" << endl;
    else         cout << ans << endl;
  }
  return 0;
}

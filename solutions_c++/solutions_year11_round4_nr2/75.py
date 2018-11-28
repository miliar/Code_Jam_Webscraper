#include <iostream>
#include <vector>
using namespace std;

long long w[550][550], xw[550][550], yw[550][550];
long long g[550][550], xg[550][550], yg[550][550];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int R, C, D; cin >> R >> C >> D;
    vector<string> grid(R);
    for (int i = 0; i < R; i++)
      cin >> grid[i];

    memset(w, 0, sizeof(w));
    memset(xw, 0, sizeof(xw));
    memset(yw, 0, sizeof(yw));
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        g[i+1][j+1] = D+grid[i][j]-'0';
        xg[i+1][j+1] = (D+grid[i][j]-'0')*(i+1);
        yg[i+1][j+1] = (D+grid[i][j]-'0')*(j+1);
        w[i+1][j+1] = w[i+1][j]+w[i][j+1]-w[i][j]+(D+grid[i][j]-'0');
        xw[i+1][j+1] = xw[i+1][j]+xw[i][j+1]-xw[i][j]+(D+grid[i][j]-'0')*(i+1);
        yw[i+1][j+1] = yw[i+1][j]+yw[i][j+1]-yw[i][j]+(D+grid[i][j]-'0')*(j+1);
      }

    int res = 0;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        for (int k = 3; i+k <= R && j+k <= C; k++) {
          long long sw = w[i+k][j+k]-w[i+k][j]-w[i][j+k]+w[i][j];
          long long sxw = 2*(xw[i+k][j+k]-xw[i+k][j]-xw[i][j+k]+xw[i][j]);
          long long syw = 2*(yw[i+k][j+k]-yw[i+k][j]-yw[i][j+k]+yw[i][j]);

          sw -= g[i+1][j+1]+g[i+1][j+k]+g[i+k][j+1]+g[i+k][j+k];
          sxw -= 2*(xg[i+1][j+1]+xg[i+1][j+k]+xg[i+k][j+1]+xg[i+k][j+k]);
          syw -= 2*(yg[i+1][j+1]+yg[i+1][j+k]+yg[i+k][j+1]+yg[i+k][j+k]);

          long long x = 2*(i+1)+k-1, y = 2*(j+1)+k-1;
          if (sxw == x*sw && syw == y*sw)
            res = max(res, k);
          // cout << i << " " << j << " " << k << " " << sw << " " << sxw << " " << syw << " " << x << " " << y << endl;
        }
      }
    }
    if (res == 0) cout << "Case #" << c << ": IMPOSSIBLE" << endl;
    else cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}

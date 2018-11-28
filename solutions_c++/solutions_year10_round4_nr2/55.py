#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int M[1024];
int cost[10][512];
int f[11][1024][11];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int P;
    cin >> P;
    int n = 1 << P;
    for (int i = 0; i < n; i++) {
      cin >> M[i];
      M[i] = P - M[i];
    }
    for (int i = 0; i < P; i++) {
      for (int j = 0; j < (1 << (P - i - 1)); j++) {
        cin >> cost[i][j];
      }
    }
    memset(f, -1, sizeof(f));
    for (int i = 0; i < n; i++) {
      f[0][i][M[i]] = 0;
    }
    for (int i = 1; i <= P; i++) {
      for (int j = 0; j < (n >> i); j++) {
        int l = j << 1;
        int r = l + 1;
        for (int x = 0; x <= P; x++) {
          if (f[i - 1][l][x] == -1) {
            continue;
          }
          for (int y = 0; y <= P; y++) {
            if (f[i - 1][r][y] == -1) {
              continue;
            }
            int s = f[i - 1][l][x] + f[i - 1][r][y];
            int c = max(x, y);
            if (f[i][j][c] == -1 || s < f[i][j][c]) {
              f[i][j][c] = s;
            }
            if (c > 0) {
              s += cost[i - 1][j];
              c--;
              if (f[i][j][c] == -1 || s < f[i][j][c]) {
                f[i][j][c] = s;
              }
            }
          }
        }
      }
    }
    cout << "Case #" << t << ": " << f[P][0][0] << endl;
  }
}

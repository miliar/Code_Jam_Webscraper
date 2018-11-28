#include <iostream>

using namespace std;

const int maxH = 100 + 10;
const int maxW = 100 + 10;
const int MOD = 10007;

int N, H, W, R;
int map[maxH][maxW];
int f[maxH][maxW];

int main() {
  int r, c;
  cin >> N;
  for (int e = 1; e <= N; ++e) {
    cout << "Case #" << e << ": ";
    cin >> H >> W >> R;

    memset(map, 0, sizeof(map));
    for (int i = 0; i < R; ++i) {
      cin >> r >> c;
      map[r][c] = 1;
    }
    for (int i = 1; i <= H; ++i) {
      for (int j = 1; j <= W; ++j) {
        if (i == 1 && j == 1) {
          f[i][j] = 1;
        } else {
          f[i][j] = 0;
        }
        if (map[i][j]) {
          continue;
        }
        if (i > 1 && j > 2) f[i][j] += f[i - 1][j - 2];
        if (i > 2 && j > 1) f[i][j] += f[i - 2][j - 1];
        f[i][j] %= MOD;
      }
    }
    cout << f[H][W] << endl;
  }
  return 0;
}


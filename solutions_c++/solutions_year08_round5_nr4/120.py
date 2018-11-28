#include <iostream>
using namespace std;

int main() {
  const int MOD = 10007;
  int cases;
  cin >> cases;
  for (int caseno=1; caseno<=cases; caseno++) {
    
    int H, W, R;
    cin >> H >> W >> R;
    int rock[101][101], dp[101][101];
    memset(rock, 0, sizeof(rock));
    memset(dp, 0, sizeof(rock));
    for (int i=0; i<R; i++) {
      int r, c;
      cin >> r >> c;
      rock[r-1][c-1] = 1;
    }

    dp[0][0] = 1;
    int dx[] = {2, 1}, dy[] = {1, 2};
    for (int y=0; y<H; y++) {
      for (int x=0; x<W; x++) {
        for (int dir = 0; dir < 2; dir++) {
          int nx = x + dx[dir], ny = y + dy[dir];
          if (nx < W && ny < H && rock[ny][nx] == 0) {
            dp[ny][nx] = (dp[ny][nx] + dp[y][x]) % MOD;
          }
        }
      }
    }

    int res = dp[H-1][W-1];
    cout << "Case #" << caseno << ": " << res << endl;
  }
}

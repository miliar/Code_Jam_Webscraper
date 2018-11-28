#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define ALL(x) (x).begin(), (x).end()
#define MP make_pair

using namespace std;

int H, W;
int grid[100][100];
int color[100][100];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

inline int Valid(int r, int c) { return 0 <= r && r < H && 0 <= c && c < W; }

void Dfs(int r, int c, int col) {
  //cout << r << " " << c << " " << (char)('a' + col) << endl;
  color[r][c] = col;

  // go
  {
    int next_r = -1, next_c = -1, next_alt = grid[r][c];
    REP(i, 4) {
      int nr = r + dr[i], nc = c + dc[i];
      if (Valid(nr, nc) && next_alt > grid[nr][nc]) {
        next_r = nr;
        next_c = nc;
        next_alt = grid[nr][nc];
      }
    }
    if (next_r != -1 && color[next_r][next_c] == -1) Dfs(next_r, next_c, col);
  }
  // come
  {
    REP(i, 4) {
      int nr = r + dr[i], nc = c + dc[i];
      if (!Valid(nr, nc)) continue;
      int next_r = -1, next_c = -1, next_alt = grid[nr][nc];
      REP(j, 4) {
        int mr = nr + dr[j], mc = nc + dc[j];
        if (Valid(mr, mc) && next_alt > grid[mr][mc]) {
          next_r = mr;
          next_c = mc;
          next_alt = grid[mr][mc];
        }
      }
      if (next_r == r && next_c == c && color[nr][nc] == -1) Dfs(nr, nc, col);
    }
  }
}

int main() {
  int T;
  cin >> T;
  REP(t, T) {
    cin >> H >> W;
    REP(i, H) REP(j, W) cin >> grid[i][j];
    memset(color, -1, sizeof(color));
    int current_color = 0;
    REP(i, H) REP(j, W) if (color[i][j] == -1) Dfs(i, j, current_color++);

    cout << "Case #" << (t + 1) << ":" << endl;
    REP(i, H) {
      REP(j, W) {
        if (j) cout << " ";
        cout << (char)('a' + color[i][j]);
      }
      cout << endl;
    }
  }
  return 0;
}

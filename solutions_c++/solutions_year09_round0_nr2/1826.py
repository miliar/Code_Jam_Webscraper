#include <iostream>
#include <string>
#include <memory.h>

using namespace std;

struct pos {
  int x, y;
  pos(int _x = -1, int _y = -1) : x(_x), y(_y) { }
};

int a[100][100], h, w;
bool u[100][100];
pos Bres[100][100];
int col[100][100];

int dir[5][2] = { {0, 0}, {0, -1}, {-1, 0}, {1, 0}, {0, 1} };

inline bool good(int x, int y) {
  return (x >= 0 && y >= 0 && x < w && y < h);
}

pos dfs(pos v) {
  if (u[v.x][v.y]) return Bres[v.x][v.y];

  int go = 0;
  for (int i = 1; i < 5; i++) {
    int nx = v.x + dir[i][0], ny = v.y + dir[i][1];
    if (good(nx, ny) && a[nx][ny] < a[v.x + dir[go][0]][v.y + dir[go][1]])
      go = i;
  }

  pos res = v;
  if (go)
    res = dfs(pos(v.x + dir[go][0], v.y + dir[go][1]));

  Bres[v.x][v.y] = res;
  u[v.x][v.y] = true;
  return res;
}

int main() {
  int t; cin >> t;
  for (int _t = 0; _t < t; _t++) {
    cout << "Case #" << (_t + 1) << ":" << endl;
    cin >> h >> w;

    for (int j = 0; j < h; j++) for (int i = 0; i < w; i++)
      cin >> a[i][j];

    memset(u, 0, sizeof u);
    for (int j = 0; j < h; j++) for (int i = 0; i < w; i++)
      dfs(pos(i, j));

    memset(col, -1, sizeof col);
    int c_cnt = 0;
    for (int j = 0; j < h; j++) {
      for (int i = 0; i < w; i++) {
        pos b = Bres[i][j];
        int c = col[b.x][b.y];
        if (c == -1) {
          c = c_cnt++;
          col[b.x][b.y] = c;
        }
        cout << char('a' + c) << " ";
      }
      cout << endl;
    }
  }

  return 0;
}


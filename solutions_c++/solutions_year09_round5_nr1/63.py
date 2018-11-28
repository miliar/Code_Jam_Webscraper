#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int r, c;
char f[15][15];

struct pos {
  vector< pair<int, int> > b;
  int len;
  bool danger;

  pos() : len(0), danger(false) { }

  void upd() {
    sort(b.begin(), b.end());
  }

  void process();
};

bool operator < (const pos& a, const pos& b) {
  for (int i = 0; i < a.b.size(); i++)
    if (a.b[i] != b.b[i])
      return a.b[i] < b.b[i];
  return false;
}

bool operator == (const pos& a, const pos& b) {
  for (int i = 0; i < a.b.size(); i++)
    if (a.b[i] != b.b[i])
      return false;
  return true;
}

queue<pos> q;
set<pos> used;
pos final;

bool tmp[15][15];

int dir[4][2] = { {0, 1}, {0, -1}, {-1, 0}, {1, 0}};

inline bool good(int x, int y) {
  return (x >= 0 && x < r) && (y >= 0 && y < c);
}

int dfs_cnt;
bool u[15][15];

void dang_dfs(int x, int y) {
  if (u[x][y]) return;
  dfs_cnt++;
  u[x][y] = true;

  for (int j = 0; j < 4; j++) {
    int nx = x + dir[j][0], ny = y + dir[j][1];
    if (!good(nx, ny)) continue;
    if (tmp[nx][ny]) dang_dfs(nx, ny);
  }
}

bool is_danger(int size) {
  memset(u, 0, sizeof u);
  dfs_cnt = 0;

  for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (tmp[i][j]) {
    dang_dfs(i, j);
    return (dfs_cnt != size);
  }
}

void pos::process() {
  memset(tmp, 0, sizeof tmp);
  for (int i = 0; i < b.size(); i++)
    tmp[b[i].first][b[i].second] = true;

  for (int i = 0; i < b.size(); i++) {
    int x = b[i].first, y = b[i].second;
    for (int j = 0; j < 4; j++) {
      int nx = x + dir[j][0], ny = y + dir[j][1];

      int nnx = x - dir[j][0], nny = y - dir[j][1];

      if (!good(nx, ny) || !good(nnx, nny)) continue;
      if (f[nx][ny] == '#' || tmp[nx][ny]) continue;
      if (f[nnx][nny] == '#' || tmp[nnx][nny]) continue;

      tmp[nx][ny] = true;
      tmp[x][y] = false;
      bool d = is_danger(b.size());

      if (!(danger && d)) {
        pos npos;
        for (int _x = 0; _x < r; _x++)
          for (int _y = 0; _y < c; _y++) if (tmp[_x][_y])
            npos.b.push_back(make_pair(_x, _y));
        npos.len = len + 1;
        npos.upd();
        npos.danger = d;

        if (used.find(npos) == used.end()) {
          q.push(npos);
          used.insert(npos);
        }
      }

      tmp[nx][ny] = false;
      tmp[x][y] = true;
    }
  }

}

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cin >> r >> c;

    final.b.clear();
    pos start;

    for (int _r = 0; _r < r; _r++) for (int _c = 0; _c < c; _c++) {
      char ch = 0;
      while (ch != '.' && ch != '#' && ch != 'x' && ch != 'o' && ch != 'w') ch = cin.get();
      f[_r][_c] = ch;
      if (ch == 'o' || ch == 'w') start.b.push_back(make_pair(_r, _c));
      if (ch == 'x' || ch == 'w') final.b.push_back(make_pair(_r, _c));
    }

    used.clear();
    used.insert(start);
    q.push(start);


    cout << "Case #" << _tt << ": ";

    bool ok = false;
    while (!q.empty()) {
      pos top = q.front();
      q.pop();
      if (top == final) {
        cout << top.len << endl;
        ok = true;
        break;
      }
      top.process();
    }

    while (!q.empty()) q.pop();

    if (!ok) cout << -1 << endl;
    
  }

  return 0;
}

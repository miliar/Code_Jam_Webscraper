#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct state {
  int i, j, v, d;
  string s;
  state(int _i, int _j, int _v, int _d, string _s) : i(_i), j(_j), v(_v), d(_d), s(_s) { }
  bool operator<(const state& other) const {
    if (d != other.d) return d > other.d;
    return s > other.s;
  }
};

int dx[] = { 1, 0, -1, 0 }, dy[] = { 0, 1, 0, -1 };
int best[20][20][768];
string bests[20][20][768];
int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int W, Q; cin >> W >> Q;
    vector<string> grid(W);
    for (int i = 0; i < W; i++) cin >> grid[i];
    vector<int> qv(Q);
    for (int i = 0; i < Q; i++) cin >> qv[i];

    for (int i = 0; i < W; i++)
      for (int j = 0; j < W; j++)
        for (int k = 0; k < 768; k++) {
          best[i][j][k] = 1000000;
          bests[i][j][k] = "";
        }

    priority_queue<state> q;
    for (int i = 0; i < W; i++)
      for (int j = 0; j < W; j++) {
        if (grid[i][j] < '0' || grid[i][j] > '9') continue;
        state s(i, j, 256 + grid[i][j] - '0', 0, string(1, grid[i][j]));
        q.push(s);
        best[s.i][s.j][s.v] = s.d;
        bests[s.i][s.j][s.v] = s.s;
      }

    while (!q.empty()) {
      state cur = q.top(); q.pop();
      if (best[cur.i][cur.j][cur.v] != cur.d || bests[cur.i][cur.j][cur.v] != cur.s) continue;
      // cout << cur.i << " " << cur.j << " " << cur.v << endl;
      for (int i = 0; i < 4; i++) {
        int ni = cur.i + dx[i], nj = cur.j + dy[i];
        if (ni >= 0 && ni < W && nj >= 0 && nj < W) {
          if (grid[ni][nj] < '0' || grid[ni][nj] > '9') {
            state next(ni, nj, cur.v, cur.d + 1, cur.s+grid[ni][nj]);
            if (next.d < best[next.i][next.j][next.v] || (next.d == best[next.i][next.j][next.v] && next.s < bests[next.i][next.j][next.v])) {
              best[next.i][next.j][next.v] = next.d;
              bests[next.i][next.j][next.v] = next.s;
              q.push(next);
            }
          }
          else {
            int nv;
            if (cur.s[cur.s.size()-1] == '+') nv = cur.v + (grid[ni][nj] - '0');
            else nv = cur.v - (grid[ni][nj] - '0');
            if (nv < 0 || nv >= 768) continue;
            state next(ni, nj, nv, cur.d + 1, cur.s+grid[ni][nj]);
            if (next.d < best[next.i][next.j][next.v] || (next.d == best[next.i][next.j][next.v] && next.s < bests[next.i][next.j][next.v])) {
              best[next.i][next.j][next.v] = next.d;
              bests[next.i][next.j][next.v] = next.s;
              q.push(next);
            }
          }
        }
      }
    }

    cout << "Case #" << c << ":" << endl;
    for (int i = 0; i < Q; i++) {
      qv[i] += 256;
      int mind = 1000000; string minds;
      for (int j = 0; j < W; j++)
        for (int k = 0; k < W; k++)
          if (best[j][k][qv[i]] < mind || (best[j][k][qv[i]] == mind && bests[j][k][qv[i]] < minds)) {
            mind = best[j][k][qv[i]];
            minds = bests[j][k][qv[i]];
          }
      cout << minds << endl;
    }
  }
  return 0;
}

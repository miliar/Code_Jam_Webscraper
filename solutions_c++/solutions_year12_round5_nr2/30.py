#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <deque>
#include <map>


using namespace std;

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

class Dsu {
  vi ss, par;
  int cnt;
  public:
  Dsu(int n) : ss(n, 1), par(n), cnt(n) {
    for (int i = 0; i < n; i++) par[i] = i;
  }
  int get(int x) { return par[x] == x ? x : par[x] = get(par[x]); }
  int getCnt() const { return cnt; }
  void merge(int a, int b) {
    a = get(a); b = get(b);
    if (a == b) return;
    cnt--;
    if (ss[a] > ss[b]) swap(a, b);
    par[a] = b;
    ss[b] += ss[a];
  }
};

int s;
int wh;

const int dx[] = { 1, -1, 0, 0, 1, -1 };
const int dy[] = { 0, 0, 1, -1, 1, -1 };

vvi border;

void dfsBorder(int x, int y) {
  deque<pii> q;
  q.pb(mp(x, y));
  while (!q.empty()) {
    int x = q.front().first, y = q.front().second;
    q.pop_front();

    if (x < 0 || y < 0 || x >= wh || y >= wh) continue;
    if (border[y][x]) continue;
    border[y][x] = -1;
    for (int d = 0; d < 6; d++) {
      int nx = x + dx[d], ny = y + dy[d];
      if (nx < 0 || ny < 0 || nx >= wh || ny >= wh) continue;
      if (border[ny][nx]) continue;
      q.pb(mp(x + dx[d], y + dy[d]));
    }
  }
}
vector<pii> bpts;
void initBorder() {
  border = vvi(wh, vi(wh, false));
  for (int i = 0; i < s; i++) {
    int v1 = (i == 0 || i == s - 1) ? 1 : 2, v2 = (v1 == 2) ? 3 : 1;
    border[i][0] = v1;
    border[i][s - 1 + i] = v2;
  }
  for (int i = 1; i < s; i++) {
    int v1 = (i == s - 1) ? 1 : 4, v2 = (v1 == 4) ? 5 : 1;
    border[s + i - 1][i] = v1;
    border[s + i - 1][wh - 1] = v2;
  }
  for (int i = 1; i + 1 < s; i++) {
    border[0][i] = 6;
    border[wh - 1][s + i - 1] = 7;
  }
  dfsBorder(wh - 1, 0);
  dfsBorder(0, wh - 1);

  bpts.clear();
  for (int y = 0; y < wh; y++)
  for (int x = 0; x < wh; x++)
    if (border[y][x] > 0) bpts.pb(mp(x, y));
}

bool check(int x, int y) {
  if (x < 0 || y < 0 || x >= wh || y >= wh) return false;
  if (border[y][x] == -1) return false;
  return true;
}

void solve() {
  int m;
  scanf("%d%d", &s, &m);
  wh = 2 * s - 1;

  initBorder();
  eprintf("solve\n");

  vector<pii> pts(m);
  for (int i = 0; i < m; i++) {
    scanf("%d%d", &pts[i].first, &pts[i].second), pts[i].first--, pts[i].second--;
  }

  pii ans(m, 0);
  { // bridge/fork
    Dsu dsu(wh * wh);
    vvb board(wh, vb(wh, false));

    for (int step = 0; step < m; step++) {
      {
        int x = pts[step].first, y = pts[step].second;
        board[y][x] = true;
        for (int d = 0; d < 6; d++) {
          int nx = x + dx[d], ny = y + dy[d];
          if (!check(nx, ny)) continue;
          if (!board[ny][nx]) continue;
          dsu.merge(y * wh + x, ny * wh + nx);
        }
      }
      int res = 0;
      set<int> wast;
      map<int, set<int> > wase;

      for (int i = 0; i < sz(bpts); i++) {
        int x = bpts[i].first, y = bpts[i].second;
        if (!board[y][x]) continue;

        int cc = dsu.get(y * wh + x);
        if (border[y][x] == 1) {
          if (wast.count(cc)) res |= 1;
          wast.insert(cc);
        } else if (border[y][x] > 1) {
          wase[cc].insert(border[y][x]);
        }
      }
      for (map<int, set<int> >::iterator it = wase.begin(); it != wase.end(); it++)
        if (sz(it->second) >= 3) { res |= 2; break; }
      if (!res) continue;

      ans = min(ans, mp(step, res));
      break;
    }
  }
  { // Ring
    Dsu dsu(wh * wh);
    vvb board(wh, vb(wh, false));
    for (int i = 0; i < m; i++)
      board[pts[i].second][pts[i].first] = true;
    for (int y = 0; y < wh; y++)
    for (int x = 0; x < wh; x++) if (check(x, y) && !board[y][x]) {
      for (int d = 0; d < 6; d++) {
        int nx = x + dx[d], ny = y + dy[d];
        if (!check(nx, ny)) continue;
        if (board[ny][nx]) continue;
        dsu.merge(y * wh + x, ny * wh + nx);
      }
    }
    int badCnt =0;
    for (int y = 0; y < wh; y++)
    for (int x = 0; x < wh; x++)
      if (border[y][x] == -1) badCnt++;

    for (int step = m - 1; step >= 0; step--) {
      set<int> bs;
      for (int i = 0; i < sz(bpts); i++) {
        int x = bpts[i].first, y = bpts[i].second;
        if (board[y][x]) continue;
        bs.insert(dsu.get(y * wh + x));
      }
      int remCnt = dsu.getCnt() - sz(bs) - badCnt - (step + 1);
      assert(remCnt >= 0);
      if (remCnt > 0) {
        if (ans.first == step) ans.second |= 4;
        else if (ans.first > step) ans = mp(step, 4);
      }

      {
        int x = pts[step].first, y = pts[step].second;
        board[y][x] = false;
        for (int d = 0; d < 6; d++) {
          int nx = x + dx[d], ny = y + dy[d];
          if (!check(nx, ny)) continue;
          if (board[ny][nx]) continue;
          dsu.merge(y * wh + x, ny * wh + nx);
        }
      }
    }
  }

  int res = ans.second;
  if (!res) { printf("none\n"); return; }
  const char *ns[] = {"bridge","fork","ring"};
  bool fir = true;
  for (int i = 0; i < 3; i++) if (res & (1 << i)) {
    if (!fir) printf("-");
    fir = false;
    printf(ns[i]);
  }
  printf(" in move %d\n", ans.first + 1);
}

int main(int argc, char* argv[]) {
  {
    string fname = "std";
    if (argc >= 2) {
      fname = argv[1];
      if (fname.length() >= 3 && string(fname, fname.length() - 3) == ".in")
        fname = string(fname, 0, fname.length() - 3);
    }
    freopen((fname + ".in").c_str(), "r", stdin);
    freopen((fname + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  char buf[100];
  fgets(buf, sizeof buf, stdin);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}

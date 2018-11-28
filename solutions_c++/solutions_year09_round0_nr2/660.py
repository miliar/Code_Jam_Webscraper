#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int test = 0;

int n, m;
int board[101][101];
int flow[101][101];
int sol[101][101];

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

int check(int a, int b) {
  if (a < 1 || a > n) return 0;
  if (b < 1 || b > m) return 0;
  return 1;
}
void dfs(int x, int y, int mark) {
  if (!check(x, y)) return;
  if (sol[x][y]) return;
  sol[x][y] = mark;

  //uite la vecini
  for (int d = 0; d < 4; ++d) {
    int px = x + di[d], py = dj[d] + y;
    if (!check(px, py)) continue;
    if (abs(flow[px][py]+d) == 3) dfs(px, py, mark);
  }
}
void go() {
  cin >> n >> m;
  int i, j;
  for (i = 1; i <= n; ++i)
    for (j = 1; j <= m; ++j) cin >> board[i][j];
  vector<pair<int, int> > sinks;

  for (i = 1; i <= n; ++i) 
    for (j = 1; j <= m; ++j) {
      int best = board[i][j];
      flow[i][j] = 1000;
      for (int d = 0; d < 4; ++d) if (check(i + di[d], j + dj[d])) {
        int px = i + di[d], py = j + dj[d];
	if (board[px][py] >= best) continue;
	best = board[px][py]; flow[i][j] = d;
      }
      if (best == board[i][j]) sinks.push_back(make_pair(i, j));
    }
  memset(sol, 0, sizeof(sol));
  int k = 0;
  for (i = 0; i < sinks.size(); ++i) {
    ++k;
    dfs(sinks[i].first, sinks[i].second, k);
  }
  char letter = 'a';
  
  int used[33];
  memset(used, 0, sizeof(used));

  cout << "Case #" << ++test<<":";
  for (i = 1; i <= n; ++i) {
    cout << '\n';
    for (j = 1; j <= m; ++j) {
      if (!used[sol[i][j]]) {used[sol[i][j]] = letter - 'a' + 1; letter++;}
      cout << char(used[sol[i][j]] - 1 + 'a');
      if (j != m) cout << ' ';
    }
  }
  cout << '\n';
}
int main() {
  freopen("large-B.in", "r", stdin);
  freopen("large-B.out", "w", stdout);

  int t;
  cin >> t;
  while (t--) go();
  return 0;
}

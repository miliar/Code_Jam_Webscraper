#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int const INF = 123456;

int const max_n = 444;
int dist[max_n];
vector<int> neigh[max_n];

void bfs(int s)
{
  dist[s] = 0;
  queue<int> Q;
  Q.push(s);
  while (!Q.empty()) {
    int x = Q.front();
    Q.pop();
    for (vector<int>::iterator it = neigh[x].begin(); it != neigh[x].end(); it++) {
      int y = *it;
      if (dist[y] > dist[x] + 1) {
        dist[y] = dist[x] + 1;
        Q.push(y);
      }
    }
  }
}

int done[max_n][max_n][max_n];
bool mat[max_n][max_n];

int solve(int x, int p, int gp)
{
  if (done[x][p][gp] >= 0) return done[x][p][gp];
  if (x == 1) return 1;
  int res = 0;
  for (vector<int>::iterator it = neigh[x].begin(); it != neigh[x].end(); it++) {
    int y = *it;
    if (dist[y] == dist[x] - 1) {
      res = max(res, solve(y, x, p));
    }
  }
  for (vector<int>::iterator it = neigh[x].begin(); it != neigh[x].end(); it++) {
    int y = *it;
    if (mat[p][y] || mat[gp][y]) continue;
    res++;
  }
  done[x][p][gp] = res;
  return res;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int case_ = 1; case_ <= t; case_++) {
    int n, m;
    scanf("%d %d", &n, &m);
    memset(done, -1, sizeof done);
    memset(mat, 0, sizeof mat);
    for (int i = 0; i < max_n; i++) {
      neigh[i].clear();
      dist[i] = INF;
      mat[i][i] = true;
    }
    for (int i = 0; i < m; i++) {
      int x, y;
      scanf("%d,%d", &x, &y);
      assert(x < n);
      assert(y < n);
      neigh[x].push_back(y);
      neigh[y].push_back(x);
      mat[x][y] = mat[y][x] = true;
    }
    bfs(1);
    int len = dist[0];
    int res = solve(0, n, n) - len;
    printf("Case #%d: %d %d\n", case_, len-1, res);
    fflush(stdout);
  }
  return 0;
}

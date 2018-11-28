#include <iostream>
#include <string>
#include <cstring>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, (n))

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int m, n, a[200][200];
int r[20000];
char c, ans[200][200];

int inside(int x, int y) {
  return 0 <= x && x < m && 0 <= y && y < n;
}
int root(int x) {
  while (r[x] != x) 
    x = r[x];
  return x;
}

void merge(int x, int y) {
  int rx = root(x);
  int ry = root(y);

  if (rand() % 2) {
    r[x] = r[y] = r[rx] = ry;
  } else {
    r[x] = r[y] = r[ry] = rx;
  }
}

void dfs(int i, int j) {
  ans[i][j] = c;

  REP(d, 4) {
    int ii = i + dx[d];
    int jj = j + dy[d];
    if (inside(ii, jj) && ans[ii][jj] == 0 && root(ii * n + jj) == root(i * n + j)) {
      dfs(ii, jj);
    }
  }
}

void doit() {
  REP(i, m) REP(j, n) {
    r[i*n + j] = i * n + j;
  }

  REP(i, m) REP(j, n) {
    int best = a[i][j], mi, mj;
    REP(d, 4) {
      int ii = i + dx[d];
      int jj = j + dy[d];
      if (inside(ii, jj) && a[ii][jj] < best) {
	best = a[ii][jj];
	mi = ii;
	mj = jj;
      }
    }

    if (best < a[i][j]) {
      merge(i*n + j, mi*n + mj);
    }
  }


  c = 'a';
  REP(i, m) REP(j, n) 
    if (ans[i][j] == 0){
      dfs(i, j);
      c++;
    }
}

int main() {
  int N;
  cin >> N;
  REP(i, N) {
    cin >> m >> n;
    memset(ans, 0, sizeof ans);
    REP(j, m) REP(k, n) cin >> a[j][k];
    doit();
    cout << "Case #" << (i + 1) << ":" << endl;
    REP(j, m) REP(k, n) {
      cout << ans[j][k];
      if (k == n-1) cout << endl;
      else cout << ' ';
    }
  }
}

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

using namespace std;

const int maxn=110;

int n,m,tx[maxn*maxn],ty[maxn*maxn], cas, ret;
char g[maxn][maxn];
bool nx[maxn*maxn];
vector<int> e[maxn*maxn];

void addedge(int a, int b, int c, int d) {
  if (b & 1) 
    e[a * m + b].push_back(c * m + d);
  else
    e[c * m + d].push_back(a * m + b);
}

bool dfs(int u) {
  if (nx[u]) return 0;
  nx[u] = 1;
  int sz = e[u].size();
  rep(i, sz) {
    int v = e[u][i];
    int tmp = ty[v];
    ty[v] = u;
    tx[u] = v;
    if (tmp == -1 || dfs(tmp)) return 1;
    ty[v] = tmp;
  }
  return 0;
}

int main() {
  cin >> cas;
  rep(tt, cas) {
    cin >> n >> m;
    memset(g, 0, sizeof(g));
    rep(i, maxn * maxn) e[i].clear();
    rep(i, n) scanf(" %s", g[i]);
    ret = 0;
    rep(i, n) rep(j, m) {
      if (g[i][j] == 'x') continue;
      ret++;
      if (j == 0) continue;
      if (j - 1 >= 0 && g[i][j - 1] == '.') addedge(i, j, i, j - 1);
      if (i && g[i-1][j-1] == '.') addedge(i, j, i - 1, j - 1);
      if (i < n - 1 && g[i+1][j-1] == '.') addedge(i, j, i + 1, j - 1);
    }
    rep(i, maxn * maxn) ty[i] = tx[i] = -1;
    memset(nx, 0, sizeof(nx));
    rep(i, n) rep(j, m) if ((j & 1) && dfs(i * m + j)) {
      memset(nx, 0, sizeof(nx));
      ret--;
    }
    printf("Case #%d: %d\n", tt + 1, ret);
  }
}

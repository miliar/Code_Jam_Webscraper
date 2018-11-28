#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

vector<int> adj[40];
vector<int> par[40];
int lvl[40];
int vis[40];
int res;

void compute(int u, int curr) {
  
  if (!vis[u]++)
    ++curr;

  if (u != 1)
    for (int i = 0; i < adj[u].size(); ++i) {
      if (!vis[adj[u][i]]++)
	++curr;
    }

  if (u == 0)
    res = max(curr, res);

  for (int i = 0; i < par[u].size(); ++i)
    compute(par[u][i], curr);

  if (u != 1)
    for (int i = 0; i < adj[u].size(); ++i)
      if(!--vis[adj[u][i]])
	--curr;

  if (!--vis[u])
    --curr;
}

int main() {
  int nt, cases = 1;
  scanf(" %d", &nt);
  while (nt--) {
    int p, w;
    scanf(" %d%d", &p, &w);
    for (int i = 0; i < p; ++i) {
      lvl[i] = 0;
      adj[i].clear();
      par[i].clear();
    }

    for (int i = 0; i < w; ++i) {
      int x, y;
      scanf(" %d,%d", &x, &y);
      adj[x].push_back(y);
      adj[y].push_back(x);
    }

    queue<int> Q;
    Q.push(0);
    while (!Q.empty()) {
      int u = Q.front(); Q.pop();
      if (u == 1)
	break;
      for (int i = 0; i < adj[u].size(); ++i) {
	int v = adj[u][i];
	if (v !=  0 && (lvl[v] == 0 || lvl[u] + 1 == lvl[v])) {
	  if (lvl[v] == 0)
	    Q.push(v);
	  par[v].push_back(u);
	  lvl[v] = lvl[u] + 1;
	}
      }
    }

    res = 0;
    memset(vis, 0, sizeof(vis));
    compute(1, 0);

    printf("Case #%d: %d %d\n", cases++, lvl[1]-1, res-lvl[1]);
  }  
  return 0;
}

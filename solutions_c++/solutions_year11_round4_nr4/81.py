#include<cstdio>
#include<vector>

using namespace std;

struct edge {
  int u, v;
  edge(int a, int b)
    : u(a), v(b) { }
};
typedef vector<edge> vertex;
typedef vector<vertex> graph;

int P, W;
int best_c, best_t;
int visit[50], threaten[50];

void dfs(const graph& g, int u, int c)
{
  if(c > best_c)
    return;
  visit[u] = 1;
  for(int i=0; i<(int)g[u].size(); ++i)
    threaten[g[u][i].v]++;

  if(threaten[1] > 0) {
    int t = 0;
    for(int i=0; i<P; ++i)
      if(threaten[i] > 0 && visit[i] == 0)
	t++;
    if(best_c > c || (best_c == c && best_t < t)) {
      best_c = c;
      best_t = t;
    }
    for(int i=0; i<(int)g[u].size(); ++i)
      threaten[g[u][i].v]--;
    visit[u] = 0;
    return;
  }

  for(int i=0; i<(int)g[u].size(); ++i) {
    if(visit[g[u][i].v]) continue;
    dfs(g, g[u][i].v, c+1);
  }
  
  for(int i=0; i<(int)g[u].size(); ++i)
    threaten[g[u][i].v]--;
  visit[u] = 0;
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int CN=1; CN<=T; ++CN) {
    scanf("%d%d", &P, &W);

    graph G(P);
    for(int i=0; i<P; ++i)
      threaten[i] = visit[i] = 0;
    for(int i=0; i<W; ++i) {
      int a, b;
      scanf("%d,%d", &a, &b);
      G[a].push_back(edge(a, b));
      G[b].push_back(edge(b, a));
    }

    best_c = 10000;
    visit[0] = 1;
    dfs(G, 0, 0);

    printf("Case #%d: %d %d\n", CN, best_c, best_t);
  }

  return 0;
}

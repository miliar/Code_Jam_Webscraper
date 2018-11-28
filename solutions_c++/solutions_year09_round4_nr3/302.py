/* GCJ'09 Template v.2e-9
 * Per Austrin
 */
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;

int CASES;

void init() {
  scanf("%d", &CASES);
}


int pr[200][200];
int n, k;

bool below(int i, int j) {
  for (int a = 0; a < k; ++a)
    if (pr[i][a] >= pr[j][a]) return false;
  return true;
}

bool isect(int i, int j) { return !below(i, j) && !below(j, i); }

typedef int Flow;

struct flow_edge {
  int dest, back;// back is index of back-edge in graph[dest]
  Flow c, f; // capacity and flow
  Flow cost; //used by bellman ford
  Flow r() { return c - f; } // used by ford fulkerson
  flow_edge() {}
  flow_edge(int _dest, int _back, Flow _c, Flow _f = 0
	    /*, Flow _cost = 0*/)
    : dest(_dest), back(_back), c(_c), f(_f)/*, cost(_cost)*/ { }
};

typedef vector<flow_edge> adj_list;
typedef adj_list::iterator adj_iter;

void flow_add_edge(adj_list *g, int s, int t, // add s -> t
		   Flow c, Flow back_c = 0/*, Flow cost = 0*/) {
  g[s].push_back(flow_edge(t, g[t].size(), c/*, 0, cost*/));
  g[t].push_back(flow_edge(s, g[s].size() - 1, back_c
			   /*, 0, cost*/));
}

#define MAXNODES 500

int mark[MAXNODES];

Flow inc_flow_dfs(adj_list *g, int s, int t, Flow maxf) {
  if (s == t) return maxf;
  Flow inc;   mark[s] = 0;
  for (adj_iter it = g[s].begin(); it != g[s].end(); ++it)
    if (mark[it->dest] && it->r() && 
	(inc=inc_flow_dfs(g,it->dest,t,min(maxf, it->r()))))
      return it->f+=inc, g[it->dest][it->back].f -= inc, inc;
  return 0;
}

Flow max_flow(adj_list *graph, int n, int s, int t) {
  Flow flow = 0, inc = 0;
  do flow += inc, memset(mark, 255, sizeof(int)*n);
  while ((inc = inc_flow_dfs(graph, s, t, 1<<28)));
  return flow;//inc_flow_bfs(graph, s, t, 1<<28)
  //inc_flow_bellman_ford(graph, n, s, t)
}


void solve(int P) {
  bool minimal[400], maximal[400];
  adj_list adj[400];
  

  scanf("%d%d", &n, &k);

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < k; ++j)
      scanf("%d", pr[i]+j);

  for (int i = 0;i < n; ++i) minimal[i] = maximal[i] = true;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) {
      if (below(i, j)) {
	minimal[j] = false;
	maximal[i] = false;
	flow_add_edge(adj, i, j+n, 1);
      }
    }

  for (int i = 0; i < n; ++i) {
    flow_add_edge(adj, 2*n, i, 1);
    flow_add_edge(adj, i+n, 2*n+1, 1);
  }

  int ans = max_flow(adj, 2*n+2, 2*n, 2*n+1);
  
  printf("Case #%d: %d\n", P, n-ans);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}

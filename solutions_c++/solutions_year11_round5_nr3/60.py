#include<cstdio>
#include<vector>
#include<queue>

using namespace std;

struct edge {
  int src, dst;
  edge(int s, int d)
    : src(s), dst(d) { }
};
typedef vector<edge> vertex;
typedef vector<vertex> graph;

#define idx(r, c) ((((r)+R)%R)*C+(((c)+C)%C))

void solve()
{
  int R, C;
  scanf("%d%d", &R, &C);

  graph g(R*C);
  graph r(R*C);
  for(int i=0; i<R; ++i) {
    char s[128];
    scanf("%s", s);

    for(int j=0; j<C; ++j) {
      if(s[j] == '|') {
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i+1, j)));
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i-1, j)));
      } else if(s[j] == '-') {
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i, j+1)));
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i, j-1)));
      } else if(s[j] == '\\') {
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i-1, j-1)));
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i+1, j+1)));
      } else {
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i-1, j+1)));
	g[idx(i, j)].push_back(edge(idx(i, j), idx(i+1, j-1)));
      }
      for(int k=0; k<(int)g[idx(i, j)].size(); ++k) {
	edge e = g[idx(i, j)][k];
	r[e.dst].push_back(edge(e.dst, e.src));
      }
    }
  }

  bool impossible = false;
  for(int i=0; i<R*C; ++i) {
    if(r[i].size() == 0)
      impossible = true;
  }

  while(true) {
    bool next = false;
    for(int i=0; i<R*C; ++i) {
      if(r[i].size() == 1) {
	int k = r[i][0].dst;
	if(g[k].size() == 1) continue;
	next = true;
	if(g[k][0].dst == i) {
	  edge e = g[k][0];
	  g[k].clear();
	  g[k].push_back(e);
	} else {
	  edge e = g[k][1];
	  g[k].clear();
	  g[k].push_back(e);
	}
      }
    }
    r = graph(R*C);
    for(int i=0; i<R*C; ++i) {
      for(int k=0; k<(int)g[i].size(); ++k) {
	edge e = g[i][k];
	r[e.dst].push_back(edge(e.dst, e.src));
      }
    }

    if(!next)
      break;
  }

  impossible = false;
  for(int i=0; i<R*C; ++i) {
    if(r[i].size() == 0)
      impossible = true;
  }
  if(impossible) {
    puts("0");
    return;
  }
  
  int comp = 0;
  vector<int> vis(R*C, 0);
  for(int i=0; i<R*C; ++i) {
    if(vis[i]) continue;
    queue<int> q;
    q.push(i);
    vis[i] = 1;
    while(!q.empty()) {
      int u = q.front(); q.pop();
      if(g[u].size() == 0) continue;
      for(int k=0; k<(int)g[u].size(); ++k) {
	int w = g[u][k].dst;
	for(int j=0; j<(int)r[w].size(); ++j) {
	  int v = r[w][j].dst;
	  if(vis[v]) continue;
	  vis[v] = 1;
	  q.push(v);
	}
      }
    }
    if(g[i].size() == 2) {
      comp++;
    }
  }

  int ret = 1;
  for(int i=0; i<comp; ++i)
    ret = (ret*2)%1000003;
  printf("%d\n", ret);
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int C=1; C<=T; ++C) {
    printf("Case #%d: ", C);
    solve();
  }
}

#include <cstdio>
#include <vector>

using namespace std;

#define MAX_R 2000
#define MAX_COMPONENT 2000

vector<int> adj[MAX_R];
int deg[MAX_R];
int r;
int x1[MAX_R], y1[MAX_R], x2[MAX_R], y2[MAX_R];
int cnumber[MAX_R];
int ccount;
int mx[MAX_COMPONENT];
int my[MAX_COMPONENT];
bool visited[MAX_R];

void read_input()
{
  scanf("%d",&r);
  for(int i=0; i<r; i++)
    scanf("%d %d %d %d",&x1[i], &y1[i], &x2[i], &y2[i]);
}

inline bool rtouch(int a1, int a2, int b1, int b2)
{
  a2++;
  b2++;
  return (a2 >= b1) && (b2 >= a1);
}

inline bool touch(int u, int v)
{
  return rtouch(x1[u],x2[u],x1[v],x2[v]) &&
    rtouch(y1[u],y2[u],y1[v],y2[v]);
}

void build_graph()
{
  for(int i=0; i<r; i++) {
    adj[i].clear();
    deg[i] = 0;
  }

  for(int u=0; u<r; u++)
    for(int v=0; v<r; v++)
      if(touch(u,v)) {
	adj[u].push_back(v);
	deg[u]++;

	adj[v].push_back(u);
	deg[v]++;
      }
}

void dfs(int u, int cnum)
{
  visited[u] = true;
  cnumber[u] = cnum;
  for(int i=0; i<deg[u]; i++) {
    int v = adj[u][i];
    if(!visited[v])
      dfs(v,cnum);
  }
}

void initialize()
{
  for(int i=0; i<r; i++) {
    visited[i] = false;
    cnumber[i] = -1;
  }
}

void find_component()
{
  int c=0;
  for(int i=0; i<r; i++)
    if(cnumber[i]==-1) {
      dfs(i,c);
      c++;
    }
  ccount = c;
}

void find_max_range()
{
  for(int c=0; c<ccount; c++) {
    mx[c] = 0;
    my[c] = 0;
  }
  for(int i=0; i<r; i++) {
    if(mx[cnumber[i]] < x2[i])
      mx[cnumber[i]] = x2[i];
    if(my[cnumber[i]] < y2[i])
      my[cnumber[i]] = y2[i];
  }
}

int find_max_time()
{
  int max_time = 0;
  for(int i=0; i<r; i++) {
    int tx = mx[cnumber[i]] - x1[i] + 1;
    int ty = my[cnumber[i]] - y1[i] + 1;
    if(tx + ty - 1 > max_time)
      max_time = tx + ty - 1;
  }
  return max_time;
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++) {
    read_input();
    build_graph();
    initialize();
    find_component();
    find_max_range();
    printf("Case #%d: %d\n",tt+1,find_max_time());
  }
}

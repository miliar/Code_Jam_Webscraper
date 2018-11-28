#include <cstdio>
#include <vector>

using namespace std;

#define MAX_N  100
#define MAX_K  25
#define MAX_NODE  (MAX_N*2 + 2)

int n,k;
int p[MAX_N][MAX_K];

typedef pair<int,int> edge;

vector<int> adj[MAX_NODE];
edge edges[MAX_N*MAX_N * 2*MAX_N];
int m,nn;

void read_one_input()
{
  scanf("%d %d",&n,&k);
  for(int i=0; i<n; i++)
    for(int j=0; j<k; j++)
      scanf("%d",&p[i][j]);
}

int compare(int u, int v)  // return +1 is u is greater than v
{
  if(p[u][0]==p[v][0])
    return 0;
  if(p[u][0]<p[v][0])
    return -compare(v,u);
  // now assume that u is under v
  for(int i=0; i<k; i++)
    if(p[u][i]<=p[v][i])
      return 0;
  return 1;
}

int left(int i)
{
  return i;
}

int right(int i)
{
  return n+i;
}

int add_edge(int f, int t)
{
  //printf("added: %d -> %d\n",f,t);
  edges[m].first = f;
  edges[m].second = t;
  m++;
  return m-1;
}

void build_graph()
{
  for(int i=0; i<2*n+2; i++)
    adj[i].clear();

  m = 0;
  nn = 2*n + 2;
  for(int i=0; i<n; i++)
    for(int j=i+1; j<n; j++) {
      int c = compare(i,j);
      //printf("%d,%d,%d\n",i,j,c);
      if(c==1) {
	int v = right(j);
	int e = add_edge(i,v);
	adj[i].push_back(e);
	adj[v].push_back(e);
      }
      else if(c==-1) {
	int v = right(i);
	int e = add_edge(j,v);
	adj[j].push_back(e);
	adj[v].push_back(e);
      }
    }

  for(int i=0; i<n; i++) {
    // source
    int e = add_edge(2*n,i);
    adj[2*n].push_back(e);
    // sink
    e = add_edge(right(i),2*n+1);
    adj[right(i)].push_back(e);
  }
}

int path[MAX_NODE];
int parent[MAX_NODE];
int ep[MAX_NODE];
bool visited[MAX_NODE];

bool dfs(int u)
{
  visited[u] = true;
  for(vector<int>::iterator i=adj[u].begin();
      i!=adj[u].end(); i++) {
    int e = *i;
    if(edges[e].first==u) { // goes from u
      int v = edges[e].second;
      if(!visited[v]) {
	parent[v] = u;
	ep[v] = e;
	dfs(v);
      }
    }
  }
}

bool find_path(int fr, int t)
{
  parent[fr] = -1;
  for(int i=0; i<nn; i++)
    visited[i] = false;
  parent[fr] = -1;
  ep[fr] = -1;
  dfs(fr);
  return visited[t];
}

void augment()
{
  int v = 2*n+1;
  while(v!=-1) {
    if(ep[v]!=-1) {
      int e = ep[v];
      int t = edges[e].first;
      edges[e].first = edges[e].second;
      edges[e].second = t;
    }
    v = parent[v];
  }
}

int max_flow()
{
  int f = 0;
  while(find_path(2*n, 2*n+1)) {
    augment();
    f++;
  }
  return f;
}

main()
{
  int t;
  scanf("%d", &t);
  for(int tt=0; tt<t; tt++) {
    read_one_input();
    build_graph();
    int f = max_flow();
    printf("Case #%d: %d\n",tt+1,n-f);
  }
}

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <string>
using namespace std;

//http://www.prefield.com/algorithm/basic/template.html
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

//http://www.prefield.com/algorithm/graph/graph.html
typedef int Weight;
struct Edge {
  int src, dst;
  Weight cost;
  int capacity;
  Edge(int src, int dst, Weight weight, int capacity_) :
    src(src), dst(dst), cost(weight), capacity(capacity_) { }
};
#define weight capacity
bool operator < (const Edge &e, const Edge &f) {
  return e.cost != f.cost ? e.cost > f.cost : // !!INVERSE!!
    e.src != f.src ? e.src < f.src : e.dst < f.dst;
}

typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

typedef vector<Weight> Array;
typedef vector<Array> Matrix;

#define INF 1000000

#define RESIDUE(s,t) (capacity[s][t]-flow[s][t])
Weight maximumFlow(const Graph &g, int s, int t) {
  int n = g.size();
  Matrix flow(n, Array(n)), capacity(n, Array(n));
  REP(u,n) FOR(e,g[u]) capacity[e->src][e->dst] += e->weight;

  Weight total = 0;
  while (1) {
    queue<int> Q; Q.push(s);
    vector<int> prev(n, -1); prev[s] = s;
    while (!Q.empty() && prev[t] < 0) {
      int u = Q.front(); Q.pop();
      for(int dst=0;dst<n;dst++){
        if (prev[dst] < 0 && RESIDUE(u, dst) > 0) {
        prev[dst] = u;
        Q.push(dst);
      }
      }
/*
      FOR(e,g[u]) if (prev[e->dst] < 0 && RESIDUE(u, e->dst) > 0) {
        prev[e->dst] = u;
        Q.push(e->dst);
      }
*/
    }
    if (prev[t] < 0) return total; // prev[x] == -1 <=> t-side
    Weight inc = INF;
    for (int j = t; prev[j] != j; j = prev[j])
      inc = min(inc, RESIDUE(prev[j], j));
    for (int j = t; prev[j] != j; j = prev[j])
      flow[prev[j]][j] += inc, flow[j][prev[j]] -= inc;
    total += inc;
  }
}

int price[100][25];
int main( void )
{
 int T;
 cin>>T;
 for(int X=1;X<=T;++X){
  int n,k;
  cin>>n>>k;
  Graph g(2*n+4);
  int s=2*n+0;
  int t=2*n+1;
  int s0=2*n+2;
  int t0=2*n+3;
  for(int y=0;y<n;++y){
   for(int i=0;i<k;i++)
    cin>>price[y][i];
  }
  for(int y=0;y<n;++y){
  {
   Edge e(s,y*2+0, 0, 1);
   g[s].push_back(e);
  }
  {
   Edge e(y*2+1,t, 0, 1);
   g[y*2+1].push_back(e);
  }
  {
   Edge e(s0,y*2+1, 0, 1);
   g[s0].push_back(e);
  }
  {
   Edge e(y*2+0,t0, 0, 1);
   g[y*2+0].push_back(e);
  }


  for(int j=0;j<n;++j){
   bool ok=true;
   for(int i=0;i<k;i++)
    if(price[y][i]>=price[j][i]){ok=false;break;}
   if(ok){
    {
     Edge e(y*2+1,j*2+0, 0, 1);
     g[y*2+1].push_back(e);
    }
   }
  }}

   {
    Edge e(s0,s, 0, 1);
    g[s0].push_back(e);
   }
   {
    Edge e(t,t0, 0,1);
    g[t].push_back(e);
   }
  int r;
  for(r=1;r<=n;++r){
   g[s0][g[s0].size()-1].capacity = r;
   g[t][g[t].size()-1].capacity = r;
   int v  = maximumFlow(g,s0,t0);
   //printf( "%d: %d %d\n", r, v, 0 );
   if(v == r + n )
   break;
  }
  printf("Case #%d: %d\n",X,r);
 }
 return 0;
}


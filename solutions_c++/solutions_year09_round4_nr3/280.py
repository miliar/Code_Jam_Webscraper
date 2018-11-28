#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }


const int NMAX = 200;
const int MMAX = 200;

#define WHITE 0
#define GRAY 1
int N,M; //sizes of the S and T sets
vector<int> adj[NMAX]; //adj[u][i]=v -> u in (0...n-1); v in (0..m-1)
int color[NMAX];
vector<int> path; //path contains only right side vertices
int match[MMAX]; //-1 or the vertex in S {0..n-1} matched

int aug(int u) {
  if (color[u] == WHITE) {
    color[u] = GRAY;
    rep(i,adj[u].size()) {
      int v = adj[u][i]; int w = match[v]; path.push_back(v);
      if (w == -1) return 1;
      else {
        if (aug(w)) return 1;
        else path.pop_back();
      }
    }
  }
  return 0;
}

int matching() {
  int u, v, w, flow = 0;
  rep(i,M) match[i] = -1;
  rep(i,N) {
    //Solve matching
    rep(j,N) color[j] = WHITE;
    path.clear();
    flow += aug(i);
    
    //Update path
    u = i;
    rep(j,path.size()) {
      w = path[j]; v = match[w]; match[w] = u; u = v;
    }
  }
  return flow;
}


  
int pr[NMAX][NMAX];
  

main() {
	int n,k, T;
	cin >> T;
	
	rep(t,T) {
		cin >> n >> k;
		rep(i,n) rep(j,k) cin >> pr[i][j];
		N = n; M = n;
		
		rep(i,NMAX) adj[i].clear();		
		
		rep(i,n) rep(j,n) if (i != j) {
			bool below = true;
			rep(r, k) if (pr[i][r] >= pr[j][r]) {below = false; break;}
			if (below == true) adj[i].push_back(j);
		}
		
		cout << "Case #" << t+1 << ": " << n - matching() << endl;	
	}
}

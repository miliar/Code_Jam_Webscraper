#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

// BEGIN CUT HERE
#define RUNCASE -1
// END CUT HERE

int N,K,M;
VVI cap;

int smaller(VI a, VI b) {
  REP(i, K) if(a[i]>=b[i]) return 0;
  return 1;
}

VI vis;
bool dfs(int n, int t) {
  if(n==t) return true;
  if(vis[n]) return false;
  vis[n]=1;
  REP(i, M) if(cap[n][i] && dfs(i, t)) {cap[n][i]--; cap[i][n]++; return true;}
  return false;
}

int maxflow(int s, int t) {
  int res=0;
  while(vis=VI(M), dfs(s,t)) res++;
  return res;
}

void go() {
  cin >> N >> K;
  VVI price(N,VI(K));
  REP(i, N) REP(j, K) cin >> price[i][j];
  VVI edge(N,VI(N));
  REP(i, N) REP(j, N) edge[i][j]=smaller(price[i], price[j]);
  //cout << endl; REP(i, N) {REP(j, N) cout << edge[i][j] << " "; cout << endl;}
  M=2*N+N*N+2;
  cap=VVI(M,VI(M));
  REP(i, N) REP(j, N) if(edge[i][j]) {cap[i][2*N+i*N+j]=1; cap[2*N+i*N+j][N+j]=1;}
  REP(i, N) {cap[M-2][i]=1; cap[i+N][M-1]=1;}
  //cout << endl; REP(i, M) {REP(j, M) cout << cap[i][j] << " "; cout << endl;}
  int res=maxflow(M-2,M-1);
  //cout << res << " ";
  cout << N-res << endl;
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) {
    printf("Case #%d: ", i+1);
    go();
  }
}

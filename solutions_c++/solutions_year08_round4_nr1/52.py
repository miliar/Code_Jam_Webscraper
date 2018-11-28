#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

const int inf = 123456789;
int cas = 0;
int M,V;
int I[1<<15],G[1<<15],C[1<<15];
int dp[1<<15][2];
bool isleaf(int i) { return i >= (M-1)/2; }
int doop(int g, int a, int b) {
  if (g == 0) return a || b;
  if (g == 1) return a && b;
  assert(0);
}
void doit() {
  scanf("%d%d",&M,&V);
  assert(M < (1<<15));
  FOR(i,M) {
    if (isleaf(i)) {
      scanf("%d",&I[i]);
    } else {
      scanf("%d%d",&G[i],&C[i]);
    }
  }

  for (int i = M-1; i >= 0; --i) {
    FOR(v,2) {
      if (isleaf(i)) {
	dp[i][v] = I[i] == v ? 0 : inf;
      } else {
	dp[i][v] = inf;
	FOR(g,2) FOR(a,2) FOR(b,2) if (C[i] || g == G[i]) {
	  if (doop(g,a,b) == v) {
	    dp[i][v] <?= (g!=G[i]) + dp[2*i+1][a] + dp[2*i+2][b];
	  }
	}
      }
    }
  }

  int ans = dp[0][V];

  printf("Case #%d: ",++cas);
  if (ans < inf/2) {
    printf("%d\n",ans);
  } else {
    printf("IMPOSSIBLE\n");
  }
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}

#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define A first
#define B second

typedef long double ld;

ld bc[41][41];
int C,N;
ld dp[41];

int cas=0;
void doit() {
  scanf("%d%d",&C,&N);
  assert(bc[C][N] != 0);

  CLR(dp,0);
  FR(c,1,C+1) {
    ld q = bc[C-c][N] / bc[C][N];
    ld p = 1 - q;
    assert(p != 0);
    dp[c] = 1;
    //fprintf(stderr, "prob to moveon %d: %Lf\n",c,p);
    FR(k,1,N+1) if (k <= c) {
    /*
      fprintf(stderr, "%Lf * %Lf * %Lf / %Lf\n",
	dp[c-k],bc[c][k],bc[C-c][N-k],bc[C][N]);*/
      dp[c] += dp[c-k] * bc[c][k] * bc[C-c][N-k] / bc[C][N];
      //fprintf(stderr, "  dp[%d] = %Lf\n",c,dp[c]);
    }
    dp[c] /= p;
    //fprintf(stderr, "dp[%d] = %Lf\n", c, dp[c]);
    assert(dp[c] == dp[c]);
  }

  ld ans = dp[C];

  printf("Case #%d: %.7Lf\n", ++cas, ans);
}

int zzzz;
int main() {
  CLR(bc,0);

  bc[0][0] = 1;

  FR(n,1,41) FOR(k,n+1) {
    bc[n][k] = bc[n-1][k];
    if (n) bc[n][k] += bc[n-1][k-1];
    assert(bc[n][k] == bc[n][k]);
  }

  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}

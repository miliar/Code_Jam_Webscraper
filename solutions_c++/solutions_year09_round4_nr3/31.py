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

int cas=0;
int n,k;
int p[100][25];
bool adj[100][100];
bool mark[100];
int rmatch[100];
bool dfs(int l) {
  if (mark[l]) return 0;
  mark[l] = 1;

  FOR(r,n) if (adj[l][r]) {
    if (rmatch[r]==-1 || dfs(rmatch[r])) {
      rmatch[r] = l;
      return 1;
    }
  }
  return 0;
}
void doit() {
  scanf("%d%d",&n,&k);

  FOR(i,n) FOR(j,k) scanf("%d",&p[i][j]);

  CLR(adj,0);

  FOR(i,n) FOR(j,n) if (i!=j) {
    adj[i][j] = 1;
    FOR(t,k) if (p[i][t] <= p[j][t]) adj[i][j] = 0;
  }

  int ans = n;
  CLR(rmatch,-1);
  FOR(i,n) {
    CLR(mark,0);
    ans -= dfs(i);
  }

  printf("Case #%d: %d\n", ++cas, ans);
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}

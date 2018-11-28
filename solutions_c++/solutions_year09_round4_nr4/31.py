#include <algorithm>
#include <cmath>
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
int N;
int xs[40],ys[40],rs[40];
void doit() {
  scanf("%d",&N);
  FOR(i,N) scanf("%d %d %d",&xs[i],&ys[i],&rs[i]);

  double ans = 1e10;

  if (N==1) {
    ans = rs[0];
  } else if (N==2) {
    ans = max(rs[0],rs[1]);
  } else if (N==3) {
    setmin(ans, max((double)rs[0], 0.5*(rs[1]+rs[2]+hypot(xs[2]-xs[1],ys[2]-ys[1]))));
    setmin(ans, max((double)rs[1], 0.5*(rs[0]+rs[2]+hypot(xs[2]-xs[0],ys[2]-ys[0]))));
    setmin(ans, max((double)rs[2], 0.5*(rs[0]+rs[1]+hypot(xs[0]-xs[1],ys[0]-ys[1]))));
  } else {
    assert(0);
  }

  printf("Case #%d: %.6lf\n",++cas,ans);
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}

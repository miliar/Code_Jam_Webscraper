#define DEBUG 0
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int INF = 2000000001;
#define FOR(x,b,e) for(int x=(b);x<=(e);++x)
#define FORD(x,b,e) for(int x=(b);x>=(e);--x)
#define REP(x,n) for(int x=0;x<(n);++x)
#define ALL(c) c.begin(),c.end()
#define VAR(x,c) __typeof(c) x=(c)
#define FOREACH(x,c) for(VAR(x,(c).begin());x!=(c).end();++x)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define dbg(...) \
  do { if (DEBUG) fprintf(stderr, __VA_ARGS__); } while (0)

const int MAXN = 10000;

int N, DEST;
int d[MAXN+1], l[MAXN+1];
int X[MAXN+1] = {0};

int main() {
  int Z;
  scanf("%d", &Z);
  for (int T = 1; T <= Z; T++) {
    scanf("%d", &N);
    REP (i,N) {
      X[i] = 0;
      scanf("%d%d", &d[i], &l[i]);
    }
    scanf("%d", &DEST);

    X[0] = d[0];
    
    REP (i,N) {
      FOR(j,i+1,N-1) {
        if (d[j]-d[i] > X[i]) { break; }
        X[j] = max(X[j], min(l[j], d[j]-d[i]));
      }
    }

    bool flag = false;
    REP (i,N) {
      if (X[i] >= DEST - d[i]) {
        flag = true;
        break;
      }
    }

    //dbg("N: %d, D: %d\n", N, DEST);
    printf("Case #%d: ", T);
    if (flag) printf("YES");
    else printf("NO");
    printf("\n");
  }
  return 0;
}

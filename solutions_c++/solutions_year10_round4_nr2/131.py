#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <utility>

template <class T>
inline int size(const T &t) { return t.size(); }

using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define PD pushdown
#define MP makepair

#define REP(a,n) for (int a = 0; a<(n); ++a)
#define FOR(a,b,c) for (int a = (b); a<=(c); ++a)
#define FORD(a,b,c) for (int a = (b); a>=(c); --a)
#define INIT(a,v) __typeof(v) a = (v)
#define FOREACH(a,v) for (INIT(a,(v).begin()); a!=(v).end(); ++a)

#define INF 1000000000

///////////////////////

int N, P;
int ile_op[1024], ceny[11][1024];
int wyn[11][11][1024];

int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    scanf("%d", &P);
    N = 1<<P;
    REP(a, N) {
      scanf("%d", &ile_op[a]);
      REP(x, P+1)
        wyn[0][x][a] = x<=ile_op[a] ? 0 : INF;
    }
    REP(p, P)
      REP(a, 1<<(P-p-1)) {
        scanf("%d", &ceny[p][a]);
        int cl = INF, cp = INF;
        FORD(x, P, 0) {
          wyn[p+1][x][a] = cl+cp;
          cl = min(cl, wyn[p][x][2*a]);
          cp = min(cp, wyn[p][x][2*a+1]);
          wyn[p+1][x][a] = min(wyn[p+1][x][a], cl+cp+ceny[p][a]);
        }
      }
    int best = INF;
    REP(x, P+1)
      best = min(best, wyn[P][x][0]);
    printf("Case #%d: %d\n", tt+1, best);
  }
}

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

///////////////////////

int tab[103][103];

int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    int R;
    REP(a, 103) REP(b, 103) tab[a][b] = 0;
    scanf("%d", &R);
    REP(a, R) {
      int x1, x2, y2, y1;
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      FOR(x, x1, x2) FOR(y,y1,y2)
        tab[x][y] = 1;
    }
    int sek = 1;
    for (;;) {
      int jest = 0;
      FORD(x,101,1)
        FORD(y,101,1) {
          if (tab[x][y-1] && tab[x-1][y])
            tab[x][y] = 1;
          else if (!tab[x][y-1] && !tab[x-1][y])
            tab[x][y] = 0;
          jest |= tab[x][y];
        }
      if (!jest)
        break;
      ++sek;
    }
    printf("Case #%d: %d\n", tt+1, sek);
  }
}

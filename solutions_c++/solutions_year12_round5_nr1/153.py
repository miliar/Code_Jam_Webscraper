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

struct A {
  int P, L, nr;
} tab[1000];

bool mn(A a, A b) {
  if (a.P*b.L>b.P*a.L) return true;
  if (a.P*b.L<b.P*a.L) return false;
  return a.nr<b.nr;
}
int N;


int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    scanf("%d", &N);
    REP(a, N) {
      scanf("%d", &tab[a].L);
      tab[a].nr = a;
    }
    REP(a, N)
      scanf("%d", &tab[a].P);
    printf("Case #%d:", tt+1);
    sort(tab, tab+N, mn);
    REP(a, N)
      printf(" %d", tab[a].nr);
    printf("\n");
  }
}



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

int N;
int tab[60][60];

int szukaj() {
  FORD(sr, N-1, 0) {
    REP(x, sr)
      REP(y, sr-x)
        if (tab[y][x]!=tab[sr-x][sr-y])
          goto zle;
    return N-1-sr;
    zle:;
  }
  return -10000;
}

void odbx() {
      int a = 0, b = N-1;
      while (a<b) {
        REP(x, N)
          swap(tab[a][x], tab[b][x]);
        ++a, --b;
      }
}

void odby() {
      int a = 0, b = N-1;
      while (a<b) {
        REP(x, N)
          swap(tab[x][a], tab[x][b]);
        ++a, --b;
      }
}

int main() {
  int TT;
  scanf("%d", &TT);
  REP(tt, TT) {
    scanf("%d", &N);
    REP(a, 2*N-1)
      REP(b, N)
        if (a-b>=0 && a-b<N)
          scanf("%d", &tab[a-b][b]);
      int w0 = szukaj();
      odbx();
      int c1 = szukaj();
      odby();
      int w1 = szukaj();
      odbx();
      int c0 = szukaj();
      int N2 = N+min(c0, c1)+min(w1, w0);
      printf("Case #%d: %d\n", tt+1, N2*N2-N*N);
  }
}



#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define STRING(x) #x
#define PING cerr << "(" << __LINE__ << "): " << __FUNCTION__ << endl
#define PRINT(x) cerr << STRING(x) << " = " << (x) << endl

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }

int N[] = {0, 1, 1, 1, 2, 2, 2, 3, 3, 3,
           4, 4, 4, 5, 5, 5, 6, 6, 6,
           7, 7, 7, 8, 8, 8, 9, 9, 9,
           10, 10, 10};

int S[] = {-1, -1, 2, 2, -1, 3, 3, -1, 4, 4,
           -1, 5, 5, -1, 6, 6, -1, 7, 7,
           -1, 8, 8, -1, 9, 9, -1, 10, 10,
           -1, 11, 11};

int main() {
  int tab[101];
  int T;
  scanf("%d\n", &T);
  REP(t, T) {
    int n, s, p;
    scanf("%d%d%d", &n, &s, &p);
    REP(i, n) scanf("%d", tab + i);
    sort(tab, tab + n);
    ULL count = 0;
    REP(i, n) {
      if (N[tab[i]] >= p) ++count;
      else if (s && S[tab[i]] >= p) {
        ++count; --s;
      }
    }
    printf("Case #%d: %I64u\n", t + 1, count);
  }
  return 0;
}



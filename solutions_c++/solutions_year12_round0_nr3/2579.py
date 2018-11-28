#include <algorithm>
#include <cassert>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(LL i=(a),_b=(b);i<=_b;++i)
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

LL mult[] = {0, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};

int main() {
  int T;
  scanf("%d\n", &T);
  REP(t, T) {
    LL a, b;
    scanf("%I64d %I64d", &a, &b);
    ULL count = 0;
    FOR(x, a, b - 1) {
      const int n = floor(log10(x));
      set<LL> bef;
      REP(i, n) {
        LL num = x;
        LL rem = num % mult[i + 1];
        num /= mult[i + 1];
        num += (mult[n - i] * rem);
        if (num <= b && num > x && !bef.count(num)) {
          ++count;
        }
        bef.insert(num);
      }
    }
    printf("Case #%d: %I64u\n", t + 1, count);
  }
  return 0;
}



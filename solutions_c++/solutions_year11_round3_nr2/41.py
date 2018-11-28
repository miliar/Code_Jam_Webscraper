#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;
typedef pair<LL, LL> pll;
typedef vector<LL> vl;
typedef vector<double> vd;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define SZ(a) (a.size())
#define MP(a, b) make_pair(a, b)
#define SHL(a,b) ((a) << (b))
#define SHR(a,b) ((a) >> (b))
#define FI first
#define SE second
#define PB push_back

template<class T> int bitcount(T a) { int x = 0; while (a) { x += (a & 1); a >>= 1; } return x; }
template<class T> inline T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> inline T sqr(T a) { return a * a; } // NOTE: T must be enough to save sqr!
inline int parity(LL a) { return __builtin_parityl(a); }
inline int parity(int a) { return __builtin_parity(a); }
template<class T> T s2type(string s) { T res; istringstream in(s); in >> res; return res; }
template<class T> string toString(T n) { ostringstream out; out << n; return out.str(); }

const double PI = acos(-1.0);
const double EPS = 1e-11;

int ts;
int L, N, C;
LL T;
LL d[1234567];
LL td[1234567];
pll x[1234567];

int main()
{
  int i, j, k, t;
  LL ans;
  scanf("%d", &ts);
  FOR(t, ts)
  {
    scanf("%d %lld %d %d", &L, &T, &N, &C);
    td[0] = 0; j = -1;
    FOR(i, C) { scanf("%lld", &d[i]); d[i] *= 2; td[i+1] = td[i] + d[i]; if (j == -1 && td[i + 1] > T) j = i; }
    k = C;
    while (k < N)
    {
      d[k] = d[k % C];
      td[k+1] = td[k] + d[k];
      if (j == -1 && td[k+1] > T) j = k;
      k++;
    }
//    FOR(i, N) printf("%d: %lld %lld\n", i, d[i % C], td[i+1]);
//    printf("%d\n", j);
    ans = td[N];
    if (j != -1)
    {
      k = 1; x[0] = MP(T - td[j+1], j);
      FORI(i, j+1, N-1) x[k++] = MP(-d[i], i);
      sort(x, x+k);
//      FOR(i, k) printf("possible boost: %d @%lld %lld\n", i, x[i].SE, -x[i].FI / 2);
//      printf("%d\n", k);
      FOR(i, min(L, k))
      {
        ans += x[i].FI / 2;
      }
    }

    printf("Case #%d: %lld\n", t + 1, ans);
  }
  return 0;
}


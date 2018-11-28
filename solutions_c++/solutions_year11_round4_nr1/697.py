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
typedef vector<LL> vl;
typedef vector<double> vd;
typedef pair<double, pii> pdii;

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
int X, S, R, T, N;
//pdii a[1024];
pii a[1024];

int main()
{
  int i, j, k, l, b, t;
  double ans, left, tmp;
  scanf("%d", &ts);
  FOR(t, ts)
  {
    scanf("%d %d %d %d %d", &X, &S, &R, &T, &N);
    l = 0; ans = 0.0;
    R -= S; left = T;
//    FOR(i, N) { scanf("%d %d %d", &j, &k, &b); a[i] = MP((double) ((k - j) * 1.0) / (b + S), MP(k - j, b + S)); l += k - j; }
    FOR(i, N) { scanf("%d %d %d", &j, &k, &b); a[i] = MP(b + S, k - j); l += k - j; }
//    if (l != X) a[N++] = MP((X - l * 1.0) / S, MP(X - l, S));
    if (l != X)
      a[N++] = MP(S, X - l);
    sort(a, a+N);
//    FOR(i, N) printf("%d: %d %d\n", i, a[i].FI, a[i].SE);
//    FOR(i, N) printf("%d: %lf %d %d\n", i, a[i].FI, a[i].SE.FI, a[i].SE.SE);
//    printf("improve = %d\n", R);
//    FORD(i, N-1, 0)
    FOR(i, N)
    {
      if (left > 0.0)
      {
        if (left * (a[i].FI + R) < a[i].SE)
        {
          tmp = left * (a[i].FI + R);
          ans += left + ((a[i].SE - tmp) / a[i].FI);
          left = 0.0;
        }
        else
        {
          tmp = a[i].SE * 1.0 / (a[i].FI + R);
          ans += tmp;
          left -= tmp;
        }
      }
      else ans += a[i].SE * 1.0 / a[i].FI;
//      printf("%d: %lf\n", i, left);
    }

    printf("Case #%d: %.10lf\n", t + 1, ans);
  }
  return 0;
}


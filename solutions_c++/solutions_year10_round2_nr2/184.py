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
const int MAXN = 50;

int N, K, B, T;
int x[MAXN];
int v[MAXN];
int ok[MAXN];

int main()
{
  int tc, t;
  int i, j, k, l;
  int ans;

  scanf("%d", &tc);
  FOR(t, tc)
  {
    ans = 0;
    scanf("%d %d %d %d", &N, &K, &B, &T);
    FOR(i, N) scanf("%d", &x[i]);
    FOR(i, N) scanf("%d", &v[i]);
    FOR(i, N) ok[i] = (T * v[i] + x[i] >= B);
    j = 0;
    FORD(i, N-1, 0)
    {
      if (ok[i]) { ans += j; K--; }
      else j++;
      if (K == 0) break;
    }

    printf("Case #%d: ", t + 1);
    if (K > 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;
}


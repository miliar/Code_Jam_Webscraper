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

int ok(int n, int m)
{
  int i = 1, j = 1;
  while (j <= n) j *= 10;
  while (i <= n)
  {
    i *= 10;
    j /= 10;
    if (m == ((n % i) * j + n / i)) return 1;
  }
  return 0;
}

int main()
{
  int tc, t, a, b;
  int i, j, k, l;
  int ans;
  int y[10];

  scanf("%d", &tc);
  FOR(t, tc)
  {
    map<string, vi> x;
    vs z;
    ans = 0;
    scanf("%d %d", &a, &b);
    FORI(i, a, b)
    {
      ZERO(y);
      j = i;
      while (j > 0) { y[j % 10]++; j /= 10; }
      string s = "";
      FOR(j, 10) s += (char) (y[j] + '0');
      if (x.find(s) != x.end())
        x[s].PB(i);
      else
      {
        vi v;
        v.PB(i);
        x[s] = v;
        z.PB(s);
      }
     }
    FOR(i, SZ(z))
    {
      vi v = x[z[i]];
      l = SZ(v);
//      fprintf(stderr, "--- %d\n", l);
      FOR(j, l) FORI(k, j+1, l-1)
      {
        ans += ok(v[j], v[k]);
      }
    }
//    FOR(i, SZ(z)) cout << z[i] << " " << SZ(x[z[i]]) << endl;
    x.clear();
    z.clear();
    printf("Case #%d: %d\n", t + 1, ans);
  }
  return 0;
}


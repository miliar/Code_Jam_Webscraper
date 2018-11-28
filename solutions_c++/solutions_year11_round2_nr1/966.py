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

int ts;

int main()
{
  int i, j, k, t, n;
  char b[128][128];
  int wp1[128];
  int wp2[128];
  double owp[128];
  double oowp[128];

  scanf("%d", &ts);
  FOR(t, ts)
  {
    scanf("%d", &n);
    FOR(i, n) scanf("%s", b[i]);
    FOR(i, n)
    {
      wp1[i] = wp2[i] = 0;
      FOR(j, n) if (b[i][j] != '.') { wp1[i]++; wp2[i] += b[i][j] == '1' ? 1 : 0; }
    }
    FOR(i, n)
    {
      owp[i] = 0.0;
      FOR(j, n) if (i != j && b[i][j] != '.')
      {
//        if (b[i][j] == '.') owp[i] += (wp2[j] * 1.0 / wp1[j]);
        if (b[i][j] == '1') owp[i] += (wp2[j] * 1.0 / (wp1[j] - 1));
        else owp[i] += ((wp2[j] - 1.0) / (wp1[j] - 1.0));
      }
      owp[i] /= wp1[i];
    }
    FOR(i,n)
    {
      oowp[i] = 0.0;
      FOR(j, n) if (i != j && b[i][j] != '.')
      {
        oowp[i] += owp[j];
      }
      oowp[i] /= wp1[i];
    }

    printf("Case #%d:\n", t + 1);
    FOR(i, n)
    {
//      printf("%d %d %lf %lf\n", wp1[i], wp2[i], owp[i], oowp[i]);
      printf("%.10lf\n", (wp2[i] * 0.25 / wp1[i]) + owp[i] * 0.5 + oowp[i] * 0.25);
    }
  }
  return 0;
}


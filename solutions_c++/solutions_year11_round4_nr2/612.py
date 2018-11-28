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
char z[512];
int a[512][512];
int R, C, D;

int ok(int r, int c, int K)
{
  int i, j, k;

  // R
  k = 0;
  FOR(i, K) FOR(j, K)
  {
    k += (i * 2 - (K - 1)) * (a[i + r][j + c]);
//    printf("%d %d %d\n", i, j, (i * 2 - (K - 1)) * (a[i + r][j + c]));
  }
//  printf("%d\n", k);
  k -= -(K - 1) * (a[r][c]) +
       -(K - 1) * (a[r][c+K-1]) +
       (K - 1) * (a[r+K-1][c]) +
       (K - 1) * (a[r+K-1][c+K-1]);
//  printf("R: %d %d %d %d\n", r, c, K, k);
  if (k == 0)
  {
    // C
    k = 0;
    FOR(i, K) FOR(j, K) k += (j * 2 - (K - 1)) * (a[i + r][j + c]);
    k -= -(K - 1) * (a[r][c]) +
         -(K - 1) * (a[r+K-1][c]) +
         (K - 1) * (a[r][c+K-1]) +
         (K - 1) * (a[r+K-1][c+K-1]);
//    printf("C: %d %d %d %d\n", r, c, K, k);
  }
  return k == 0;
}

int blah(int k)
{
  int i, j;
  FOR(i, R-k+1) FOR(j, C - k+1) if (ok(i, j, k)) return 1;
  return 0;
}

int main()
{
  int i, j, k, t;
  int ans;
  scanf("%d", &ts);
  FOR(t, ts)
  {
    scanf("%d%d%d", &R, &C, &D);
    FOR(i, R) { scanf("%s", z); FOR(j, C) a[i][j] = z[j] - '0' + D; }
//    printf("%d\n", min(R, C));
    FORD(k, min(R, C), 3)
    {
      if (blah(k)) break;
    }
    if (k < 3)
      printf("Case #%d: IMPOSSIBLE\n", t + 1);
    else
      printf("Case #%d: %d\n", t + 1, k);
  }
  return 0;
}


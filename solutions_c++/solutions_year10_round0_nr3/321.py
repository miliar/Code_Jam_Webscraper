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

const int MAXN = 1024;

int main()
{
  int t;
  int R, K, N;
  int g[MAXN];
  int done[MAXN];
  int cek[MAXN];
  int i, j, k;
  int cur, round;
  long long ans;
  long long all;
  long long mult[MAXN];

  scanf("%d", &t);
  FOR(i, t)
  {
    scanf("%d %d %d", &R, &K, &N);
    all = 0;
    FOR(j, N) { scanf("%d", &g[j]); all += g[j]; }
    MINUS(done);
    ZERO(mult);
    cur = round = 0;
    ans = 0;
    if (all <= K)
    {
      ans = all * R;
    }
    else
    {
      while (done[cur] == -1 && round < R)
      {
        mult[cur] = ans;
        done[cur] = round;
        k = 0;
        while (k + g[cur] <= K)
        {
          k += g[cur];
          cur = (cur + 1) % N;
        }
        ans += k;
        round++;
      }
//      printf("%d %d %lld\n", round, cur, ans);
      if (done[cur] != -1)
      {
        ans += (ans - mult[cur]) * ((R - round) / (round - done[cur]));
        round += ((R - round) / (round - done[cur])) * (round - done[cur]);
      }
//      printf("%d %d %lld %lld\n", round, cur, ans, all);
      while (round < R)
      {
        k = 0;
        while (k + g[cur] <= K)
        {
          k += g[cur];
          cur = (cur + 1) % N;
        }
        ans += k;
        round++;
      }
    }
    printf("Case #%d: %lld\n", i + 1, ans);
  }

  return 0;
}


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
typedef pair<pair<LL, LL>, int> pli;

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
LL con[64];
int P, W;

int main()
{
  int i, j, k, t;
  int ans;
  int thr;
  LL l;

  scanf("%d", &ts);
  FOR(t, ts)
  {
    queue<pli> q;
    map<LL, int> m;
    ZERO(con);
    ans = -1; thr = -1;

    scanf("%d %d", &P, &W);
    FOR(i, W) { scanf("%d,%d", &j, &k); con[j] |= (1LL << k); con[k] |= (1LL << j); }

    q.push(MP(MP(con[0], 1LL), 0));
    while (!q.empty())
    {
      pli p = q.front(); q.pop();
      if (ans != -1) // just check
      {
        if (p.SE == ans && ((p.FI.FI) & 2LL))
          thr = max(thr, bitcount(p.FI.FI - p.FI.SE));
      }
      else // check + add to queue!
      {
        if ((p.FI.FI) & 2LL)
        {
          ans = p.SE;
          thr = bitcount(p.FI.FI - p.FI.SE);
        }
        else
        {
          FOR(i, P)
            if ((p.FI.FI & (1LL << i)) && !(p.FI.SE & (1LL << i)))
            {
              l = p.FI.SE | (1LL << i);
              if (m.find(l) == m.end() && (p.FI.FI | con[i]) > p.FI.FI)
              {
                m[l] = 1;
                q.push(MP(MP(p.FI.FI | con[i], l), p.SE + 1));
              }
            }
        }
      }
    }

    printf("Case #%d: %d %d\n", t + 1, ans, thr);
  }
  return 0;
}


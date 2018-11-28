/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>
#include <queue>

using namespace std;

#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%Ld"
#endif

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

#define EOL(i, n) " \n"[i == (n) - 1]
#define LEN(a) (int)(sizeof(a) / sizeof(a[0]))
#define IS(a, i) (((a) >> (i)) & 1)

typedef double dbl;
typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;
typedef unsigned char byte;

template <class T> T inline sqr(T x) { return x * x; }
template <class T> inline void relaxMin( T &a, T b ) { a = min(a, b); }
template <class T> inline void relaxMax( T &a, T b ) { a = max(a, b); }

string str( int i ) { char s[100]; sprintf(s, "%d", i); return string(s); }

template <class T> inline T sign( T x ) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
template <class T> inline T myAbs( T a ) { return a > 0 ? a : -a; }

const int maxn = 10;
const int maxV = 2 * maxn * maxn;

int h, w;
char s[maxn][maxn];
vi in[maxV];
vi g[maxV];

int u[maxV];
int cc, fail, on, o[maxV];
int next[maxV], to[maxV][2];
int is[maxV][maxV];

void dfs( int v )
{
  u[v] = 1;
  forn(i, sz(g[v]))
    if (!u[g[v][i]])
      dfs(g[v][i]);
  o[on++] = v;
}

void paint( int v )
{
  if (fail)
    return;
  if (u[v ^ 1])
  {
//    printf("%d,%d : %d,%d\n", (v / 2) / w, (v / 2) % w, u[v ^ 1], cc);
    fail = 1;
  }
  next[v / 2] = to[v / 2][v & 1];
  printf("next[%d] = %d\n", v / 2, to[v / 2][v & 1]);
  u[v] = cc;
  forn(i, sz(g[v]))
    if (!u[g[v][i]])
      paint(g[v][i]);
}

#define F(i, j) ((i) * w + (j))

void go( int v )
{
  u[v] = 1;
  if (!u[next[v]])
    go(next[v]);
}

int main()
{
  int tn;
  scanf("%d", &tn);
  forab(tt, 1, tn)
  {
    forn(i, maxV)
    {
      in[i].clear();
      g[i].clear();
    }

    scanf("%d%d", &h, &w);
    forn(i, h)
      scanf("%s", s[i]);
    forn(i, h)
      forn(j, w)
      {
        const char *str = "-|/\\";
        int dx[] = {1, 0, 1, 1};
        int dy[] = {0, 1, -1, 1};
        int k = strchr(str, s[i][j]) - str;
        int i1 = (i + dy[k] + h) % h; 
        int j1 = (j + dx[k] + w) % w; 
        int i2 = (i - dy[k] + h) % h; 
        int j2 = (j - dx[k] + w) % w;
        in[F(i1, j1)].pb(F(i, j) * 2 + 0);
        in[F(i2, j2)].pb(F(i, j) * 2 + 1);
        to[F(i, j)][0] = F(i1, j1);
        to[F(i, j)][1] = F(i2, j2);
      }
    forn(i, maxV)
    {
      vi &v = in[i];
      forn(a, sz(v))
        forn(b, sz(v))
          if (a != b)
          {
//            printf("%d -> %d\n", v[a], v[b] ^ 1);
            g[v[a]].pb(v[b] ^ 1);
          }
    }

    int vn = h * w * 2;
    zero(u);
    on = 0;
    forn(i, vn)
      if (!u[i])
        dfs(i);
    assert(on == vn);

    memset(is, 0, sizeof(is));
    forn(i, vn)
      forn(j, sz(g[i]))
        is[i][g[i][j]] = 1;
    forn(k, vn)
      forn(i, vn)
        forn(j, vn)
          is[i][j] |= is[i][k] & is[k][j];

    int num = 0;
    forn(pr, 1 << (h * w))
    {
      zero(u);
      forn(i, h * w)
        u[i * 2 + IS(pr, i)] = 1;

      int fail = 0;
      forn(i, vn)
        forn(j, vn)
          if (u[i] && u[j] && is[i][j ^ 1])
            fail = 1;
      num += !fail;
    }
    fprintf(stderr, "Case #%d: %d\n", tt, num);
    printf("Case #%d: %d\n", tt, num);

  }
  return 0;
}

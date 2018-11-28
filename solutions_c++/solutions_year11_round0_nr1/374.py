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

template <class T> T inline sqr(T x) { return x * x; }
template <class T> inline void relaxMin( T &a, T b ) { a = min(a, b); }
template <class T> inline void relaxMax( T &a, T b ) { a = max(a, b); }

string str( int i ) { char s[100]; sprintf(s, "%d", i); return string(s); }

inline int sign( int x ) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
inline int myAbs( int a ) { return a > 0 ? a : -a; }

const int maxn = (int)1e5;

char ch[maxn];
int n, x[maxn];
int T, cnt, p[2], cx[2];

int main()
{
  int TN;
  scanf("%d", &TN);
  forab(tn, 1, TN)
  {
    scanf("%d", &n);
    forn(i, n)
      scanf(" %c%d", &ch[i], &x[i]);

    T = 0, p[0] = p[1] = 0, cx[0] = cx[1] = 1, cnt = 0;
    while (cnt < n)
    {
      int old = cnt;
      T++;
      forn(i, 2)
      {
        int &j = p[i];
        while (j < n && (ch[j] == 'O') != i)
          j++;
        if (j == n)
          continue;
        if (cx[i] != x[j])
          cx[i] += (x[j] > cx[i] ? 1 : -1);
        else if (j == old)
          cnt++, j++;
      }
    }
    printf("Case #%d: %d\n", tn, T);
  }
  return 0;
}

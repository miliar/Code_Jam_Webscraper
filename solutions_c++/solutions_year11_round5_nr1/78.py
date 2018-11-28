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

const int maxn = (int)1e5 + 10;
const dbl eps = 1e-9;

int X1[maxn], Y1[maxn], X2[maxn], Y2[maxn];
dbl Ly[maxn], Ry[maxn], H[maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  forab(tt, 1, tn)
  {
    int W, N1, N2, K;
    scanf("%d%d%d%d", &W, &N1, &N2, &K);
    vi xx;
    forn(i, N1)
      scanf("%d%d", &X1[i], &Y1[i]), xx.pb(X1[i]);
    forn(i, N2)
      scanf("%d%d", &X2[i], &Y2[i]), xx.pb(X2[i]);
   sort(all(xx));
   int num = unique(all(xx)) - xx.begin();

/*
   forn(i, N1)
     printf("(%d,%d)%c", X1[i], Y1[i], EOL(i, N1));
   forn(i, N2)
     printf("(%d,%d)%c", X2[i], Y2[i], EOL(i, N1));
*/

   printf("Case #%d:\n", tt);

   dbl S = 0;
   int a = 0, b = 0;
   forn(i, num)
   {
     while (X1[a + 1] < xx[i]) a++;
     while (X2[b + 1] < xx[i]) b++;
     assert(a + 1 < N1);
     assert(b + 1 < N2);
     Ly[i] = Y1[a] + (dbl)(Y1[a + 1] - Y1[a]) * (xx[i] - X1[a]) / (X1[a + 1] - X1[a]);
     Ry[i] = Y2[b] + (dbl)(Y2[b + 1] - Y2[b]) * (xx[i] - X2[b]) / (X2[b + 1] - X2[b]);
     H[i] = fabs(Ry[i] - Ly[i]);
     //printf("H[%d] = %.20lf (x = %d)\n", i, H[i], xx[i]);
   }
   forn(i, num - 1)
     S += (xx[i + 1] - xx[i]) * (H[i + 1] + H[i]) / 2;
   //printf("S = %.20lf, K = %d --> %.20lf\n", S, K, S / K);

   S /= K;
   dbl curS = 0;
   int cnt = 0;
   forab(i, 1, num - 1)
   {
     dbl dS = (xx[i] - xx[i - 1]) * (H[i - 1] + H[i]) / 2;
     dbl curX = xx[i - 1], curH = H[i - 1];
     dbl koef = (H[i] - H[i - 1]) / (xx[i] - xx[i - 1]);
     //printf("curS = %.20lf, curX = %.20lf, curH = %.20lf, dS = %.20lf, koef = %.20lf\n", curS, curX, curH, dS, koef);
     while (curS + dS >= S - eps)
     {
       dbl A = 0.5 * koef;
       dbl B = curH;
       dbl C = -(S - curS);
       dbl x;
       if (fabs(A) < eps)
         x = -C / B;
       else
       {
         assert(B * B >= 4 * A * C - eps);
         dbl x1 = (-B - sqrt(fabs(B * B - 4 * A * C))) / (2 * A);
         dbl x2 = (-B + sqrt(fabs(B * B - 4 * A * C))) / (2 * A);
         if (x1 < -eps)
           x = x2;
         else if (x2 < -eps)
           x = x1;
         else
           x = min(x1, x2);
         //printf("roots: %.20lf, %.20lf\n", x1, x2);
       }
       //printf("A=%.20lf, B=%.20lf, C=%.20lf, x=%.20lf\n", A, B, C, x);
       curX += x, curH += x * koef;
       if (++cnt < K)
         printf("%.20lf\n", curX);
       dS -= (S - curS), curS = 0;
     }
     curS += dS;
//     printf("H[%d] = %.20lf, curS = %.20lf\n", i, H[i], curS);
   }
  }
  return 0;
}

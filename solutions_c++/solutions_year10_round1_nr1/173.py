#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>

#define oo 1234567890
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

using namespace std;

const double PI = 2.0 * acos (0.0);

typedef pair <int, int> PII;
typedef long long LL;

inline int getInt () { int x; scanf ("%d", &x); return x; }
inline LL getLL () { LL x; scanf ("%lld", &x); return x; };
inline int NUM (char c) { return (int)c - 48; }
inline char CHR (int n) { return (char)(n + 48); }
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

// ptrrsn_1's template

int nTC;
int N, K;
char M[55][55];
char TMP[55][55];

inline void readInput () {
       scanf ("%d%d", &N, &K);
       
       REP (i, N) {
           scanf ("%s", M[i]);
       }
}

inline void rotate () {
       REP (i, N) {
           REP (j, N) {
               TMP[i][j] = M[i][j];
           }
       }
       
       REP (i, N) REP (j, N)
           M[j][N - i - 1] = TMP[i][j];
}

inline void gravity () {
       REPD (i, N) {
            REP (j, N) {
                if (M[i][j] != '.')
                   continue;
                FORD (k, i - 1, 0) {
                     if (M[k][j] != '.') {
                        M[i][j] = M[k][j];
                        M[k][j] = '.';
                        break;
                     }
                }
            }
       }
}

bool red = false, blue = false;

inline void checkWinner () {
       REP (i, N) {
           REP (j, N) {
               if (M[i][j] == '.')
                  continue;
               // horizontal
               int ctr = 0;
               REP (k, K) {
                   if (j + k >= N)
                      break;
                   if (M[i][j + k] == M[i][j])
                      ctr++;
               }
               
               if (ctr == K) {
                  if (M[i][j] == 'B')
                     blue = true;
                  else
                      red = true;
               }
               
               ctr = 0;
               REP (k, K) {
                   if (i + k >= N)
                      break;
                   if (M[i + k][j] == M[i][j])
                      ctr++;
               }
               
               if (ctr == K) {
                  if (M[i][j] == 'B')
                     blue = true;
                  else
                      red = true;
               }
               
               ctr = 0;
               
               REP (k, K) {
                   if (i + k >= N || j + k >= N)
                      break;
                   if (M[i + k][j + k] == M[i][j])
                      ctr++;
               }
               
               
               if (ctr == K) {
                  if (M[i][j] == 'B')
                     blue = true;
                  else
                      red = true;
               }
               
               ctr = 0;
               
               REP (k, K) {
                   if (i + k >= N || j - k < 0)
                      break;
                   if (M[i + k][j - k] == M[i][j])
                      ctr++;
               }
               
               if (ctr == K) {
                  if (M[i][j] == 'B')
                     blue = true;
                  else
                      red = true;
               }
               
           }
       }
}

int main () {
    freopen ("Alarge.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    
    scanf ("%d", &nTC);
    
    REP (tc, nTC) {
          readInput ();
          rotate ();
          gravity ();
          
          red = blue = false;
          
          checkWinner ();
          
          printf ("Case #%d: ", tc + 1);
          if (red && blue)
             puts ("Both");
          else if (red)
               puts ("Red");
          else if (blue)
               puts ("Blue");
          else
              puts ("Neither");
    }
    
    return 0;
}

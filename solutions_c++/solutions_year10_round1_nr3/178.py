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
int A1, A2, B1, B2;
int ret;

inline bool isWin (int A, int B) {
       if (A == 0 || B == 0)
          return true;
       if (A < B)
          swap (A, B);
       if (isWin (B, A % B)) {
          if (A / B == 1) {
                return false;
          } else {
                 return true;
          }
       } else {
          return true;
       }
}

int main () {
    freopen ("Csmall.in", "r", stdin);
    freopen ("Csmall.out", "w", stdout);
    
    scanf ("%d", &nTC);
    
    FOR (tc, 1, nTC) {
        scanf ("%d%d%d%d", &A1, &A2, &B1, &B2);
        ret = 0;
        FOR (i, A1, A2) {
            FOR (j, B1, B2) {
                if (isWin (i, j)) {
                   ret++;
                }
            }
        }
        
        printf ("Case #%d: %d\n", tc, ret);
    }
    return 0;
}

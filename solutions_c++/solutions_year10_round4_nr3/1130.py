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

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

using namespace std;

const double PI = 2.0 * acos (0.0);

typedef long long LL;
typedef pair <int, int> PII;

inline int getInt () { int x; scanf ("%d", &x); return x; }
inline LL getLL () { LL x; scanf ("%lld", &x); return x; };
inline int NUM (char c) { return (int)c - 48; }
inline char CHR (int n) { return (char)(n + 48); }
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

// ptrrsn_1's template

#define MAXR 500
#define MAXC 500

int nTC;
int M[MAXR + 2][MAXC + 2];
int tmp[MAXR + 2][MAXC + 2];

int main () {
    nTC = getInt ();
    
    FOR (tc, 1, nTC) {
        int N = getInt ();
        RESET (M, 0);
        REP (i, N) {
            int r1, c1, r2, c2;
            scanf ("%d%d%d%d", &c1, &r1, &c2, &r2);
            r1--; c1--; r2--; c2--;
            FOR (i, r1, r2) {
                FOR (j, c1, c2) {
                    M[i][j] = 1;
                }
            }
        }
        int ret = 0;
        while (true) {
            bool finish = true;
            REP (i, 100) {
                REP (j, 100) {
                    if (M[i][j]) {
                        finish = false;
                    }
                }
            }
            if (finish)
                break;
            ret++;
            REP (i, 100) {
                REP (j, 100) {
                    if (i > 0 && j > 0 && M[i - 1][j] && M[i][j - 1] && !M[i][j]) {
                        tmp[i][j] = 1;
                    } else if ((i == 0 || !M[i - 1][j]) && (j == 0 || !M[i][j - 1]) && M[i][j]) {
                        tmp[i][j] = 0;
                    } else {
                        tmp[i][j] = M[i][j];
                    }
                }
            }
            REP (i, 100) {
                REP (j, 100) {
                    M[i][j] = tmp[i][j];
                }
            }
        }
        printf ("Case #%d: %d\n", tc, ret);
    }
    
    return 0;
}

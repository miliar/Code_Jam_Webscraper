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

#define MAXN 100
#define MAXDATA 300

int nTC;
int D, I, M, N;
int data[MAXN + 5];
int dp[MAXN + 5][MAXDATA + 5];

int main () {
    freopen ("blarge.in", "r", stdin);
    freopen ("blarge.out", "w", stdout);
    
    scanf ("%d", &nTC);
    
    FOR (tc, 1, nTC) {
        scanf ("%d%d%d%d", &D, &I, &M, &N);
        REP (i, N)
            scanf ("%d", &data[i]);
        
        // impossible
        REP (i, N + 1)
            REP (j, 256)
                dp[i][j] = oo;
        
        REP (i, 256)
            dp[0][i] = 0;
        
        FOR (i, 1, N) {
            // Delete
            REP (j, 256) {
                dp[i][j] = MIN (dp[i][j], dp[i - 1][j] + D);
            }
            // Change and Insert between
            REP (k, 256) {
                if (M != 0) {
                    REP (j, 256) {
                        int cost = abs (k - j);
                        cost = cost / M + (cost % M > 0);
                        cost--;
                        if (cost < 0)
                           cost = 0;
                      //  if (k == 5 && i == N && j < 20)
                      //     printf ("j = %d, cost = %d\n", j, cost);
                        dp[i][k] = MIN (dp[i][k], dp[i - 1][j] + cost * I + abs (data[i - 1] - k));
                       // if (k == 5 && i == N && j < 20)
                     //   printf ("dp = %d\n", dp[i][k]);
                    }
                } else {
                   dp[i][k] = MIN (dp[i][k], dp[i - 1][k] + abs (data[i - 1] - k));
                }
               // if (k == 5 && i == N)
               //    printf ("hasil = %d\n", dp[i][k]);
            }
        }
        
        /*
        REP (i, N + 1) {
            REP (j, 10) {
                printf ("%d ", dp[i][j]);
            }
            puts ("");
        }
        */
        
        int ret = oo;
        REP (i, 256) {
            ret = MIN (ret, dp[N][i]);
        }
        
        printf ("Case #%d: %d\n", tc, ret);
    }
    return 0;
}

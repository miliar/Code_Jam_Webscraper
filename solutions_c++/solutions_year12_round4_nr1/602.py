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
#include <sstream>
#include <ctime>

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
template <class T> inline T ABS (T a) { if (a < 0) return -a; return a; }

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

// ptrrsn_1's template

#define MAXN 10005

int N, d[MAXN + 5], len[MAXN + 5], D;
int dp[MAXN + 5];
int L[MAXN + 5];

int main () {
    int nTC;
    scanf("%d", &nTC);
    FOR (tc, 1, nTC) {
        scanf("%d", &N);
        REP (i, N) scanf("%d%d", &d[i], &len[i]);
        scanf("%d", &D);
        d[N] = D;
        len[N] = 0;
        
        RESET(L, -1);
        L[0] = MIN(len[0], d[0]);
        REP (i, N) {
            if (L[i] == -1) continue;
           // cout << i << " " << L[i] << endl;
            FOR (j, i + 1, N) {
                if (d[j] - d[i] <= L[i]) {
                    L[j] = MAX(L[j], MIN(len[j], d[j] - d[i]));
                }
            }
        }
      //  cout << L[N] << endl;
        bool ret = (L[N] != -1);
        
        if (ret) printf("Case #%d: YES\n", tc);
        else printf("Case #%d: NO\n", tc);
    }
    
    return 0;
}

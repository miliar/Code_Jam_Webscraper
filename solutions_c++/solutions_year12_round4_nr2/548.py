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

#define MAXN 1000

int N, W, L;
int r[MAXN + 5];
vector <PII> v;
double x[MAXN + 5], y[MAXN + 5];

int main () {
    int nTC;
    scanf("%d", &nTC);
    
    FOR (tc, 1, nTC) {
        scanf("%d%d%d", &N, &W, &L);
        REP (i, N) scanf("%d", &r[i]);
        v.clear();
        REP (i, N) v.PB(MP(r[i], i));
        sort(ALL(v));
        swap(v[0], v[SIZE(v) - 1]);
        sort(v.begin() + 1, v.end());
        /*
        REP (i, SIZE(v)) cout << v[i].F << " " << v[i].S << endl;
        cout << endl;
        */
        RESET(x, 0);
        RESET(y, 0);
        double bef = v[0].F;
        y[v[0].S] = 0;
        double hehe = bef;
        bool flag = false;
        
        REP (i, N) {
            if (i == 0) continue;
            
            if (!flag) {
                y[v[i].S] = y[v[i - 1].S] + bef + v[i].F;
                if (y[v[i].S] > MAX(W, L)) {
                    y[v[i].S] = 0;
                    x[v[i].S] = hehe + v[i].F;
                    flag = true;
                }
            } else
                x[v[i].S] = x[v[i - 1].S] + bef + v[i].F;
            
            bef = v[i].F;
        }
        if (W > L) REP (i, N) swap(x[i], y[i]);
        /*
        REP (i, N) REP (j, N) {
            if (i == j) continue;
            if (sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j])) < r[i] + r[j] - eps) {
                cerr << "Case " << tc << endl;
                break;
            }
        }
        
        REP (i, N) {
            if (x[i] > W + eps || y[i] > L + eps) {
                cerr << "Case " << tc << " is wrong!" << endl;
                break;
            }
        }
        */
        printf("Case #%d:", tc);
        REP (i, N) printf(" %.15lf %.15lf", x[i], y[i]);
        puts("");
    }
    
    return 0;
}

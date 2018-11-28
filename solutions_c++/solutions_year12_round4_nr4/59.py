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

#define MAXROW 60
#define MAXCOL 60
#define MAXN 10

int nrows, ncols;
char M[MAXROW + 5][MAXCOL + 5];
int N;
int ans[MAXN + 5];
bool legal[MAXN + 5];
bool found[MAXROW + 5][MAXCOL + 5];

inline bool valid (int r, int c) {
    return r >= 0 && r < nrows && c >= 0 && c < ncols && M[r][c] != '#';
}

vector <PII> s;

int dfs(int r, int c) {
    if (found[r][c]) return 0;
    found[r][c] = true;
    int ret = 1;
    s.PB(MP(r, c));
    if (valid(r - 1, c)) ret += dfs(r - 1, c);
    if (valid(r, c - 1)) ret += dfs(r, c - 1);
    if (valid(r, c + 1)) ret += dfs(r, c + 1);
    return ret;
}

int what;
map <vector <PII>, bool> MAP;

#define s _s
bool solve(vector <PII> s) {
    vector <PII> TMP;
    sort(ALL(s));
    s.resize(unique(ALL(s)) - s.begin());
    if (MAP.count(s) != 0) return false;
    MAP[s] = true;
    if (SIZE(s) == 1 && M[s[0].F][s[0].S] == CHR(what)) return true;
    /*
    cout << "start" << endl;
    REP (i, SIZE(s)) cout << s[i].F << " " << s[i].S << endl;
    cout << endl;
    */
    // bawah
    TMP = s;
    REP (i, SIZE(s)) {
        int r = s[i].F, c = s[i].S;
        if (valid(r + 1, c)) s[i].F++;
    }
    if (solve(s)) return true;
    s = TMP;
    
    // kiri
    REP (i, SIZE(s)) {
        int r = s[i].F, c = s[i].S;
        if (valid(r, c - 1)) s[i].S--;
    }
    if (solve(s)) return true;
    s = TMP;
    
    // kanan
    REP (i, SIZE(s)) {
        int r = s[i].F, c = s[i].S;
        if (valid(r, c + 1)) s[i].S++;
    }
    if (solve(s)) return true;
    return false;
}
#undef s

int main () {
    int nTC;
    scanf("%d", &nTC);
    FOR (tc, 1, nTC) {
        cerr << tc << endl;
        printf("Case #%d:\n", tc);
        scanf("%d%d", &nrows, &ncols);
        REP (i, nrows) scanf("%s", M[i]);
        N = 0;
        REP (i, nrows) REP (j, ncols) if (isdigit(M[i][j])) {
            N = MAX(N, (int)(M[i][j] - '0') + 1);
        }
        REP (i, nrows) REP (j, ncols) if (isdigit(M[i][j])) {
            RESET(found, 0);
            int x = M[i][j] - '0';
            what = x;
            s.clear();
            ans[x] = dfs(i, j);
            // REP (i, SIZE(s)) cout << s[i].F << " " << s[i].S << endl;
            MAP.clear();
            legal[x] = solve(s);
        }
        REP (i, N) {
            printf("%d: %d ", i, ans[i]);
            if (legal[i]) puts("Lucky");
            else puts("Unlucky");
        }
    }
    return 0;
}

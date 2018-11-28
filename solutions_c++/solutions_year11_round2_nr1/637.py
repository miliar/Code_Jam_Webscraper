#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define PB push_back
#define PII pair<int, int>
#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

const int maxn = 100 + 10;
const int inf = (-1u) >> 1;

int Case = 1;
int n, b[maxn], a[maxn];
char s[maxn][maxn];
double wp[maxn], owp[maxn];

void init() {
    scanf ("%d", &n);
    REP(i,n) {
        scanf ("%s", s[i]);
        a[i] = b[i] = 0;
        REP(j,n) {
            if (s[i][j] != '.') ++b[i];
            if (s[i][j] == '1') ++a[i];
        }
        if (b[i] == 0) puts ("!!!");
        wp[i] = (double)a[i] / b[i];
    }
}

void solve() {
    printf ("Case #%d:\n", Case++);
    REP(i,n) {
        double tot = 0;
        int num = 0;
        REP(j,n) if (s[i][j] != '.') {
            int a1 = 0, b1 = 0;
            REP(k,n) if (k != i) {
                if (s[j][k] != '.') ++b1;
                if (s[j][k] == '1') ++a1;
            }
            tot += (double)a1 / b1;
            ++num;
        }
        if (num == 0) puts ("num !!!");
        owp[i] = tot / num;
        //printf ("%d: %lf\n", i, owp[i]);
    }
    REP(i,n) {
        double ans = wp[i]/4 + owp[i]/2;
        double tot = 0;
        int num = 0;
        REP(j,n) if (s[i][j] != '.') {
            tot += owp[j];
            ++num;
        }
        if (num == 0) puts ("num !!!");
        ans += tot / (4*num);
        printf ("%.10lf\n", ans);
    }
}

//#define SMALL
#define LARGE

int main() {
    string name = "A";
    #ifdef SMALL
    freopen ((name + "-small-attempt0.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}



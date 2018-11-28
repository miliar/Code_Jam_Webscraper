#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

#define PB push_back
#define PII pair<int, int>
#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;
const double eps = 1e-8;

int sgn(double x) {
    return (x > eps) > (x < -eps);
}

int Case = 1;
int len, v1, v2, rt, n;

struct range {
    int s, e, v;
    range(int _s=0, int _e=0, int _v=0):
        s(_s), e(_e), v(_v) {
    }
    void input() {
        scanf ("%d%d%d", &s, &e, &v);
    }
    bool operator<(const range& r) const {
        return s < r.s;
    }
};

bool comp(const range& r1, const range& r2) {
    return r1.v < r2.v;
}

range r[maxn*3];

void init() {
    scanf ("%d%d%d%d%d", &len, &v1, &v2, &rt, &n);
    REP(i,n) {
        r[i].input();
    }
    sort (r, r + n);
}

void solve() {
    printf ("Case #%d: ", Case++);
    int pre = 0, pn = n;
    REP(i,pn) {
        if (pre < r[i].s) {
            r[n++] = range(pre, r[i].s, 0);
        }
        pre = r[i].e;
    }
    if (pre < len) {
        r[n++] = range(pre, len, 0);
    }
    sort (r, r + n, comp);
    double lefttime = rt, ans = 0;
    REP(i,n) {
        int vrun = v2+r[i].v;
        int vwalk = v1+r[i].v;
        double len = 1.0*r[i].e - r[i].s;
        double nowt;
        if (sgn(lefttime) > 0) {
            if (sgn(lefttime*vrun - len) > 0) {
                nowt = len/vrun;
                lefttime -= nowt;
            } else {
                double nowlen = len - lefttime * vrun;
                nowt = lefttime + nowlen/vwalk;
                lefttime = 0;
            }
        } else {
            nowt = len/vwalk;
        }
        ans += nowt;
    }
    printf ("%.8lf\n", ans);
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




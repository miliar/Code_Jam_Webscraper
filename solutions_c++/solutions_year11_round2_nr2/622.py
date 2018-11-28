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

const int maxn = 200 + 10;
const int inf = (-1u) >> 1;
const double eps = 1e-8;
const double eeps = 1e-12;

int sgn(double x) {
    return (x > eps) - (x < -eps);
}

int ssgn(double x) {
    return (x > eeps) - (x < -eeps);
}

int Case = 1;
int n, d, b[maxn], a[maxn];

void init() {
    scanf ("%d%d", &n, &d);
    REP(i,n) {
        scanf ("%d%d", &a[i], &b[i]);
    }
}

bool check(double t) {
    double nowl = a[0] - t;
    REP(i,n) {
        double minl = a[i]-t;
        double maxl = a[i]+t;
        minl = max(minl, nowl);
        //printf ("minl %lf nowl %lf\n", minl, nowl);
        double avalen = (maxl - minl);
        if (ssgn((double)d*(b[i]-1) - avalen) > 0) {
            return false;
        }
        nowl = minl + (double)d*b[i];
    }
    return true;
}

void solve() {
    printf ("Case #%d: ", Case++);
    double l = 0, r = 1e10;
    //check(2.5);
    while (ssgn(l-r) < 0) {
        double mid = (l+r) / 2;
        if (check(mid)) {
            r = mid;
        } else {
            l = mid;
        }
    }
    printf ("%.10lf\n", l);
}

#define SMALL
//#define LARGE

int main() {
    string name = "B";
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


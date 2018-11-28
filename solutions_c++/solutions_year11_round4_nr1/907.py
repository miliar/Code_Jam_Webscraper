#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
//#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "A"
#define RR 151

struct node {
    int l, r, w;
    node (int l = 0, int r = 0, int w = 0)
        : l (l), r (r), w (w) {}
    void read () {
        cin >> l >> r >> w;
    }
    bool operator < (const node &o) const {
        return l < o.l;
    }
};

int X, S, R, t, n;
node a[1 << 17];

inline bool pred (const node &a, const node &b) {    
    /*double da = (a.r - a.l) / (S + a.w + 0.0) / (R + a.w + 0.0);
    double db = (b.r - b.l) / (S + b.w + 0.0) / (R + b.w + 0.0);
    return da > db;*/  
    return a.w < b.w;
}

void solve () {
    cin >> X >> S >> R >> t >> n;
    for (int i = 0; i < n; ++i)
        a[i].read();
    sort(a, a + n);
    int m = n;
    if (a[0].l) a[m++] = node(0, a[0].l);
    if (a[n - 1].r < X) a[m++] = node(a[n - 1].r, X);
    for (int i = 0; i + 1 < n; ++i) {
        int l = a[i].r;
        int r = a[i + 1].l;
        if (l < r) a[m++] = node(l, r);
    }
    n = m;
    sort(a, a + n, pred);
    double res = 0.0;
    double time = t;
    for (int i = 0; i < n; ++i) {
        double L = a[i].r - a[i].l;
        double L1 = min(L, time * (R + a[i].w));
        res += L1 / (R + a[i].w) + (L - L1) / (S + a[i].w);
        time -= L1 / (R + a[i].w);
    }
    printf("%.15lf\n", res);
}

//#define SMALL
#define LARGE
//#define DEBUG

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt2.in", "r", stdin);
    freopen(TASK "-small-attempt2.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);

        printf("Case #%d: ", test);

        solve();
        
        fprintf(stderr, "done.\n");
    }
    return 0;
}

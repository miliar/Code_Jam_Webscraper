#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
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
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "B"
#define RR 151

struct point {
    double x, y;
    point () {}
    point (double x, double y) 
        : x (x), y (y) {}
    point operator - (const point &o) const {
        return point(x - o.x, y - o.y);
    }
    point operator + (const point &o) const {
        return point(x + o.x, y + o.y);
    }
    point operator * (int m) const {
        return point(x * m, y * m);
    }
};

int n, m, d;
string a[1 << 4];

inline bool check (int x, int y, int side) {
    point o ((x + x + side) / 2.0, (y + y + side) / 2.0);
    point res (0.0, 0.0);
    for (int i = 0; i < side; ++i) {
        for (int j = 0; j < side; ++j) {
            if (i == 0 && j == 0 || i == 0 && j == side - 1 || i == side - 1 && j == 0 || i == side - 1 && j == side - 1) continue;
            point p (x + i + 0.5, y + j + 0.5);
            res = res + (p - o) * (d + a[x + i][y + j]);
        }
    }
    return fabs(res.x) < eps && fabs(res.y) < eps;    
}

inline bool check (int side) {
    for (int i = 0; i + side - 1 < n; ++i) {
        for (int j = 0; j + side - 1 < m; ++j) {
            if (check(i, j, side))
                return true;
        }
    }
    return false;
}

void solve () {
    cin >> n >> m >> d;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            a[i][j] -= '0';
    for (int k = min(n, m); k >= 3; --k) {
        if (check(k)) {
            printf("%d\n", k);
            return;
        }
    }
    puts("IMPOSSIBLE");
}

#define SMALL
//#define LARGE
//#define DEBUG

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
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

#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
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

int n;
string a[1 << 7];
double wp[1 << 7];
double owp[1 << 7];
double oowp[1 << 7];
double tmp[1 << 7];

void solve () {
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    memset(wp, 0, sizeof wp);
    memset(owp, 0, sizeof owp);
    memset(oowp, 0, sizeof oowp);
    for (int i = 0; i < n; ++i) {
        int num = 0, den = 0;
        for (int j = 0; j < n; ++j) {
            if (a[i][j] != '.') ++den;
            if (a[i][j] == '1') ++num;
        }
        if (!num) continue;
        wp[i] = double(num) / den;
    }
    for (int i = 0; i < n; ++i) {
        memset(tmp, 0, sizeof tmp);
        for (int j = 0; j < n; ++j) {
            int num = 0, den = 0;
            if (a[i][j] != '.') {
                for (int k = 0; k < n; ++k) {
                    if (a[j][k] != '.' && k != i) ++den;
                    if (a[j][k] == '1' && k != i) ++num;
                }
            }
            if (!num) continue;
            tmp[j] = double(num) / den;
        }
        int den = 0;
        double num = 0.0;   
        for (int j = 0; j < n; ++j) {
            if (a[i][j] != '.') {
                ++den;
                num += tmp[j];
            }
        }
        if (!den) continue;
        owp[i] = num / den;
    }
    for (int i = 0; i < n; ++i) {
        int den = 0;
        double num = 0.0;
        for (int j = 0; j < n; ++j) {
            if (a[i][j] != '.') {
                ++den;
                num += owp[j];
            }
        }
        if (!den) continue;
        oowp[i] = num / den;
    }
    for (int i = 0; i < n; ++i)
        printf("%.15lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
}

//#define SMALL
#define LARGE
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

        printf("Case #%d:\n", test);

        solve();
        
        fprintf(stderr, "done.\n");
    }
    return 0;
}

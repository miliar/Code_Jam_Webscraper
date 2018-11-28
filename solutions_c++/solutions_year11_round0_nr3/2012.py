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
#define TASK "C"
#define RR 151

int n;
int a[1 << 10];

void solve () {
    int xor = 0;
    for (int i = 0; i < n; ++i)
        xor ^= a[i];
    if (xor) {
        puts("NO");
        return;
    }
    sort(a, a + n, greater<int>());
    printf("%d\n", accumulate(a, a + n - 1, 0));
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

        printf("Case #%d: ", test);

        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> a[i];

        solve();
        
        fprintf(stderr, "done.\n");
    }

    return 0;
}

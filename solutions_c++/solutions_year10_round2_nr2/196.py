#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 50 + 10;
const int inf = (-1u) >> 1;
const double eps = 1e-8;

int Case = 1;
int n, k, b, t, x[maxn], v[maxn];
double mint[maxn], cat[maxn][maxn];
int ti[maxn];

int sgn(double x) {
    return (x > eps) - (x < -eps);
}

void init() {
    scanf ("%d%d%d%d", &n, &k, &b, &t);
    for (int i = 0; i < n; ++i)
        scanf ("%d", &x[i]);
    for (int i = 0; i < n; ++i) {
        scanf ("%d", &v[i]);
        mint[i] = ((double)b - x[i]) / v[i];
    }
}

void solve() {
    printf ("Case #%d: ", Case++);
    int ans = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (sgn(mint[i] - t) > 0) {
            ti[i] = inf;
            continue;
        }
        ti[i] = 0;
        int j = i + 1;
        while (j < n && ti[j] == inf)
            ++j, ++ti[i];
        if (j < n)
            ti[i] += ti[j];
        if (k == 0)
            break;
        //printf ("%d yes %d\n", i, ti[i]);
        --k, ans += ti[i];
    }
    if (k)
        puts("IMPOSSIBLE");
    else
        printf ("%d\n", ans);
}

//#define SMALL
#define LARGE

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


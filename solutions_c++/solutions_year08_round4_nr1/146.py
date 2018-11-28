// comment

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

const int nmax = 1 << 16;
const int inf = (int)1e+9;

int n, needvalue;
int a[nmax], b[nmax];
int change[nmax];
int state[nmax];

void init() {
    scanf("%d%d", &n, &needvalue);
    for (int i = 1; i <= n; ++i) a[i] = b[i] = inf, state[i] = -1;
    int x;
    for (int i = 1; i <= n; ++i) {
        if (2*i + 1 <= n) {
            scanf("%d%d", &state[i], &change[i]);
        } else {
            scanf("%d", &x);
            if (x == 1) a[i] = 0; else b[i] = 0;
        }
    }
}

int getTrue(int x, int s) {
    if (s == 0) return min(a[2*x], a[2*x + 1]);
    return min(inf, a[2*x] + a[2*x + 1]);
}

int getFalse(int x, int s) {
    if (s == 1) return min(b[2*x], b[2*x + 1]);
    return min(inf, b[2*x] + b[2*x + 1]);
}

void solve() {
    for (int i = (n - 1) / 2; i > 0; --i) {
        a[i] = getTrue(i, state[i]);
        if (change[i]) a[i] = min(a[i], getTrue(i, 1 - state[i]) + 1);

        b[i] = getFalse(i, state[i]);
        if (change[i]) b[i] = min(b[i], getFalse(i, 1 - state[i]) + 1);
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        init();
        solve();
        int res = (needvalue == 1) ? a[1] : b[1];
        printf("Case #%d: ", testid + 1);
        if (res < inf) printf("%d\n", res); else printf("IMPOSSIBLE\n");
    }
    
    return 0;
}

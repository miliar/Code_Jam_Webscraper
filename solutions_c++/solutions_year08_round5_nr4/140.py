// simple

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <string>

using namespace std;

const int inf = (int)1e+9;
const int nmax = 101;
const int mode = 10007;

int a[nmax][nmax];
int n, m;
bool bad[nmax][nmax];

void init() {
    int b;
    scanf("%d%d%d", &n, &m, &b);
    for (int i = 0; i < b; ++i) {
        int x, y;
        scanf("%d%d", &x, &y);
        bad[x][y] = true;
    }
}

void solve() {
    a[1][1] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) if (!bad[i][j]) {
            if (i >= 3 && j >= 2) a[i][j] += a[i - 2][j - 1];
            if (i >= 2 && j >= 3) a[i][j] += a[i - 1][j - 2];
            a[i][j] %= mode;
        }
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        memset(bad, 0, sizeof(bad));
        memset(a, 0, sizeof(a));
        init();
        solve();

        printf("Case #%d: ", testid + 1);
        printf("%d\n", a[n][m]);

        cerr << testid + 1 << endl;
    }

    return 0;
}

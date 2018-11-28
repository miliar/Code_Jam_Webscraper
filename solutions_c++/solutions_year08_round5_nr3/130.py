// dp with profile

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <string>

using namespace std;

const int inf = (int)1e+9;
const int nmax = 12;

int a[nmax][1 << nmax];
int b[nmax][nmax];
int n, m;

void init() {
    scanf("%d%d\n", &n, &m);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            char c = fgetc(stdin);
            if (c == 'x') b[i][j] = 1;
        }
        scanf("\n");
    }
}

bool right(int row, int x) {
    for (int i = 0; i < m; ++i) {
        if (((x >> i) & 1)) {
            if ((x >> i) & 2) return false;
            if (row >= 0) if (b[row][i] == 1) return false;
        }
    }
    return true;
}

bool good(int x, int y) {
    for (int i = 0; i < m; ++i) {
        if (((x >> i) & 1) && (y >> i) & 2) return false;
        if (((y >> i) & 1) && (x >> i) & 2) return false;
    }
    return true;
}

int bitcnt(int x) {
    int res = 0;
    while (x > 0) {
        res += (x & 1);
        x >>= 1;
    }
    return res;
}

void solve() {
    for (int i = 1; i <= n + 1; ++i) {
        for (int pi = 0; pi < (1 << m); ++pi) if (right(i - 1, pi)) {
            for (int pj = 0; pj < (1 << m); ++pj) if (right(i - 2, pj)) {
                if (good(pi, pj)) {
                    a[i][pi] = max(a[i][pi], a[i - 1][pj] + bitcnt(pi));
                }
            }
        }        
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));

        init();
        solve();

        printf("Case #%d: ", testid + 1);
        printf("%d\n", a[n + 1][0]);

        cerr << testid + 1 << endl;
    }

    return 0;
}

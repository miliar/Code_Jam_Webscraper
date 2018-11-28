#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int r, c, d;
char tmpTable[15][15];

char table[30][30];

int go(int a, int b, int d) {
    if (a - d < 0 || a + d >= r) return 0;
    if (b - d < 0 || b + d >= c) return 0;
    int x = 0;
    int y = 0;
    for (int i = a - d; i <= a + d; ++i)
        for (int j = b - d; j <= b + d; ++j) {
            if (i == a - d && j == b - d) continue;
            if (i == a - d && j == b + d) continue;
            if (i == a + d && j == b - d) continue;
            if (i == a + d && j == b + d) continue;
            x += (i - a) * (d + table[i][j] - '0');
            y += (j - b) * (d + table[i][j] - '0');
        }
    return ((x == 0) && (y == 0));
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        scanf("%d%d%d", &r, &c, &d);
        for (int i = 0; i < 2 * r + 1; ++i)
            for (int j = 0; j < 2 * c + 1; ++j)
                table[i][j] = '0';
        for (int i = 0; i < r; ++i) {
            scanf("%s", &tmpTable[i]);
            for (int j = 0; j < c; ++j)
                table[2 * i + 1][2 * j + 1] = tmpTable[i][j];
        }
        int res = -1;
        r = 2 * r + 1;
        c = 2 * c + 1;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j) {
                if (i % 2 == 1 && j % 2 == 1) {
                    for (int d = 2; d < max(r, c); d += 2)
                        if (go(i, j, d))
                            res = max(res, d + 1);
                } else {
                    for (int d = 3; d <= max(r, c); d += 2) {
                        if (go(i, j, d))
                            res = max(res, d + 1);
                    }
                }
            }
        if (res == -1) printf("Case #%d: IMPOSSIBLE\n", testId);
        else printf("Case #%d: %d\n", testId, res);
    }
    return 0;
}

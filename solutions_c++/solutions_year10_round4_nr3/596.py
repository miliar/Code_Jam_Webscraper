#include <cmath>
#include <cstdio>
#include <map>
#include <vector>

#define MAXN 200

using namespace std;

int test, tests;
bool a[2][MAXN][MAXN];

void solve() {
    int c;
    scanf("%d", &c);

    for (int r = 0; r < MAXN; r++)
        for (int c = 0; c < MAXN; c++) {
            a[0][r][c] = false;
            a[1][r][c] = false;
        }

    int r1, r2, c1, c2;
    for (int step = 0; step < c; step++) {
        scanf("%d%d%d%d", &c1, &r1, &c2, &r2);
        for (int r = r1; r <= r2; r++)
            for (int c = c1; c <= c2; c++)
                a[0][r][c] = true;
    }

    int prev = 0;
    int next = 1;
    int cnt = 0;
    bool flag = true;
    while (flag) {
        flag = false;
        cnt++;

        for (int r = 1; r < MAXN; r++)
            for (int c = 1; c < MAXN; c++) {
                if (a[prev][r][c]) {
                    if (a[prev][r - 1][c] || a[prev][r][c - 1]) {
                        flag = true;
                        a[next][r][c] = true;
                    }
                }
                else {
                    if (a[prev][r - 1][c] && a[prev][r][c - 1]) {
                        flag = true;
                        a[next][r][c] = true;
                    }
                }
            }

        prev = 1 - prev;
        next = 1 - next;
        for (int r = 0; r < MAXN; r++)
            for (int c = 0; c < MAXN; c++)
                a[next][r][c] = false;
    }

    printf("Case #%d: %d\n", test, cnt);
}

int main() {
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}

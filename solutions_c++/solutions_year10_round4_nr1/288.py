#include <cmath>
#include <cstdio>
#include <map>
#include <vector>

#define MAXN 1000

using namespace std;

int test, tests;

int K;
int a[MAXN][MAXN];
bool r[2*MAXN];
bool l[2*MAXN];

void read() {
    scanf("%d", &K);

    int i = 0;
    int j = 0;
    for (int step = 0; step < K * K; step++) {
        scanf("%d", &a[i][j]);
        i = i - 1;
        j = j + 1;
        if (i < 0 || j >= K) {
            if (i + j < K - 1) {
                i = i + j + 1;
                j = 0;
            }
            else {
                j = i + j + 1 - K + 1;
                i = K - 1;
            }
        }
    }
}

bool in(int i, int j) {
    return i >= 0 && i < K && j >= 0 && j < K;
}

void init() {
    // right
    for (int d = 1 - K; d <= K - 1; d++) {
        r[d + K - 1] = true;
        for (int i = 0; i < K; i++)
            for (int j = 0; j < K; j++) {
                if (i - j <= d)
                    continue;
                int i2 = j + d;
                int j2 = i - d;
                if (!in(i2, j2))
                    continue;
                if (a[i][j] != a[i2][j2])
                    r[d + K - 1] = false;
            }
    }

    // left
    for (int d = 0; d < 2 * K - 1; d++) {
        l[d] = true;
        for (int i = 0; i < K; i++)
            for (int j = 0; j < K; j++) {
                if (i + j <= d)
                    continue;
                int i2 = d - j;
                int j2 = d - i;
                if (!in(i2, j2))
                    continue;
                if (a[i][j] != a[i2][j2])
                    l[d] = false;
            }
    }
}

void solve() {
    read();
    init();
    for (int res = K; res < MAXN; res++)
        for (int i = 0; i + K <= res; i++)
            for (int j = 0; j + K <= res; j++) {
                int xl = res - 1 - i - j;
                if (xl >= 0 && xl < 2 * K - 1 && !l[xl])
                    continue;
                int xr = 0 - (i - (j + K - 1));
                if (xr >= 0 && xr < 2 * K - 1 && !r[xr])
                    continue;
                printf("Case #%d: %d\n", test, res * res - K * K);
                return;
            }

}

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}

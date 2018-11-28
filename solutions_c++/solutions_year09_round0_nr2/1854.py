#include <cstdio>
#include <memory>

int a[110][110];
const int r[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int f[20000];
char v[20000];

int find(int p) {
    int t = p;
    while (f[t] != t) {
        t = f[t];
    }
    while (p != t) {
        int fp = f[p];
        f[p] = t;
        p = f[p];
    }
    return t;
}

void solve() {
    int H, W;
    scanf("%d %d", &H, &W);
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) {
            scanf("%d", &a[i][j]);
            f[i * 100 + j] = i * 100 + j;
        }
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) {
            int tx, ty, rx, ry, sum;
            sum = a[i][j];
            for (int s = 0; s < 4; s++) {
                tx = i + r[s][0];
                ty = j + r[s][1];
                if (tx >= 0 && tx < H && ty >= 0 && ty < W) {
                    if (a[tx][ty] < sum) {
                        sum = a[tx][ty];
                        rx = tx;
                        ry = ty;
                    }
                }
            }
            if (sum < a[i][j]) {
                f[find(i * 100 + j)] = find(rx * 100 + ry);
            }
        }
    memset(v, 0, sizeof v);
    char ans = 'a';
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (v[f[find(i * 100 + j)]] == 0) {
                v[f[find(i * 100 + j)]] = ans;
                ans++;
            }
            if (j > 0) printf(" ");
            printf("%c", v[f[find(i * 100 + j)]]);
        }
        printf("\n");
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d:\n", i + 1);
        solve();
    }
    return 0;
}

#include <cstdio>
#include <cstring>

const int Del = 1 << 8;
const int maxn = 100 + 5;

int f[maxn][300];
int all[maxn];
int D, I, M, n;

void checkmin(int& x, int y) {
    if(x == -1 || y < x) x = y;
}
int myabs(int x) {
    return ((x > 0) ? x : -x);
}
int calc(int dist, int M) {
    if(dist == 0) return 0;

    return ((dist - 1) / M) * I;
}
int main() {
    freopen("B-large.in", "r", stdin);
    int T, test = 1;

    for(scanf("%d", &T); T; T --) {
        scanf("%d%d%d%d", &D, &I, &M, &n);
        for(int i = 0; i < n; i ++)
            scanf("%d", &all[i]);

        memset(f, -1, sizeof(f));
        for(int i = 0; i < 1 << 8; i ++)
            f[0][i] = myabs(all[0] - i);
        f[0][Del] = D;
        for(int i = 1; i < n; i ++) {
            if(f[i - 1][Del] != -1)
                checkmin(f[i][all[i]], f[i - 1][Del]);
            // insert && modify
            for(int j = 0; j < 1 << 8; j ++) if(f[i - 1][j] != -1)
                for(int k = 0; k < 1 << 8; k ++)
                    if(M || j == k)
                        checkmin(f[i][k], f[i - 1][j] + calc(myabs(j - k), M) + myabs(all[i] - k));

            if(f[i - 1][Del] != -1)
                for(int j = 0; j < 1 << 8; j ++)
                    checkmin(f[i][j], f[i - 1][Del] + myabs(j - all[i]));
            // delete
            for(int j = 0; j <= 1 << 8; j ++) if(f[i - 1][j] != -1)
                checkmin(f[i][j], f[i - 1][j] + D);
        }

        int ans = -1;
        for(int i = 0; i <= 1 << 8; i ++) if(f[n - 1][i] != -1) checkmin(ans, f[n - 1][i]);

        printf("Case #%d: %d\n", test ++, ans);
    }

    return 0;
}


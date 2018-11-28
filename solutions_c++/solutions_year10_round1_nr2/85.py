#include <cstdio>
#include <cstring>

using namespace std;

int opt[110][256], a[110], done[300];
int cT, cN, del, ins, m, n, i, c, min, u, ans;

inline int abs(int x) {
    if (x < 0) return -x;
    else return x;
}

inline void update(int& oldVal, int newVal) {
    if (newVal < oldVal) oldVal = newVal;
}

int main() {
    scanf("%d", &cN);
    for (cT = 1; cT <= cN; ++cT) {
        scanf("%d%d%d%d", &del, &ins, &m, &n);
        for (i = 0; i < n; ++i) scanf("%d", &a[i+1]);
        memset(opt, 1, sizeof(opt));
        for (c = 0; c < 256; ++c) opt[0][c] = 0;
        for (i = 1; i <= n; ++i) {
            for (c = 0; c < 256; ++c)
                update(opt[i][c], opt[i-1][c] + del);
            for (c = 0; c < 256; ++c)
            for (u = 0; u < 256; ++u)
                if (abs(u - c) <= m) update(opt[i][c], opt[i-1][u] + abs(c - a[i]));
            memset(done, 0, sizeof(done));
            while (true) {
                min = 100000;
                u = -1;
                for (c = 0; c < 256; ++c) if (!done[c] && opt[i][c] < min) {
                    min = opt[i][c];
                    u = c;
                }
                if (u == -1) break;
                done[u] = 1;
                for (c = 0; c < 256; ++c) if (abs(u - c) <= m) update(opt[i][c], opt[i][u] + ins);
            }
        }
        ans = 100000;
        for (c = 0; c < 256; ++c) update(ans, opt[n][c]);
        printf("Case #%d: %d\n", cT, ans);
    }
}

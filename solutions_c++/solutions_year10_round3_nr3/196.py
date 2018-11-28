#include <cstdio>
#include <cstring>
#include <algorithm>
using std::min;

#define maxn 1024 
char maze[maxn][maxn];
char str[maxn];
int count[maxn];
int C = 90;
bool judge(int x, int y, int l) {
    if (l <= C) {
        for (int i = 0; i < l; ++i) {
            for (int j = 0; j < l; ++j) {
                if (maze[x + i][y + j] == -1) return false;
                if ((i + j) & 1) {
                    if (maze[x + i][y + j] == maze[x][y]) return false;
                } else {
                    if (maze[x + i][y + j] != maze[x][y]) return false; 
                }
            } 
        }
    } else {
        bool ret = judge(x, y, C);
        if (!ret) return ret;
        ret = judge(x + l - C, y + l - C, C);
        if (!ret) return ret;
        ret = judge(x + l - C, y, C);
        if (!ret) return ret;
        ret = judge(x, y + l - C, C);
        if (!ret) return ret;
    }
    return true;
}
int main() {
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
        memset(count, 0, sizeof(count));
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", str);
            int x = 0;
            for (int j = 0; str[j]; ++j) {
                int p = str[j] - '0';
                if (str[j] >= 'A' && str[j] <= 'F') p = str[j] - 'A' + 10;
                for (int k = 3; k >= 0; --k) {
                    if (p & (1 << k)) maze[i][x++] = 1;
                    else maze[i][x++] = 0;
                }
            }
        }
        int left = n * m;
        int ans = 0;
        int last_try = -1;
        while (left > 0) {
            int lo = 1, hi = min(n, m);
            if (last_try != -1) hi = last_try;
            int pl;
            while (lo <= hi) {
                int l = (lo + hi) >> 1;
                bool ok = false;
                for (int i = 0; !ok && i + l <= n; ++i) {
                    for (int j = 0; !ok && j + l <= m; ++j) {
                        if (maze[i][j] != -1 && judge(i, j, l)) {
                            ok = true;
                        }
                    }
                }
                if (ok) {
                    lo = l + 1;
                    pl = l;
                } else hi = l - 1;
            }
            for (int i = 0; i + pl <= n; ++i) {
                for (int j = 0; j + pl <= m; ++j) {
                    if (maze[i][j] != -1 && judge(i, j, pl)) {
                        left -= pl * pl;
                        count[pl]++;
                        if (count[pl] == 1) ans++;
                        for (int x = 0; x < pl; ++x) {
                            for (int y = 0; y < pl; ++y) {
                                maze[i + x][j + y] = -1;
                            }
                        }
                    }
                }
            }
            last_try = pl;
            //printf("%d\n", pl);
        }
        fprintf(stderr, "%d\n",kase);
        printf("Case #%d: %d\n", kase, ans);
        for (int i = min(n, m); i >= 1; --i) {
            if (count[i] != 0) {
                printf("%d %d\n", i, count[i]);
            }
        }
    }
    return 0;
}

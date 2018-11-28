#define MAXN 60

#include <cstdio>
#include <cstring>

int n, m;
char bor[MAXN][MAXN];

bool canTran(int x, int y) {
    if (x >= n - 1 || y >= m - 1) {
        return false;
    }
    if (bor[x + 1][y] != '#' || bor[x][y + 1] != '#' || bor[x + 1][y + 1] != '#') {
        return false;
    }
    bor[x][y] = bor[x + 1][y + 1] = '/';
    bor[x][y + 1] = bor[x + 1][y] = '\\';
    return true;
}

int main() {
    int t, cas, i, j;
    bool tag;

//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for (cas = 1; cas <= t; cas++) {
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) {
            scanf("%s", bor[i]);
        }

        tag = true;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                if (bor[i][j] == '#' && !canTran(i, j)) {
                    tag = false;
                    break;
                }
            }
        }

        printf("Case #%d:\n", cas);
        if (tag) {
            for (i = 0; i < n; i++) {
                printf("%s\n", bor[i]);
            }
        }
        else {
            printf("Impossible\n");
        }
    }

    return 0;
}

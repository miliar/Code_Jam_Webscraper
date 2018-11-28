#include <stdio.h>
#include <string.h>

int a[110][110], mrk[110][110], n, m;
int dx[4] = {-1, 0, 0, 1}, dy[4] = {0, -1, 1, 0};
char id[110];

int dfs(int x, int y) {
    if (mrk[x][y]) {
        return mrk[x][y];
    }
    int nx, ny, bk, minn = 0x3fffffff;
    int k;
    for (k = 0; k < 4; ++k) {
        nx = x + dx[k];
        ny = y + dy[k];
        if (nx < 0 || nx >=n || ny < 0 || ny>=m) {
            continue;
        }
        if (a[nx][ny] < minn) {
            minn = a[nx][ny];
            bk = k;
        }
    }
    nx = x + dx[bk];
    ny = y + dy[bk];
    mrk[x][y] = dfs(nx, ny);
    return mrk[x][y];
}

int main() {
    int ca, i, j, k, idn;
    int cases = 0;
    scanf("%d", &ca);
    while (ca--) {
        scanf("%d%d", &n, &m);
        for (i=0;i<n;++i) {
            for (j = 0; j < m; ++j) {
                scanf("%d", &a[i][j]);
            }
        }
        idn = 0;
        memset(mrk, 0, sizeof(mrk));
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                for (k = 0; k < 4; ++k) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (nx < 0 || nx >=n || ny < 0 || ny>=m) {
                        continue;
                    }
                    if (a[nx][ny] < a[i][j]) {
                        break;
                    }
                }
                if (k >= 4) {
                    mrk[i][j] = ++idn;
                }
            }
        }
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (!mrk[i][j]) {
                    mrk[i][j] = dfs(i, j);
                }
            }
        }
        memset(id, 0, sizeof(id));
        char c = 'a';
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (!id[mrk[i][j]]) {
                    id[mrk[i][j]] = c++;
                }
            }
        }

        printf("Case #%d:\n", ++cases);
        for (i = 0; i < n; ++i) {
            printf("%c", id[mrk[i][0]]);
            for (j = 1; j < m; ++j) {
                printf(" %c", id[mrk[i][j]]);
            }
            puts("");
        }

    }
    return 0;
}
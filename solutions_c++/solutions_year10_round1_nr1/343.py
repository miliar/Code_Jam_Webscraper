#include <cstdio>
#include <cstring>

#define N 105

char s[N][N], a[N][N];
bool vis[N][N];
int n, m;

void down(int x, int y) {
    int i;
    for (i = x; i < n; ++i)
        if (s[i][y] != '.')
            break;
    s[i - 1][y] = a[x][y];
}

bool red, blue;

void ch(int x, int y) {
    int cnt = 1, i, j;
    for (j = y + 1; j < n && s[x][j] == s[x][y]; ++j)
        ++cnt;
    if (cnt >= m) {
        if (s[x][y] == 'R') red = 1;
        if (s[x][y] == 'B') blue = 1;
    }

    cnt = 1;
    for (i = x + 1; i < n && s[i][y] == s[x][y]; ++i)
        ++cnt;
    if (cnt >= m) {
        if (s[x][y] == 'R') red = 1;
        if (s[x][y] == 'B') blue = 1;
    }

    cnt = 1;
    for (i = x + 1, j = y + 1; i < n && j < n && s[i][j] == s[x][y]; ++i, ++j)
        ++cnt;
    if (cnt >= m) {
        if (s[x][y] == 'R') red = 1;
        if (s[x][y] == 'B') blue = 1;
    }

    cnt = 1;
    for (i = x + 1, j = y - 1; i < n && j >= 0 && s[i][j] == s[x][y]; ++i, --j)
        ++cnt;
    if (cnt >= m) {
        if (s[x][y] == 'R') red = 1;
        if (s[x][y] == 'B') blue = 1;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, i, j, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; ++i)
            scanf("%s", s[i]);
        for (i = 0; i < n; ++i)
            for (j = 0; j < n; ++j)
                a[j][n - 1 - i] = s[i][j];
//        puts("");
//        for (i = 0; i < n; ++i) {
//            a[i][n] = 0;
//            puts(a[i]);
//        }
        for (i = 0; i < n; ++i)
            for (j = 0; j < n; ++j)
                s[i][j] = '.';
        memset(vis, 0, sizeof(vis));
        for (i = n - 1; i >= 0; --i)
            for (j = 0; j < n; ++j)
                if (!vis[i][j]) {
                    vis[i][j] = 1;
                    down(i, j);
                }
//        puts("");
//        for (i = 0; i < n; ++i)
//            puts(s[i]);
        red = blue = 0;
        for (i = 0; i < n; ++i)
            for (j = 0; j < n; ++j)
                if (s[i][j] != '.') {
                    ch(i, j);
                    if (red && blue)
                        break;
                }
        printf("Case #%d: ", ++cas);
        if (red && blue)
            puts("Both");
        else if (red)
            puts("Red");
        else if (blue)
            puts("Blue");
        else
            puts("Neither");
    }
    return 0;
}

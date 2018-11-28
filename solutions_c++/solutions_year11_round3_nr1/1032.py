#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int n, m;
bool ok(int x, int y) {
    if (x >= 0 && x < n && y >= 0 && y < m) return 1;
    return 0;
}

int main() {
    freopen("11.in", "r", stdin);
    freopen("11.out", "w", stdout);
    int t, tt, i, j;
    char str[51][51];
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++) {
        printf("Case #%d:\n", tt);
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) scanf("%s", str[i]);
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++) {
                if (str[i][j] == '#' &&
                    str[i][j + 1] == '#' &&
                    str[i + 1][j] == '#' &&
                    str[i + 1][j + 1] == '#'
                ) {
                    str[i][j] = '/';
                    str[i][j + 1] = '\\';
                    str[i + 1][j] = '\\';
                    str[i + 1][j + 1] = '/';
                }
            }
        bool flag = 0;
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                if (str[i][j] == '#') flag = 1;
        if (flag) printf("Impossible\n");
        else for (i = 0; i < n; i++) printf("%s\n", str[i]);
    }
    return 0;
}

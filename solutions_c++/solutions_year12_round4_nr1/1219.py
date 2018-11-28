#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <vector>
#include <stdlib.h>
#define MAX_N 10005
using namespace std;

int n, d[MAX_N], l[MAX_N];
bool vis[MAX_N][MAX_N];
int D;

bool dfs(int a, int b) {
    int s = abs(d[a] - d[b]);
    s = min(l[a], s);
    if (d[a] + s >= D) return 1;
    for (int i = a + 1; i <= n; i++) {
        int tmp = abs(d[a] - d[i]);
        if (tmp <= s) {
            if (!vis[i][a]) {
                vis[i][a] = 1;
                if (dfs(i, a)) return 1;
            }
        } else break;
    }
    for (int i = a - 1; i > 0; i--) {
        int tmp = abs(d[a] - d[i]);
        if (tmp <= s) {
            if (!vis[i][a]) {
                vis[i][a] = 1;
                if (dfs(i, a)) return 1;
            }
        } else break;
    }
    return 0;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int icase, tt = 0, i;
    scanf("%d", &icase);
    while (icase--) {
        memset(vis, 0, sizeof(vis));
        scanf("%d", &n);
        for (i = 1; i <= n; i++)
            scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &D);
        bool flag = dfs(1, 0);
        printf("Case #%d: %s\n", ++tt, flag ? "YES" : "NO");
    }
    return 0;
}

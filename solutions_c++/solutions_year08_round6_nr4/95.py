#include<stdio.h>
#include<string>
int edge[10][2];
int g[10][10];
int opt[10];
bool used[10];
int n, m;
inline bool useall() {
    for (int i = 1; i <= m; i++) {
        if (!used[i]) {
            return 0;
        }
    }
    return 1;
}
int dfs(int p) {
    if (useall()) {
        for (int i = 1; i < m; i++) {
            int u = opt[edge[i][0]];
            int v = opt[edge[i][1]];
            if (u && v && g[u][v] == 0) {
                return 0;
            }
        }
        
        return 1;
    }
    if (p > n) {
        return 0;
    }
    if (dfs(p + 1)) {
        return 1;
    }
    for (int i = 1; i <= m; i++) {
        if (!used[i]) {
            opt[i] = p;
            used[i] = 1;
            if (dfs(p + 1)) {
                return 1;
            }
            opt[i] = 0;
            used[i] = 0;
        }
    }
    return 0;
}
int main() {
    //freopen("d.in", "r", stdin);
    //freopen("d.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int casen = 1; casen <= T; casen++) {
        scanf("%d", &n);
        memset(g, 0, sizeof(g));
        for (int i = 1; i < n; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            g[u][v] = g[v][u] = 1;
            
        }
        
        scanf("%d", &m);

        for (int i = 1; i < m; i++) {
            scanf("%d%d", &edge[i][0], &edge[i][1]);            
        }
        printf("Case #%d: ", casen);
        memset(used, 0, sizeof(used));
        memset(opt, 0, sizeof(opt));
        if (dfs(1)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}


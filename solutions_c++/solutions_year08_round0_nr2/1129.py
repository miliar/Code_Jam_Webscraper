#include <stdio.h>
#include <string.h>

const int Max = 200;

int conn[Max][Max];
int n, m, T, vis[Max], my[Max];
int start[Max], end[Max];

int parse(char buf[]) {
    return ((buf[0]-'0')*10 + buf[1]-'0')*60 + (buf[3]-'0')*10 + buf[4]-'0';
}

void input() {
    scanf("%d%d%d", &T, &n, &m);
    char buf[32];
    for(int i = 0;i < n;i ++) {
        scanf("%s", buf);
        start[i] = parse(buf);
        scanf("%s", buf);
        end[i] = parse(buf);
    }
    memset(conn, 0, sizeof(conn));
    for(int i = 0;i < m;i ++) {
        scanf("%s", buf);
        int tmp = parse(buf);
        for(int j = 0;j < n;j ++) if(tmp >= end[j] + T) conn[j][n+i] = 1;
        scanf("%s", buf);
        tmp = parse(buf);
        for(int j = 0;j < n;j ++) if(start[j] >= tmp + T) conn[n+i][j] = 1;
    }
}

int path(int u) {
    if(vis[u]) return 0;
    vis[u] = 1;
    for(int v = 0;v < n+m;v ++) {
        if(!conn[u][v]) continue;
        if(my[v] == -1||path(my[v])) {
            my[v] = u;
            return 1;
        }
    }
    return 0;
}

void solve() {
    int res = 0;
    memset(my, -1, sizeof(my));
    for(int i = 0;i < n+m;i ++) {
        memset(vis, 0, sizeof(vis));
        if(path(i)) res ++;
    }
    int A = 0, B = 0;
    for(int i = 0;i < n;i ++) if(my[i] == -1) A ++;
    for(int i = n;i < n+m;i ++) if(my[i] == -1) B ++;
    //if(A + res != n||B + res != m) printf("WA\n");
    printf("%d %d\n", A, B);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: ", cas);
        solve();
    }
    getchar(); getchar();
    return 0;
}

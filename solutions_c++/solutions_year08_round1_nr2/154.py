#include <cstdio>
#include <cstring>
#include <algorithm>

const int Max = 2000;

int n, m, unmalted[Max], malted[Max];
char conn[Max][Max], choose[Max];

void input() {
    scanf("%d%d", &n, &m);
    memset(conn, 0, sizeof(conn));
    memset(choose, 0, sizeof(choose));
    for(int i = 0;i < m;i ++) {
        int tmp;
        malted[i] = -1;
        scanf("%d", &tmp);
        for(int j = 0;j < tmp;j ++) {
            int a, b;
            scanf("%d%d", &a, &b);
            -- a;
            if(b == 0) conn[i][a] = 1;
            else {
                malted[i] = a;
                tmp --;
                j --;
            }
        }
        unmalted[i] = tmp;
    }
}

void solve() {
    while(1) {
        int id = -1, changed = 0;
        for(int i = 0;i < m;i ++) if(unmalted[i] == 0) {
            if(malted[i] == -1) {
                printf("IMPOSSIBLE\n");
                return ;
            }
            int id = malted[i];
            if(choose[id]) continue;
            changed = 1;
            choose[id] = 1;
            for(int j = 0;j < m;j ++) if(conn[j][id]) unmalted[j] --;
        }
        if(changed == 0) break;
    }
    for(int i = 0;i < n;i ++) {
        if(i) printf(" ");
        if(choose[i]) printf("1");
        else printf("0");
    }
    printf("\n");
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

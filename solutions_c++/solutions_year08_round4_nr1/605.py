#include <stdio.h>
#include <string.h>

const int Max = 10000+10;

int n, v;
int gate[Max], changeable[Max], dp[Max][2];

void input() {
    scanf("%d%d", &n, &v);
    for(int i = 0;i < n/2;i ++) scanf("%d%d", &gate[i], &changeable[i]);
    for(int i = n/2;i < n;i ++) scanf("%d", &gate[i]);
    for(int i = 0;i < n;i ++) dp[i][0] = dp[i][1] = Max;
}

void search(int v) {
    if(v >= n/2) {
        dp[v][gate[v]] = 0;
        return ;
    }
    search(v*2+1);
    search(v*2+2);
    for(int i = 0;i < 2;i ++) for(int j = 0;j < 2;j ++) if(dp[v*2+1][i] < Max&&dp[v*2+2][j] < Max) {
        int v1 = i|j, v2 = i&j, v3 = dp[v*2+1][i] + dp[v*2+2][j];
        if(gate[v] == 0) {
            if(v3 < dp[v][v1]) dp[v][v1] = v3;
            if(changeable[v]&&v3+1 < dp[v][v2]) dp[v][v2] = v3 + 1;
        }
        else {
            if(v3 < dp[v][v2]) dp[v][v2] = v3;
            if(changeable[v]&&v3+1 < dp[v][v1]) dp[v][v1] = v3 + 1;
        }
    }
}

void solve() {
    search(0);
    if(dp[0][v] < Max) printf("%d\n", dp[0][v]);
    else printf("IMPOSSIBLE\n");
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
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

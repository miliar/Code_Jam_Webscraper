#include <stdio.h>
#include <string.h>

void input();
void solve();

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    
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

const int Max = 100;
int dp[Max][Max], n, m;

void input() {
    int c;
    scanf("%d%d%d", &n, &m, &c);
    memset(dp, -1, sizeof(dp));
    for(int i = 0;i < c;i ++) {
        int x, y;
        scanf("%d%d", &x, &y);
        dp[x-1][y-1] = 0;
    }
    dp[n-1][m-1] = 1;
}

void solve() {
    for(int i = n-1;i >= 0;i --) for(int j = m-1;j >= 0;j --) {
        if(dp[i][j] != -1) continue;
        dp[i][j] = 0;
        if(i+2 < n&&j+1 < m) dp[i][j] = (dp[i][j] + dp[i+2][j+1])%10007;
        if(i+1 < n&&j+2 < m) dp[i][j] = (dp[i][j] + dp[i+1][j+2])%10007;
    }
    printf("%d\n", dp[0][0]);
}

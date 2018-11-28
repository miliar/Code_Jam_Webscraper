#include <stdio.h>
#include <string.h>

const int Max = 100;
const int MaxN = 1000;

char dic[Max][120];
int n, m, id[MaxN];
int dp[MaxN][Max];

void input() {
    char buf[120];
    scanf("%d", &m);
    gets(buf);
    for(int i = 0;i < m;i ++) gets(dic[i]);
    scanf("%d", &n);
    gets(buf);
    for(int i = 0;i < n;i ++) {
        gets(buf);
        for(int j = 0;j < m;j ++) if(strcmp(dic[j], buf) == 0) id[i] = j;
    }
}

int solve() {
    for(int j = 0;j < m;j ++) dp[0][j] = 0;
    dp[0][id[0]] = n;
    for(int i = 1;i < n;i ++) for(int j = 0;j < m;j ++) {
        dp[i][j] = n;
        if(id[i] == j) continue;
        for(int k = 0;k < m;k ++) if(k != j&&dp[i-1][k] + 1 < dp[i][j]) dp[i][j] = dp[i-1][k] + 1;
        if(dp[i-1][j] < dp[i][j]) dp[i][j] = dp[i-1][j];
    }
    int res = n;
    for(int j = 0;j < m;j ++) if(dp[n-1][j] < res) res = dp[n-1][j];
    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: %d\n", cas, solve());
    }
    return 0;
}

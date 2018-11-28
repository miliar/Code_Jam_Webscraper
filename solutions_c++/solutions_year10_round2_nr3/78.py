#include <cstdio>
#include <cstring>

#define MOD 100003

int T,N,c[501][501],dp[501][501];

int C(int n, int m) {
    if(m == 0)
        return c[n][m] = 1;
    if(n == 0)
        return c[n][m] = 0;
    if(c[n][m] != -1)
        return c[n][m];
    return c[n][m] = (C(n-1,m) + C(n-1,m-1)) % MOD;
}

int main() {
    int i,j,k,cas=1;

    memset(c, 0xff, sizeof(c));
    for(i=1; i<=500; i++)
        for(j=1; j<=500; j++)
            C(i,j);
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &N);
        memset(dp, 0, sizeof(dp));
        for(i=1; i<=N; i++)
            dp[i][1] = 1;
        for(i=1; i<=N; i++)
            for(j=2; j<i; j++)
                for(k=1; k<j; k++)
                    dp[i][j] = (dp[i][j] + (long long)dp[j][k] * c[i-j-1][j-k-1]) % MOD;
        int ans=0;
        for(i=0; i<=N; i++)
            ans = (ans + dp[N][i]) % MOD;
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

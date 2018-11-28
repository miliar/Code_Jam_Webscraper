#include<stdio.h>

int T;

int C[510][510], MAX = 505, MOD = 100003;

void get_C()
{
    C[1][0] = 1; C[1][1] = 1; C[0][0] = 1;
    int i, j;
    for(i = 2; i < MAX; i ++)
    {
        C[i][0] = 1;
        C[i][i] = 1;
        for(j = 1; j < i; j ++)
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD;
    }
}

int prod(int a, int b)
{
    if(b < 10000 || a < 10000)
        return  (a * b) % MOD;
    
    if(b % 2 == 1)
        return (prod(a, b / 2) * 2 + a) % MOD;
    else
        return (prod(a, b / 2) * 2) % MOD;
}


int dp[510][510];
bool used[510][510];

int dfs(int n, int m)
{
    if(m == 1)
        return 1;
    if(used[n][m])
        return dp[n][m];
    used[n][m] = true;
    if(n == 2)
    {
        if(m == 1)
            dp[n][m] = 1;
        else
            dp[n][m] = 0;
        return dp[n][m];
    }
    int i, min, ans = 0;
    min = 2 * m - n;
    if(min < 1)
        min = 1;
    for(i = min; i < m; i ++)
        ans = (ans + prod(dfs(m, i), C[n - m - 1][m - i - 1])) % MOD;
    dp[n][m] = ans;
    return ans;
}

int main()
{
    get_C();
    int i, n, ans, m, j;   
    for(i = 0; i < MAX; i ++)
        for(j = 0; j < MAX; j ++)
            used[i][j] = false;
    scanf("%d", &T);
    for(int test = 1; test <= T; test ++)
    {
        scanf("%d", &n);
        ans = 0;
        for(m = 1; m < n; m ++)
            ans += dfs(n, m);
        printf("Case #%d: %d\n", test, ans % MOD);
    }
    return 0;
}

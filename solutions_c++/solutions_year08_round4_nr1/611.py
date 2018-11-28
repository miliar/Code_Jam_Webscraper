#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int M, V;
int G[10010], C[10010];
int dp[10010][2];

int f(int a, int b, int op)
{
    if (op == 0) return a | b;
    return a & b;
}

void dfs(int x)
{
    if (C[x] == -1)
    {
        dp[x][G[x]] = 0;
        return ;
    }
    
    dfs(x * 2);
    dfs(x * 2 + 1);
    
    for (int i = 0; i <= 1; ++i)
        for (int j = 0; j <= 1; ++j)
        {
            int a = dp[x * 2][i];
            int b = dp[x * 2 + 1][j];
            if (a == -1 || b == -1) continue;
            int val = f(i, j, G[x]);
            if (dp[x][val] == -1 || dp[x][val] > a + b)
                dp[x][val] = a + b;
            
            if (C[x] == 1)
            {
                val = f(i, j, 1 - G[x]);
                if (dp[x][val] == -1 || dp[x][val] > a + b + 1)
                    dp[x][val] = a + b + 1;
            }
        }
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int test = 1; test <= N; ++test)
    {
        
        // input
        scanf("%d %d", &M, &V);
        for (int i = 1; i <= (M - 1) / 2; ++i)
            scanf("%d %d", G + i, C + i);
        for (int i = (M - 1) / 2 + 1; i <= M; ++i)
        {
            scanf("%d", G + i);
            C[i] = -1;
        }
        
        // solve
        memset(dp, -1, sizeof dp);
        dfs(1);
        if (dp[1][V] == -1)
            printf("Case #%d: IMPOSSIBLE\n", test);
        else
            printf("Case #%d: %d\n", test, dp[1][V]);
    }
	return 0;
}

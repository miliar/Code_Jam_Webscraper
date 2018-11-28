#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#define SIZE 256
#define INF 100000000

using namespace std;

int main()
{
    freopen("B-small.in", "r", stdin);
   freopen("B-small.out", "w", stdout);
    int C = 0, T;

    scanf("%d", &T);
    while (T--)
    {
        int D, I, M, N, a[SIZE];
        scanf("%d %d %d %d", &D, &I, &M, &N);
        for(int i = 0; i < N; i++)
            scanf("%d", &a[i]);
        int dp[SIZE / 2][SIZE][2];
        for(int i = 0; i < SIZE / 2; i++)
            for(int j = 0; j < SIZE; j++)
                    dp[i][j][0] = dp[i][j][1] = INF;
        for(int i = 0; i < SIZE; i++)
            dp[0][i][1] = abs(i - a[0]);
        for(int i = 1; i < N; i++)
        {
            for(int j = 0; j < SIZE; j++)
            {
                for(int k = 0; k < SIZE; k++)
                {
                    int tx = 0;
                    if(abs(j - k) > M)
                    {
                        if(M == 0)tx = INF;
                        else tx = I * ((abs(j - k) - 1) / M);

                    }
                    int t0 = dp[i - 1][k][0] + tx, t1 = dp[i - 1][k][1] + tx;
                    dp[i][j][1] = min(min(t0, t1) + abs(a[i] - j), dp[i][j][1]);
                }
                dp[i][j][1] = min(dp[i][j][1], i * D + abs(j - a[i]));
                dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j][1] + D);
            }
        }
        int res = INF;
        for(int i = 0; i < SIZE; i++)
            for(int j = 0; j < 2; j++)
                res = min(res, dp[N - 1][i][j]);
        printf("Case #%d: %d\n", ++C, res);
    }


    return 0;
}

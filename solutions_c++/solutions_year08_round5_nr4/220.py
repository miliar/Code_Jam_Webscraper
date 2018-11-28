#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[110][110];
bool rock[110][110];

int main()
{
    int N;
    scanf("%d", &N);
    
    for (int test = 1; test <= N; ++test)
    {
        memset(rock,0,sizeof rock);
        
        int H, W, R;
        scanf("%d %d %d", &H, &W, &R);
        
        for (int i = 0; i < R; ++i)
        {
            int r, c;
            scanf("%d %d", &r, &c);
            rock[c][r] = true;
        }
    
        memset(dp,0,sizeof dp);
        dp[1][1] = 1;
        
        for (int i = 1; i <= W; ++i)
            for (int j = 1; j <= H; ++j)
            {
                if (dp[i][j] == 0) continue;
                
                int move[2][2] = {{2,1},{1,2}};
                for (int k = 0; k < 2; ++k)
                {
                    int ni = i + move[k][0];
                    int nj = j + move[k][1];
                    
                    if (ni <= W && nj <= H && !rock[ni][nj])
                        dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % 10007;
                }
            }
        
        printf("Case #%d: %d\n", test, dp[W][H]);
    }
	return 0;
}

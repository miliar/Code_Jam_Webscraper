#include<iostream>
using namespace std;

int map[101][101];
int dp[101][101];

int main(){
    int r, h, w;
    int cnt;
    scanf("%d", &cnt);
    for (int t = 1; t <= cnt; t++){
        memset(map, 0, sizeof(map));
        memset(dp,0,sizeof(dp));
    scanf("%d%d%d", &h, &w, &r);
    int x, y;
    for (int i = 0; i < r; i++){
    scanf("%d%d", &x, &y);
    map[x][y] = 1;
    }
    dp[1][1] = 1;
    for (int i = 2; i <= h; i++)
        for (int j = 2; j <= w; j++)
            if (map[i][j])
               dp[i][j] = 0;
            else
                dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j - 2]) % 10007;
    printf("Case #%d: %d\n", t, dp[h][w] % 10007);
    }
}


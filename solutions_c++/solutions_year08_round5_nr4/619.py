#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

long long dp[101][101];
int stone[101][101];

int
main(void)
{
    int i, j;
    int x, y;
    int N, H, W, R;
    int r, c;

    cin >> N;

    for(i=1;i<=N;i++) {
        memset(dp, 0, sizeof(dp));
        memset(stone, 0, sizeof(stone));
        cin >> H >> W >> R;
        for(j=0;j<R;j++) {
            cin >> r >> c;
            stone[r][c] = 1;
        }
        dp[1][1] = 1;
        for(x=1;x<=100;x++) {
            for(y=1;y<=100;y++) {
                if (stone[x][y])
                    continue;
                if (x >= 2 && y >= 3) {
                    dp[x][y] += dp[x-1][y-2];
                }
                if (x >= 3 && y >= 2) {
                    dp[x][y] += dp[x-2][y-1];
                }
                dp[x][y] %= 10007;
            }
        }
      cout << "Case #" << i << ": " << dp[H][W] << endl;
    }
    
    return 0;
}

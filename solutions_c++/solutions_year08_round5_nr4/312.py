#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <string>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <memory.h>

using namespace std;

int const MOD = 10007;
int main()
{
    int N;
    cin >> N;
    for( int cs = 1; cs <= N; ++cs )
    {
        int h, w, r;
        cin >> h >> w >> r;

        vector<vector<int> > dp(h, vector<int>(w));
        dp[0][0] = 1;

        for( int i = 0; i != r; ++i )
        {
            int y, x;
            cin >> y >> x;
            dp[y-1][x-1] = -1;
        }

        int dx[] = { 2, 1 };
        int dy[] = { 1, 2 };
        for( int i = 0; i != h; ++i )
        for( int j = 0; j != w; ++j )
        if( dp[i][j] != -1 )
        for( int k = 0; k != 2; ++k )
        {
            int y = i + dy[k];
            int x = j + dx[k];
            if( y < h && x < w && dp[y][x] != -1 )
            {
                dp[y][x] += dp[i][j];
                dp[y][x] %= MOD;
            }
        }

        cout << "Case #" << cs << ": " << dp[h-1][w-1] << endl;
    }
    return 0;
}
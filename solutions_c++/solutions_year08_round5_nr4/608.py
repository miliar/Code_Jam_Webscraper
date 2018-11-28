#include <iostream>
#include <cstring>

using namespace std;

const int MOD = 10007;
int dp[128][128];
int special[128][128];

int main()
{
	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		int H, W, R;
		cin >> H >> W >> R;
		memset(special, 0, sizeof(special));
		for (int i = 0; i < R; i++)
		{
			int x, y;
			cin >> x >> y;
			special[x][y] = 1;
		}
		dp[1][1] = 1;
		for (int i = 1; i <= H; i++)
			for (int j = 1; j <= W; j++)
				if (i != 1 || j != 1)
				{
					dp[i][j] = 0;
					if (i > 2 && j > 1)
						dp[i][j] += dp[i-2][j-1];
					if (i > 1 && j > 2)
						dp[i][j] += dp[i-1][j-2];
					if (special[i][j])
						dp[i][j] = 0;
					dp[i][j] %= MOD;
				}
		cout << "Case #" << ++kase << ": " << dp[H][W] << endl;
	}
	return 0;
}

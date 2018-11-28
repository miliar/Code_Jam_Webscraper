#include <iostream>
#include <cstdio>

int abs(int a) { return a < 0 ? -a : a; }

using namespace std;

int dp[111][256] = {0};

int main()
{
	int T; cin >> T;
	for (int tcase = 0; tcase < T; tcase++)
	{
		int D, I, M, N; cin >> D >> I >> M >> N;	
		int a[101];
		for (int i = 0; i < N; i++) cin >> a[i];
	
		for (int i = 1; i <= N; i++)
    {
			for (int j = 0; j < 256; j++)
			{
				dp[i][j] = D + dp[i-1][j];
				for (int k = 0; k < 256; k++)
					if (abs(k-j) <= M)
						dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(a[i-1]-j));
			}
			
			if (M != 0)
			{
				for (int j = 0; j < 256; j++)
					for (int k = 0; k < j; k++)
					{
						int cost = (j-k+M-1)/M * I;
						dp[i][j] = min(dp[i][j], dp[i][k] + cost);
					}
					
				for (int j = 255; j >= 0; j--)
					for (int k = j+1; k < 256; k++)
					{
						int cost = (k-j+M-1)/M * I;
						dp[i][j] = min(dp[i][j], dp[i][k] + cost);
					}
			}
		}

		int ans = 1e9;
		for (int j = 0; j < 256; j++)
			ans = min(ans, dp[N][j]);
		printf("Case #%d: %d\n", tcase+1, ans);
	}
	
	return 0;
}

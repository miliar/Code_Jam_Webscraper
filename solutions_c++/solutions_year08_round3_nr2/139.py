#include <iostream>
#include <string>

using namespace std;

char num[50];
long long dp[50][210];

int prime[4] = {2, 3, 5, 7};

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		scanf("%s", num);
		memset(dp, 0, 50 * 210 * 4);
		int n = strlen(num);
		for(int i = 0; i < 4; ++i) dp[0][0] = 1;
		for(int i = 0; num[i]; ++i)
		{
			for(int j = 0; j <= i; ++j)
			{
				int mod = 0;
				for(int l = j; l <= i; ++l) mod = (mod * 10 + (num[l] - '0')) % 210;
				for(int l = 0; l < 210; ++l) if(dp[j][l])
				{
					dp[i + 1][(mod + l) % 210] += dp[j][l];
					if(j != 0) dp[i + 1][(l - mod + 210) % 210] += dp[j][l];
				}
			}
		}
		long long res = 0;
		for(int i = 0; i < 210; ++i) if(i % 2 == 0 || i % 3 == 0 || i % 7 == 0 || i % 5 == 0) res += dp[n][i];
		cout << "Case #" << tt << ": " << res << endl;
	}
	return 0;
}
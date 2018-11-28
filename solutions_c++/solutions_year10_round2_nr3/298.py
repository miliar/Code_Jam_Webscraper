#include <iostream>

using namespace std;

const int MOD = 100003;

int binom[512][512];
int dp[512][512];

int main()
{
	for (int n = 0; n <= 500; n++)
	{
		binom[n][0] = binom[n][n] = 1;
		for (int k = 1; k < n; k++)
			binom[n][k] = (binom[n-1][k-1] + binom[n-1][k]) % MOD;
	}
	for (int n = 2; n <= 500; n++)
	{
		dp[n][1] = 1;
		for (int k = 2; k <= n-1; k++)
		{
			dp[n][k] = 0;
			for (int j = 1; j <= k-1; j++)
				dp[n][k] = (dp[n][k] + dp[k][j] * binom[n-1-k][k-j-1]) % MOD;
		}
	}
/*
	for (int n = 2; n <= 6; n++)
	{
		cout << "n=" << n << ": ";
		for (int k = 1; k <= n-1; k++)
			cout << dp[n][k] << " ";
		cout << endl;
	}
	return 0;
*/

	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		int n, res = 0;
		cin >> n;
		for (int k = 0; k <= n; k++)
			res = (res + dp[n][k]) % MOD;
		cout << "Case #" << ++kase << ": " << res << endl;
	}
	return 0;
}

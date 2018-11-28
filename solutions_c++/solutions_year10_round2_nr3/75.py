#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const long long MOD = 100003;



int n;
long long dp[601][601];
long long C[601][601];

void Load()
{
	cin >> n;

}


void GenC()
{
	int i, j;
	for (i = 0; i <= 540; i++)
	{
		C[i][0] = 1;
		for (j = 1; j <= i; j++)
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
	}
}

void Solve()
{
	memset(dp, 0, sizeof(dp));
	int i, j, k;
	for (i = 2; i <= n; i++) dp[1][i] = 1;

	for (i = 1; i < n; i++)
	{
		for (j = 2; j <= n; j++)
		{
			if (dp[i][j] == 0) continue;
			for (k =2*j-i; k <= n; k++)
				dp[j][k] = (dp[j][k] + dp[i][j] * C[k - j-1][j - i-1]) % MOD;
		}
	}

	long long ans = 0;
	for (i = 1; i < n; i++)
		ans = (ans + dp[i][n]) % MOD;
	cout << ans << "\n";
}

int main()
{
	int nt, tt;
	GenC();
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}

#include <iostream>
#include <cstdio>

#define MOD 1000000007

using namespace std;

int A[100];
int limit[500000];
int dp[1000][1010];

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;
		for(int i = 0; i < m; ++i) cin >> A[i];
		for(int i = 0; i < n; ++i)
		{
			limit[i] = A[i % m];
			A[i % m] = ((long long)x * A[i % m] + (long long)y * (i + 1)) % z;
		}
		long long res = 0;
		memset(dp, 0, 1000 * 1010 * 4);
		for(int i = 0; i < n; ++i)
		{
			dp[i][1] = 1;
			for(int j = 0; j < i; ++j) if(limit[j] < limit[i])
			{
				for(int k = 1; k <= n; ++k)
				{
					dp[i][k + 1] = (dp[i][k + 1] + (long long)dp[j][k]) % MOD;
				}
			}
		}
		for(int i = 0; i < n; ++i)
		{
			for(int k = 1; k <= n; ++k)
			{
				res = (res + dp[i][k]) % MOD;
			}
		}
		printf("Case #%d: %d\n", t, (int)res);
	}
	return 0;
}
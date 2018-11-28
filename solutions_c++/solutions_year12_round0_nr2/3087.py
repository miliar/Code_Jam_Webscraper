#include<iostream>
#include<memory.h>
#include<vector>

using namespace std;

int dp[111][111];

int solve()
{
	int N, S, p;
	cin >> N >> S >> p;

	vector<int> v(N);
	for(int i = 0; i < N; ++i)	cin >> v[i];

	memset(dp, 0, sizeof(dp));

	bool ok;
	int t;

	for(int i = 1; i <= N; ++i)
	{
		for(int j = 0; j <= S; ++j)	dp[i][j] = dp[i - 1][j];
		ok = false;

		// Surprising
		for(int a = 0; a <= 10; ++a)
		{
			t = v[i - 1] - 3 * a;

			if(t >= 2 && t <= 4 && a + 2 >= p)
			{
				ok = true;
				break;
			}
		}

		if(ok)	
			for(int j = 1; j <= N; ++j)	dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);

		ok = false;

		// Not surprising
		for(int a = 0; a <= 10; ++a)
		{
			t = v[i - 1] - 3 * a;

			if((t == 0 && a >= p) || (t == 1 && a + 1 >= p) || (t == 2 && a + 1 >= p))
			{
				ok = true;
				break;
			}
		}

		if(ok)
			for(int j = 0; j <= S; ++j)	dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1);
	}

	return dp[N][S];
}

int main()
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i)	cout << "Case #" << i << ": " << solve() << endl;
	
	return 0;
}

#include <iostream>
#include <cstdio>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
const int N = 100, A = 256, INF = 1000000100;

int ans, t, D, I, n,  M, T[N + 1], dp[A], last[A];

int best(int v, int b[])
{
	int res = b[v];
	for(int i = max(0, v - M); i <= min(A - 1, v + M); ++i)
		res = min(res, b[i]);
	return res;
}

int main()
{
	int i, j, k;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		memset(dp, 0, sizeof(dp));
		memset(last, 0, sizeof(last));
		cin >> D >> I >> M >> n;
		for(i = 0; i < n; ++i)
			cin >> T[i];
		for(i = 0; i < n; ++i)
		{
			for(j = 0; j < A; ++j)
				dp[j] = min(abs(T[i] - j) + best(j, last), last[j] + D);
			for(j = 0; j < A; ++j)
				dp[j] = min(dp[j], best(j, dp) + I);
			for(j = A - 1; j >= 0; --j)
				dp[j] = min(dp[j], best(j, dp) + I);
			for(j = 0; j < A; ++j)
				last[j] = dp[j];
		//	cout << i << endl;
		//	for(k = 0; k < A; ++k)
		//		cout << k << " " << dp[k] << endl;
		}
		ans = dp[0];
		for(i = 0; i < A; ++i)
			ans = min(ans, dp[i]);
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}

#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;

const int M = 100003;

int dp[510][510];
int c[510][510];

long long C(int n, int k)
{
	if(n == k)
		return 1;
	if(n < k)
		return 0;
	if(c[n][k] != -1)
		return c[n][k];
	return c[n][k] = (C(n - 1, k - 1) + C(n - 1, k)) % M;
}

long long Func(int n, int len)
{
	if(len == 1)
		return 1;
	if(dp[n][len] != -1)
		return dp[n][len];
	long long ans = 0;
	for(int i = 1; i < len; i++)
	{
		ans += Func(len, i) * C(n - len - 1, len - i - 1);
		ans %= M;
	}
	return dp[n][len] = ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	memset(dp, -1, sizeof(dp));
	memset(c, -1, sizeof(c));
	for(int i = 0; i <= 500; i++)
		c[i][0] = 1;
	//for(int i = 0; i <= 500; i++)
	//	for(int j = 0; j <= i; j++)
	//		C(i, j);
	//cout << Func(6, 3);
	for(int i = 2; i <= 500; i++)
		for(int j = 1; j < i; j++)
			Func(i, j);
	for(int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		int ans = 0;
		for(int i = 1; i < n; i++)
			ans = (ans + Func(n, i)) % M;
		printf("Case #%d: %d\n", tc + 1, ans);
	}
	return 0;
}
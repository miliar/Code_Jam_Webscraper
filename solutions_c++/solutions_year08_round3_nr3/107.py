#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>

#define tt 1000000007

using namespace std;


int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int u = 1; u <= r; u++)
	{
		long long n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;
		vector<long long> sp(n);
		vector<long long> a(m);
		for (int i = 0; i < m; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
		{
			sp[i] = a[i % m];
			a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
		}
		vector<long long> dp(n, 1);
		for (int i = 1; i < n; i++)
		{
			for (int j = i - 1; j >= 0; j--)
			{
				if (sp[i] > sp[j])
				{
					dp[i] += dp[j];
					dp[i] %= tt;
				}
			}
			dp[i] %= tt;
			//dp[i] = 1 + sum(dp[j], if(a[i] > a[j]))
		}
		long long cnt = 0;
		for (int i = 0; i < n; i++)
		{
			cnt += dp[i] % tt;
			cnt %= tt;
		}
		cout << "Case #" << u << ": " << cnt << endl;
	}
	return 0;
}


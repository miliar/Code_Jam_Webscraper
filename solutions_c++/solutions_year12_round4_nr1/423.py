#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef pair<long long, long long> pii;

const int maxN = 10100;

int t, n, d;
pii ar[maxN];
long long dp[maxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			dp[i] = 0;
			scanf("%lld%lld", &ar[i].first, &ar[i].second);
		}
		scanf("%d", &d);
		dp[0] = ar[0].first;
		bool b = false;
		for (int pos = 0; pos < n; pos++)
		{
			for (int j = pos + 1; j < n; j++)
			{
				if (ar[pos].first + dp[pos] >= ar[j].first)
				{
					dp[j] = max(dp[j], min(ar[j].second, ar[j].first - ar[pos].first));
				}
				else
				{
					break;
				}
			}
			if (dp[pos] + ar[pos].first >= d)
			{
				b = true;
				break;
			}
		}
		printf("Case #%d: ", q + 1);
		if (b)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}
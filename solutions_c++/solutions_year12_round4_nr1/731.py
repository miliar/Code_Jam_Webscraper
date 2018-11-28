#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

long long d[10050], l[10050], dp[10050];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tt, T;
	scanf("%d", &T);
	for (tt = 0; tt < T; ++tt)
	{
		int n, i, j;
		long long D;
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
			scanf("%lld%lld", &d[i], &l[i]);
		scanf("%lld", &D);
		for (i = 0; i < n; ++i)
			dp[i] = 0;
		dp[0] = d[0]*d[0];
		for (i = 0; i < n; ++i)
		{
			for (j = i + 1; j < n; ++j)
			{
//				printf("%lld\n", (d[j] - d[i])*(d[j] - d[i]));
				if ((d[j] - d[i])*(d[j] - d[i]) > dp[i])
					continue;
//				printf("%d %d\n", i, j);
				dp[j] = max(dp[j], min(l[j]*l[j], (d[j] - d[i])*(d[j] - d[i])));
			}
//			printf("%lld\n", dp[i]);
		}
		
		printf("Case #%d: ", tt + 1);
		for (i = 0; i < n && dp[i] < (D - d[i])*(D - d[i]); ++i);
//		printf("%d ", i);
		if (i < n)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
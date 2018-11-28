#include <cstdio>
#include <algorithm>
using namespace std;

bool can[55];
long long x[55], v[55];
long long num[55];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long T, nt, n, k, b, t, l, i, j;
	scanf("%lld", &T);
	for (nt = 1; nt <= T; nt++)
	{
		scanf("%lld%lld%lld%lld", &n, &k, &b, &t);
		for (i = 0; i < n; i++)
			scanf("%lld", x+i);
		for (i = 0; i < n; i++)
			scanf("%lld", v+i);
		memset(can, 0, sizeof(can));
		for (l = i = 0; i < n; i++)
			if (b-x[i] <= t*v[i])
			{
				can[i] = 1;
				l++;
			}
		if (l < k)
		{
			printf("Case #%d: IMPOSSIBLE\n", nt);
			continue;
		}
		l = 0;
		memset(num, 0, sizeof(num));
		for (i = 0; i < n; i++)
			if (can[i])
			{
				for (j = 0; j < n; j++)
					if (!can[j])
					{
						if (x[j] > x[i])
							num[l]++;
					}
				l++;
			}
		sort(num, num+l);
		long long ans = 0;
		for (i = 0; i < k; i++)
			ans += num[i];
		printf("Case #%lld: %lld\n", nt, ans);
	}
	return 0;
}

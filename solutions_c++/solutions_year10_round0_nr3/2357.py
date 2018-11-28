#include <iostream>
#include <string>
#include <cmath>
using namespace std;
const int maxn = 1001;
int a[maxn];
int cnt[maxn];
int next[maxn];
int main()
{
	int i, j, t, n, r, k, c = 0;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	//freopen("in", "r", stdin);
	scanf("%d", &t);
	for (c = 0; c < t; c++)
	{
		scanf("%d %d %d", &r, &k, &n);
		memset(a, 0, sizeof(a));
		memset(cnt, 0, sizeof(cnt));
		memset(next, 0, sizeof(next));
		for (i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
		}
		for (j = 0; j < n; j++)
		{
			if (cnt[0] + a[j] <= k)
			{
				cnt[0] += a[j];
			}
			else
			{
				break;
			}
		}
		next[0] = j % n;
		for (i = 1; i < n; i++)
		{
			cnt[i] = cnt[i-1] - a[i-1];
			for (j = next[i-1]; j < n + next[i-1]; j++)
			{
				if (cnt[i] + a[j%n] <= k)
				{
					cnt[i] += a[j%n];
				}
				else
				{
					break;
				}
			}
			next[i] = j % n;
		}
		int p = 0;
		long long ans = 0;
		for (i = 0; i < r; i++)
		{
			ans += cnt[p];
			p = next[p];
		}

		printf("Case #%d: %lld\n", c + 1, ans);
	}
	return 0;
}

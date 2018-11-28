#include <cstdio>
using namespace std;

int t, n;
int a[1010];
bool f[1010];

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("outputlarge.txt", "w", stdout);

	int i, j, k, l;
	int ans;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		for (j = 0; j < n; ++j)
		{
			scanf("%d", &a[j]);
			--a[j];
			f[j] = 0;
		}
		ans = 0;
		for (j = 0; j < n; ++j)
			if (!f[j])
			{
				k = 0;
				l = j;
				while (!f[l])
				{
					f[l] = 1;
					l = a[l];
					++k;
				}
				if (k > 1)
				ans += k;
			}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
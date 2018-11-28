#include <stdio.h>
const int MAXN = 1010;
int r, k ,n;
int a[MAXN], link[MAXN];
long long sum[MAXN];
long long ans;
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (int j = 0; j < n; ++j) scanf("%d", &a[j]);
		ans = 0;
		int tail = 0;
		long long cnt = 0;
		for (int j = 0; j < n; ++j)
		{
			if (tail == j)
			{
				cnt = a[tail];
				tail = (tail + 1) % n;
			}
			while (cnt + a[tail] <= k && tail != j)
			{
				cnt += a[tail];
				tail = (tail + 1) % n;
			}
			sum[j] = cnt;
			link[j] = tail;
			cnt -= a[j];
		}
		int pos = 0;
		for (int j = 0; j < r; ++j)
		{
			ans += sum[pos];
			pos = link[pos];
		}
		printf("Case #%d: %lld\n", i, ans);
	}
	return 0;
}

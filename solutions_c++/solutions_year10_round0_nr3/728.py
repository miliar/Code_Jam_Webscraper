#include<stdio.h>
#include<string.h>

int tim[1005], a[1005], R, k, n, cur;
long long money[1005];

int main()
{
	int tc, i, j;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d %d %d", &R, &k, &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
		}
		memset(tim, 0xff, sizeof(tim));
		tim[0] = 0;
		cur = 0;
		for (i = 0; i < R; i++)
		{
			money[i] = 0;
			int tmp = 0;
			while (money[i] + a[cur] <= k && tmp < n)
			{
				tmp++;
				money[i] += a[cur];
				cur = (cur + 1) % n;
			}
//			printf("%d -- %I64d\n", i, money[i]);
			if (tim[cur] >= 0)
				break;
			else
				tim[cur] = i + 1;
		}
		long long ans = 0;
		if (i == R)
		{
			for (j = 0; j < R; j++)
			{
				ans += money[j];
			}
		}
		else
		{
			long long pmoney = 0;
			for (j = tim[cur]; j <= i; j++)
			{
				pmoney += money[j];
			}
			for (j = 0; j < tim[cur]; j++)
			{
				ans += money[j];
			}
//			printf(".... %I64d %I64d\n", ans, pmoney);
			ans += pmoney * ((R - tim[cur]) / (i - tim[cur] + 1));
			long long mod = (R - tim[cur]) % (i - tim[cur] + 1);
			for (j = tim[cur]; j < mod + tim[cur]; j++)
			{
				ans += money[j];
			}
		}
		printf("Case #%d: %I64d\n", t, ans);
	}
	return 0;
}

/*

3
6 6 4
1 4 2 1

*/

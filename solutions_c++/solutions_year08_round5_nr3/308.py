#include <cstdio>
#include <cstring>

int cnt[20][2000], test;
void work()
{
	memset(cnt, 0, sizeof(cnt));
	int n, m;
	scanf("%d%d", &n, &m);
	int block[30] = {};
	for (int i = 0; i < n; ++i)
	{
		char s[300];
		scanf("%s", s);
		for (int j = 0; j < m; ++j)
			if (s[j] == 'x')
				block[i + 1] |= 1 << j; 
	}
	for (int i = 1; i <= n; ++i)
	{
		for (int from = 0; from < 1 << m; ++from) 
		{
			if (from & block[i - 1])
				continue;
			for (int j = 0; j < 1 << m; ++j)
			{
				if (j & block[i])
					continue;
				if (j & (j << 1))
					continue;
				if (j & (j >> 1))
					continue;
				if (j & (from >> 1))
					continue;
				if (j & (from << 1))
					continue;
				int t = 0, t2 = j;
				while (t2)
				{
					t += (t2 & 1);
					t2 >>= 1;
				}
				if (cnt[i][j] < cnt[i - 1][from] + t)
					cnt[i][j] = cnt[i - 1][from] + t;
			}
			if (i == 1)
				break;
		}
	}
	int ans = 0;
	for (int i = 0; i < 1 << m; ++i)
	{
		if (ans < cnt[n][i])
			ans = cnt[n][i];
	}
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}

#include <iostream>
using namespace std;

int i, j, k, t, next[1001], n, m, s, a[1001], len, tmp, tim[1001];
long long cnt, ans, sum[1001];
bool used[1001];

int main()
{
	freopen("a.in", "r", stdin);
   	freopen("a.out", "w", stdout);
   	scanf("%d", &t);
   	for (k = 1; k <= t; k++)
   	{
   		scanf("%d%d%d", &m, &s, &n);
   		for (i = 1; i <= n; i++) scanf("%d", &a[i]);

   		memset(next, 0, sizeof(next));
   		memset(sum, 0, sizeof(sum));
   		memset(used, 0, sizeof(used));

		j = 1;
		while (!next[j])
		{
			cnt = 0;
			i = j;
			while (cnt+a[j] <= s)
			{
				cnt += a[j];
				if (j == n) j = 1; else j++;
				if (j == i) break;
			}
			next[i] = j;
			sum[i] = cnt;
		}

		i = 1; cnt = 0; j = 0;
		while (!used[i])
		{
			cnt += sum[i];
			used[i] = 1;
			tim[i] = j++;
			if (used[next[i]]) len = j - tim[next[i]];
			i = next[i];
		}
		tmp = i;
		
		memset (used, 0, sizeof (used));

		i = 1; ans = 0; j = 0;
		while (i != tmp)
		{
			ans += sum[i];
			i = next[i];
			j++;
		}
		cnt -= ans;
		m -= j;

		ans += (m / len) * cnt;

		m %= len; j = 0;
		while (j < m)
		{
			ans += sum[i];
			i = next[i];
			j++;
		}

		printf("Case #%d: %I64d\n", k, ans);
   	}
}

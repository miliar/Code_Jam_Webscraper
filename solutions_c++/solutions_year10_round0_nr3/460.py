#include <stdio.h>
#include <string.h>

int g[1000], sum[1000], used[1000];
long long ans;

int main()
{
	//freopen("C2.in", "r", stdin);
	//freopen("C2.out", "w", stdout);

	int nprob, r, k, n;
	scanf("%d", &nprob);
	for (int prob = 0; prob < nprob; prob ++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i ++) scanf("%d", &g[i]);
		memset(used, 255, sizeof(used));
		ans = 0;

		int p = 0, amount = 0;
		for (int idx = 0; idx < r; idx ++)
		{
			int q = p;
			while (amount <= k - g[q])
			{
				amount += g[q];
				q ++;
				if (q == n) q = 0;
				if (p == q) break;
			}

			if (used[p] != -1)
			{
				long long tmp = 0;
				for (int i = used[p]; i < idx; i ++) tmp += sum[i];
				ans += tmp * ((r - idx) / (idx - used[p]));
				for (int i = 0; i < (r - idx) % (idx - used[p]); i ++)
				{
					ans += sum[used[p] + i];
				}
				break;
			}
			used[p] = idx;
			sum[idx] = amount;
			ans += amount;
			amount = 0;
			p = q;
		}

		printf("Case #%d: %lld\n", prob + 1, ans);
	}


	return 0;
}
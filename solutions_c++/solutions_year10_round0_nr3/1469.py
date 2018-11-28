#include <cstdio>
#include <cstring>

int g[1000], amt[1000], next[1000];
int T, R, k, N;
bool vis[1000];

int main()
{
	scanf("%d", &T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d %d %d", &R, &k, &N);
		for(int i = 0;i < N;++i)
			scanf("%d", &g[i]);
		for(int i = 0;i < N;++i)
		{
			amt[i] = g[i];
			int j = (i == N - 1 ? 0 : i + 1);
			for(;j != i && amt[i] + g[j] <= k;j = (j == N - 1 ? 0 : j + 1))
				amt[i] += g[j];
			next[i] = j;
		}
		memset(vis, 0, sizeof(vis));
		long long total = 0;
		int i = 0;
		for(;R > 0 && !vis[i];i = next[i])
		{
			vis[i] = 1;
			total += amt[i];
			--R;
		}
		if(R > 0)
		{
			long long add = amt[i];
			int clen = 1;
			for(int j = next[i];j != i;j = next[j])
			{
				add += amt[j];
				++clen;
			}
			total += (R / clen) * add;
			R %= clen;
			if(R > 0)
			{
				total += amt[i];
				--R;
				for(int j = next[i];R > 0 && j != i;j = next[j])
				{
					total += amt[j];
					--R;
				}
			}
		}
		printf("Case #%d: %lld\n", t, total);
	}
}

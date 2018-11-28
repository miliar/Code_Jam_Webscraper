#include <cstdio>
#include <cstring>

const int maxn = 1000;

long long g[maxn];
int next[maxn];
long long earn[maxn];
int mark[maxn];
long long last[maxn];
int r, k, n;

int getnext(int s)
{
	int now = 0;
	int p = s;
	earn[s] = 0;
	do
	{
		earn[s] += g[p];
		now += g[p++];
		if (p == n) p = 0;
	}
	while (p != s && now + g[p] <= k);
	return p;
}

int cycle()
{
	int p = 0;
	int c = 0;
	do
	{
		p = next[p];
		c++;
	}
	while (p != 0);
	return c;
}

int main()
{
	int testnumber;
	
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%I64d", &g[i]);
		
		for (int i = 0; i < n; i++)
			next[i] = getnext(i);
		
		memset(mark, 0xff, sizeof mark);
		int p = 0;
		int cur = 0;
		long long total = 0;
		while (cur < r && mark[p] == -1)
		{
			last[p] = total;
			total += earn[p];
			mark[p] = cur++;
			p = next[p];
		}
		if (cur != r)
		{
			int cyc = cur - mark[p];
			total += (total - last[p]) * ((r - cur) / cyc);
			int remain = (r - cur) % cyc;
			for (int i = 0; i < remain; i++)
			{
				total += earn[p];
				p = next[p];
			}
		}
		printf("Case #%d: %I64d\n", testcount + 1, total);
	}
	
	return 0;
}

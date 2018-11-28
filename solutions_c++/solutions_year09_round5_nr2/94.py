#include <cstdio>
#include <cstring>

int Case, m, k, ans, sel[30];
char s[500], dic[200][60];
#define M 10009

void dfs(int step, int last)
{
	if (step >= k)
	{
		int cnt[30] = {};
		int base = 1, dup = 0;
		for (int i = 0; i < k; ++i)
			base *= (i + 1);
		for (int i = 0; i < k; ++i)
		{
			if (i == 0 || sel[i] != sel[i - 1])
				dup = 0;
			++dup;
			base /= dup;
			for (const char* t = dic[sel[i]]; *t; ++t)
				++cnt[*t - 'a'];
		}
		int cur = 1, val = 0;
		for (const char*t = s; *t; ++t)
		{
			if (*t != '+' && *t != '=')
			{
				cur = cur * cnt[*t - 'a'] % M;
			}
			else
			{
				val = (val + cur) % M;
				cur = 1;
			}
		}
		base %= M;
		ans = (ans + base * val) % M;
		return;
	}
	for (int i = last; i < m; ++i)
	{
		sel[step] = i;
		dfs(step + 1, i);
	}
}

void work()
{
	ans = 0;
	int maxk;
	scanf("%s%d", s, &maxk);
	strcat(s, "=");
	scanf("%d", &m);
	for (int i = 0; i < m; ++i)
		scanf("%s", dic[i]);
	printf("Case #%d:", ++Case);
	for (k = 1; k <= maxk; ++k)
	{
		ans = 0;
		dfs(0, 0);
		printf(" %d", ans);
	}
	puts("");
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}

#include <cstdio>
int test;
int type[30000], val[30000], ch[30000];
int step[30000][2];

int min(int a, int b)
{
	return (a<b)?a:b;
}
void work()
{
	int m, v;
	scanf("%d%d", &m, &v);
	for (int i = 1; i <= (m - 1) / 2; ++i)
		scanf("%d%d", &type[i], &ch[i]);
	for (int i = (m - 1) / 2 + 1; i <= m; ++i)
	{
		scanf("%d", &val[i]);
		step[i][val[i]] = 0;
		step[i][!val[i]] = 20000;
	}
	for (int i = (m - 1) / 2; i; --i)
	{
		step[i][type[i]] = step[i * 2][type[i]] + step[i * 2 + 1][type[i]];
		step[i][!type[i]] = min(step[i * 2][0] + step[i * 2 + 1][1], step[i * 2][1] + step[i * 2 + 1][0]);
		step[i][!type[i]] = min(step[i][!type[i]], step[i * 2][!type[i]] + step[i * 2 + 1][!type[i]]);
		if (ch[i])
		{
			step[i][type[i]] = min(step[i][type[i]], 1 + step[i * 2][0] + step[i * 2 + 1][1]);
			step[i][type[i]] = min(step[i][type[i]], 1 + step[i * 2][1] + step[i * 2 + 1][0]);
		}
	}
	if (step[1][v] > 10000)
		printf("Case #%d: IMPOSSIBLE\n", ++test);
	else
		printf("Case #%d: %d\n", ++test, step[1][v]);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}

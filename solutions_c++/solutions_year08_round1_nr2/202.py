# include <stdio.h>

struct Customer
{
	int a[15], flag[15];
}cus[105];

bool check(int key, int m)
{
	int i, j;
	bool flag;
	for (i = 0; i < m; i++)
	{
		flag = false;
		for (j = 1; !flag && j <= cus[i].a[0]; j++)
		{
			if (((key >> (cus[i].a[j] - 1)) % 2) == cus[i].flag[cus[i].a[j]])
				flag = true;
		}
		if (!flag) break;
	}
	return i == m;
}

bool cmp(int ans, int d)
{
	if (ans == -1) return true;
	int a, b;
	for (a = 0; ans; a++) ans &= (ans - 1);
	for (b = 0; d; b++) d &= (d - 1);
	return b < a;
}

void output(int key, int n)
{
	while (n--)
	{
		printf(" %d", key % 2);
		key >>= 1;
	}
	puts("");
}

int main()
{
	int cases, n, m, i, j, sta, t, k, a, b, ans;
	freopen("D:\\b.in", "r", stdin);
	freopen("D:\\b.out", "w", stdout);
	scanf("%d", &cases);
	t = 0;
	while (cases--)
	{
		printf("Case #%d:", ++t);
		scanf("%d%d", &n, &m);
		for (i = 0; i < m; i++)
		{
			scanf("%d", &k);
			cus[i].a[0] = k;
			for (j = 1; j <= k; j++)
			{
				scanf("%d%d", &a, &b);
				cus[i].a[j] = a;
				cus[i].flag[a] = b;
			}
		}
		int top = 1 << n;
		ans = -1;
		for (sta = 0; sta < top; sta++)
			if (check(sta, m) && cmp(ans, sta))
				ans = sta;
		if (ans == -1) puts(" IMPOSSIBLE");
		else output(ans, n);
	}
	return 0;
}
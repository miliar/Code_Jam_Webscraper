#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, n, x[2010], ans[2010];

bool pass()
{
	for (int i = 1; i < n; i++)
		for (int j = i + 1; j < n; j++)
		if (j < x[i] && x[i] < x[j])
			return false;
	return true;
}

void dfs(int l, int r)
{
	if (l > r) return;
	int k = l;
	while (x[k] != r + 1)
		k++;
	ans[k] = ans[r + 1] - 1;
	dfs(l, k - 1);
	dfs(k + 1, r);
}

bool check()
{
	for (int i = 1; i < n; i++)
	{
		int xx = x[i] - i, yy = ans[x[i]] - ans[i];
		for (int j = i + 1; j < x[i]; j++)
		{
			int xa = j - i, ya = ans[j] - ans[i];
			if (ya * xx >= xa * yy)
			{
				for (int k = x[i]; k <= n; k++)
					ans[k]++;
				return false;
			}
		}
		for (int j = x[i] + 1; j <= n; j++)
		{
			int xa = j - i, ya = ans[j] - ans[i];
			if (ya * xx > xa * yy)
			{
				for (int k = x[i]; k <= n; k++)
					ans[k]++;
				return false;
			}
		}
	}
	return true;
}

int main()
{
	scanf("%d", &T);
	int ca = 0;
	while (T--)
	{
		ca++;
		scanf("%d", &n);
		for (int i = 1; i < n; i++)
			scanf("%d", &x[i]);
		printf("Case #%d:", ca);
		if (pass())
		{
			for (int i = 1; i <= n; i++)
				ans[i] = 1;
			while (!check());
			for (int i = 1; i <= n; i++)
				printf(" %d", ans[i]);
			printf("\n");
		}
		else puts(" Impossible");
	}
	return 0;
}

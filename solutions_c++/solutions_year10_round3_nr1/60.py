#include <stdio.h>

int a[1005], b[1005];

int main()
{
	//freopen("A2.in", "r", stdin);
	//freopen("A2.out", "w", stdout);

	int nprob, n;
	scanf("%d", &nprob);
	for (int prob = 0; prob < nprob; prob ++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) scanf("%d%d", &a[i], &b[i]);
		int ans = 0;
		for (int i = 0; i < n; i ++)
		{
			for (int j = i + 1; j < n; j ++)
			{
				if ((a[i] - a[j]) * (b[i] - b[j]) < 0) ans ++;
			}
		}
		printf("Case #%d: %d\n", prob + 1, ans);
	}

	return 0;
}
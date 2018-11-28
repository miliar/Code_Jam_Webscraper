#include <stdio.h>

int d[10010], l[10010];
int a[10010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		int D;
		scanf("%d", &D);
		for (int i = 0; i < n; ++i)
			a[i] = -1;
		a[0] = d[0] * 2;
		if (a[0] >= D)
		{
			printf("Case #%d: YES\n", tt);
			continue;
		}
		bool flag = false;
		for (int i = 1; i < n; ++i)
		{
			for (int j = 0; j < i; ++j)
				if (a[j] >= d[i])
				{
					int ll;
					if (l[i] > d[i] - d[j]) ll = d[i] - d[j];
					else ll = l[i];
					if (ll + d[i] > a[i]) a[i] = ll + d[i];
				}
			if (a[i] >= D)
			{
				flag = true;
				break;
			}
		}
		if (flag) printf("Case #%d: YES\n", tt);
		else printf("Case #%d: NO\n", tt);
	}
	return 0;
}

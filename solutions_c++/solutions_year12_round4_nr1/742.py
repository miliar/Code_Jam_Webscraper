#include <stdio.h>
#define N 10000

int main()
{
	int t;
	int n, f, now;
	int d[N], l[N], best[N];
	scanf("%d", &t);
	for (int i=1;i<=t;++i)
	{
		scanf("%d", &n);
		for (int j=0;j<n;++j)
		{
			scanf("%d%d", &d[j], &l[j]);
			best[j] = 0;
		}
		scanf("%d", &f);
		now = best[0] = 2*d[0];
		for (int j=1;j<n;++j)
		{
			for (int k=j-1;k>=0;--k)
			{
				if (best[k]<d[j])
					continue;
				best[j]>?=d[j]+((d[j]-d[k])<?l[j]);
			}
			now >?= best[j];
		}
		printf("Case #%d: %s\n", i, now>=f?"YES":"NO");
	}
	return 0;
}

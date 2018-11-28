#include <algorithm>
#include <cstdio>

using namespace std;

const int maxn = 10005, oo = 1000000005;

int d[maxn], l[maxn], f[maxn], n, D, test;

int	main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &test);
	for (int kase = 1; kase <= test; ++kase)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &D);
		for (int i = 0; i <= n; ++i)
			f[i] = oo;
		for (int i = n; i >= 1; --i)
		{
			if (d[i] + l[i] >= D)
				f[i] = D - d[i];
			for (int j = i + 1; j <= n; ++j)
				if (d[j] - d[i] >= f[j])
					if (d[i] >= d[j] - l[i])
						f[i] = min(f[i], d[j] - d[i]);
		}
		printf("Case #%d: ", kase);
		if (d[1] >= f[1])
			puts("YES");
		else
			puts("NO");
	}
	
	return 0;
}

#include <cstdio>
#include <cstring>

const int MAXN = 10000 + 10;

int n;
int d[MAXN], l[MAXN];
int f[MAXN];

int main()
{
	int T, dist;
	freopen("a.out", "wt", stdout);
	freopen("a-large.in", "rt", stdin);

	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &dist);
		int x = 0, j = 1;
		memset(f, -1, sizeof(f));
		f[0] = d[0] + d[0];
		bool reach = f[0] >= dist;
		for (int i = 0; i < n; ++i)
			if (f[i] > 0)
			{
				while (j < n && f[i] >= d[j])
				{
					if (d[j] - d[i] > l[j])
						f[j] = d[j] + l[j];
					else 
						f[j] = d[j] + (d[j] - d[i]);
					if (f[j] >= dist)
						reach = true;
					++j;
				}
				//printf("%d\n", f[i]);
			}
		printf("Case #%d: ", tt);
		if (reach)
			puts("YES");
		else 
			puts("NO");
	}
	return 0;
}

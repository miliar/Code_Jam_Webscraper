#include <cstdio>
#include <cstring>
#define MAXD 10001
#define MAXL 20
int cnt, l, d, n, f[MAXD];
char st[MAXD], a[MAXD][MAXL];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);gets(st);
	for (int i = 0; i < d; i++) gets(a[i]);
	for (int i = 1; i <= n; i++)
	{
		cnt = 0; memset(f, 0, sizeof(f));
		gets(st);
		for (int j = 0, t = 0; st[j]; j++, t++)
		{
			if (st[j] == '(')
			{
				j++;
				while (st[j] != ')')
				{
					for (int k = 0; k < d; k++)
						if (a[k][t] == st[j] && f[k] == t) f[k] = t + 1;
					j++;
				}
				continue;
			}
			for (int k = 0; k < d; k++)
				if (a[k][t] == st[j] && f[k] == t) f[k] = t + 1;
		}
		for (int k = 0; k < d; k++)
			if (f[k] == l) cnt++;
		printf("Case #%d: %d\n", i, cnt);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
#include <cstdio>
#include <iostream>
#define MAXN 100
#define MAXPIXEL 256
int test, t;
int n;
int Del, Ins, Mod;
int a[MAXN];
int f[MAXN][MAXPIXEL];

void init()
{
	scanf ("%d%d%d%d", &Del, &Ins, &Mod, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void process()
{
	for (int j = 0; j < MAXPIXEL; j++)
		f[0][j] = abs(j - a[0]);

	for (int i = 1; i < n; i++)
		for (int j = 0; j < MAXPIXEL; j++)
		{
			f[i][j] = f[i - 1][j] + Del;
			for (int t = 0; t < MAXPIXEL; t++)
			{
				int tmp = abs(a[i] - j) + f[i - 1][t];
				if (abs(j - t) > 0)
					if (Mod > 0)
						tmp += (abs (j - t) - 1) / Mod * Ins;
					else
						continue;

				if (tmp < f[i][j])
					f[i][j] = tmp;
			}
		}
}

void print()
{
	int ans = f[n - 1][0];
	for (int j = 0; j < MAXPIXEL; j++) 
	{
		if (f[n - 1][j]<ans)
			ans = f[n - 1][j];
	}
	printf ("Case #%d: %d\n", test + 1, ans);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	scanf ("%d", &t);
	for (test = 0; test < t; test++)
	{
		init();
		process();
		print();
	}
	return 0;
}
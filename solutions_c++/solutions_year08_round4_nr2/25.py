#include <cstdio>
#include <cmath>

int test;
int n, m, a;

bool check(int mult, int &a, int &b)
{
	if (mult == 0)
	{
		a = 0; b = 0; return 1;
	}
	//a <= n && b <= m, a*b=mult
	int mm = sqrt(mult);
	if (m > n)
	{
		for (a = mult / m; a <= n && a <= mm; ++a)
		{
			if (!a)
				continue;
			if (mult % a == 0)
			{
				b = mult / a;
				if (a <= n && b <= m)
					return 1;
			}
		}
	}
	else
	{
		for (b = mult / n; b <= m && b <= mm; ++b)
		{
			if (!b)
				continue;
			if (mult % b == 0)
			{
				a = mult / b;
				if (a <= n && b <= m)
					return 1;
			}
		}
	}
	return 0;
}

void work()
{
	scanf("%d%d%d", &n, &m, &a);
	printf("Case #%d: ", ++test);
	int x1, y1, x2, y2;
	for (int t = a; t <= n * m; ++t)
	{
		if (check(t - a, x2, y1) && check(t, x1, y2))
		{
			printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}

#include <stdio.h>

int solve()
{
	int a, b, c = 0, p = 1;
	scanf("%d %d", &a, &b);
	while (10 * p <= a)
		p *= 10;
	for (; a < b; a++)
		for (int d = a; ;)
		{
			d = d / 10 + d % 10 * p;
			if (d == a)
				break;
			if (a < d && d <= b)
				c++;
		}
	return c;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, solve());
}
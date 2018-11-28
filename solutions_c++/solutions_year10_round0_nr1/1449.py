#include <stdio.h>
#include <math.h>

int t, n, k;
int tmp;

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%d%d", &n, &k);
		tmp = pow(2.0, (double)n);
		k %= tmp;
		if (k == tmp - 1)
			printf("Case #%d: ON\n", i + 1);
		else
			printf("Case #%d: OFF\n", i + 1);
	}
	return 0;
}
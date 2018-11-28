#include <stdio.h>

int main ()
{
	freopen ("snapper.in", "r", stdin);
	freopen ("snapper.out", "w", stdout);
	int i, t, n, k;
	scanf ("%d", &t);
	for (i=1; i <= t; ++i)
	{
		scanf ("%d%d", &n, &k);
		if ((k+1)%(1<<n))
			printf ("Case #%d: OFF\n", i);
		else
			printf ("Case #%d: ON\n", i);
	}
	return 0;
}


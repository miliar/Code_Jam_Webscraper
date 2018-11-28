#include <stdio.h>

int n;
int tot, mi, xo;

int main ()
{
	int t, ct = 0;

	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d", &n);
		tot = xo = 0;
		mi = 2147483647;

		for (int i = 0;i  < n; i ++)
		{
			int x;

			scanf ("%d", &x);
			tot += x;
			if (x < mi) mi = x;
			xo ^= x;
		}

		printf ("Case #%d: ", ++ ct);

		if (xo)
			printf ("NO\n");
		else
			printf ("%d\n", tot - mi);
	}

	return 0;
}

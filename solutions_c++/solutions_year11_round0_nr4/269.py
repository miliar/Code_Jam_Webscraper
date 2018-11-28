#include <stdio.h>

int n;

int main ()
{
	int t, ct = 0;

	for (scanf ("%d", &t) > 0; t > 0; t --)
	{
		scanf ("%d", &n);
		int wrong = 0;
		for (int i = 0; i < n; i ++)
		{
			int x;

			scanf ("%d", &x);
			if (x != i + 1) wrong ++;
		}

		printf ("Case #%d: %d.000000\n", ++ ct, wrong);
	}

	return 0;
}

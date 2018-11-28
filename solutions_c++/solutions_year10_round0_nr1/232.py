#include <stdio.h>
#include <math.h>

int main (void)
{
	int t, n, k;

	scanf ("%d", &t);
	for (int t1 = 1; t1 <= t; t1++)
	{
		scanf ("%d %d", &n, &k);

		if (k == 0)
		{
			printf ("Case #%d: OFF\n", t1);
			continue;
		}

		k %= (int) pow(2,n);

		if (k == (int) pow(2, n) - 1)
			printf ("Case #%d: ON\n", t1);
		else
			printf ("Case #%d: OFF\n", t1);
	}

	return 0;
}

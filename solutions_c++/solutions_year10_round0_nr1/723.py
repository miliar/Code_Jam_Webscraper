#include <stdio.h>

int n;

int main ()
{
	freopen ("alarge.in", "r", stdin);
	freopen ("alarge.out", "w", stdout);

	scanf ("%d", &n);
	for (int i = 0; i < n; i ++)
	{
		int a, b;

		scanf ("%d%d", &a, &b);
		if ((b & ((1 << a) - 1)) == ((1 << a) - 1))
			printf ("Case #%d: ON\n", i + 1);
		else
			printf ("Case #%d: OFF\n", i + 1);
	}

	return 0;
}
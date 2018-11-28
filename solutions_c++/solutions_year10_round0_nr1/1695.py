#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int masks[32]; // masks[i] is consecutive i's '1'

int main()
{
	int kase, serial = 1, n, k;

	masks[1] = 1;
	for (int i=2; i<32; ++i) {
		masks [i] = (masks [i-1] << 1) | 1;
	}

	scanf ("%d", &kase);
	while (kase--)
	{
		// BEGIN test case
		scanf ("%d %d", &n, &k);

		printf ("Case #%d: ", serial++);
		if ((k & masks[n]) == masks[n])
			puts ("ON");
		else
			puts ("OFF");

		// END test case
	}
	return 0;
}
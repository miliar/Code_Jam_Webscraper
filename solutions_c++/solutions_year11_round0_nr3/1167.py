#include <stdio.h>

static unsigned work ()
{
	unsigned min = -1;
	unsigned sum = 0;
	unsigned xors = 0;
	unsigned candies;
	scanf ("%u", &candies);
	while (candies--) {
		unsigned u;
		scanf ("%u", &u);
		if (u < min)
			min = u;
		sum += u;
		xors ^= u;
	}
	if (xors == 0)
		return (sum - min);
	else
		return 0;
}

int main ()
{
	unsigned T;
	scanf ("%u", &T);
	for (unsigned j=1; j<=T; ++j) {
		printf ("Case #%u: ", j);
		unsigned result = work ();
		if (result == 0)
			puts ("NO");
		else
			printf ("%u\n", result);
	}
	return 0;
}

/*
 * A.cc
 *
 *  Created on: May 20, 2011
 *      Author: jliao2
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gcd(int a, int b)
{
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

int main()
{
	int t, n, pd, pg;
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("A-large.out", "w");
	fscanf(in, "%d", &t);
	for (int test = 0; test < t; test++)
	{
		fscanf(in, "%d %d %d", &n, &pd, &pg);
		if (pg == 0 && pd != 0)
		{
			fprintf(out, "Case #%d: Broken\n", test+1);
			continue;
		}
		if (pg == 100 && pd != 100)
		{
			fprintf(out, "Case #%d: Broken\n", test+1);
			continue;
		}

		int x = 100 / gcd(pd, 100);
		if (x > n)
		{
			fprintf(out, "Case #%d: Broken\n", test+1);
			continue;
		}
		fprintf(out, "Case #%d: Possible\n", test+1);
	}
	fclose(in);
	fclose(out);
	return 0;
}

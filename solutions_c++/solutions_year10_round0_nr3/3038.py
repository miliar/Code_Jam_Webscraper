//============================================================================
// Name        : codejam_zad3.cpp
// Author      : Ivan Sovic
// Version     :
// Copyright   : Copyright Ivan Sovic, 2010.
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>



unsigned long int calculateOutput(unsigned long int r, unsigned long int k, unsigned int n, unsigned long int *g)
{
	unsigned int currentG=0, beginG=0, step=0;
	unsigned long int backpack=0, ret=0;

	while (r > 0)
	{
		if (currentG >= n)
			currentG = 0;

		backpack += g[currentG];

		if (backpack>k || (currentG==beginG && step>0))
		{
			ret += (backpack - g[currentG]);
			backpack = g[currentG];
			beginG = currentG;
			step = 0;
			r -= 1;
		}

		currentG += 1;
		step += 1;
	}

	return ret;
}

void writeOutputs(unsigned int t, unsigned long int *outputs)
{
	unsigned int i=0;

	for (i=0; i<t; i++)
	{
		printf ("Case #%d: %ld\n", (i+1), outputs[i]);
	}
}

int main()
{
	unsigned int i=0, j=0, n=0, t=0;
	unsigned long int r=0, k=0, tempG=0;
	unsigned long int *g=NULL;
	unsigned long int *outputs=NULL;

	scanf("%d", &t);

	outputs = (unsigned long int *) calloc(t, sizeof(unsigned long int));
	if (outputs == NULL)
	{
		printf ("Not enough memory!\n");
		return 1;
	}

	for (i=0; i<t; i++)
	{
		scanf("%ld %ld %d", &r, &k, &n);

		if (g)
		{
			free(g);
			g = NULL;
		}

		g = (unsigned long int *) calloc((n+1), sizeof(unsigned long int));
		if (g == NULL)
		{
			printf ("Not enough memory!\n");
			return 1;
		}

		for (j=0; j<n; j++)
		{
			scanf("%ld", &(tempG));
			g[j] = tempG;
		}

		outputs[i] = calculateOutput(r, k, n, g);
	}

	writeOutputs(t, outputs);

	return 0;
}

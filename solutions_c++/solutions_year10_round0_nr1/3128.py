//============================================================================
// Name        : codejam_zad1.cpp
// Author      : Ivan Sovic
// Version     :
// Copyright   : Copyright Ivan Sovic, 2010.
// Description : Google Code Jam, problem A
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <math.h>



char evaluateInput(unsigned int n, unsigned long int k)
{
	if (k == 0)
		return 0;

	if (((k+1) % ((unsigned long int) pow(2, n))) == 0)
		return 1;

	return 0;
}

void writeOutputs(unsigned int t, char *outputs)
{
	unsigned int i=0;

	for (i=0; i<t; i++)
	{
		if (outputs[i] == 0)
			printf ("Case #%d: OFF\n", (i+1));
		else
			printf ("Case #%d: ON\n", (i+1));
	}
}

int main()
{
	unsigned int i=0, t=0, n=0;
	unsigned long int k=0;
	char *outputs=NULL;

	scanf("%d", &t);

	outputs = (char *) calloc(t, sizeof(char));

	for (i=0; i<t; i++)
	{
		scanf("%d %ld", &n, &k);

		outputs[i] = evaluateInput(n, k);
	}

	writeOutputs(t, outputs);

	if (outputs)
		free(outputs);

	return 0;
}

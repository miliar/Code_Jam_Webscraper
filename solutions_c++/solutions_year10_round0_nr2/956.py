#include <iostream>
#include "stdio.h"

int numCount;
unsigned long slarbo[1000];

unsigned long get_gcd(unsigned long a, unsigned long b)
{
	if (!a)
		return b;
	while (b > 0)
		if (a > b)
			a -= b;
		else
			b -= a;
	return a;
}

int findSolution()
{
	unsigned long gcd;
	unsigned long min = slarbo[0];
	int min_i = 0;
	int i,j;

	// find minimum
	for (i = 1; i < numCount; i++)
	{
		if (min > slarbo[i])
		{
			min = slarbo[i];
			min_i = i;
		}
	}

	for (i = 0; i < numCount; i++)
	{
		slarbo[i] -= min;
		//printf("%lu ", slarbo[i]);
	}
	//printf("\n");

	// get gcd
	gcd = get_gcd(slarbo[0], slarbo[1]);
	for (i = 2; i < numCount; i++)
		gcd = get_gcd(gcd, slarbo[i]);

	//printf("gcd=%lu min=%lu min_i=%d\n", gcd, min, min_i);

	// find nearest
	//printf("%lu\n", (min > gcd ? 2*gcd-min : gcd-min));
	unsigned long val = gcd;
	while(val < min)
		val += gcd;

	printf("%lu\n", val - min);
}

int main()
{
	int caseCount;
	int i,j;

	scanf("%d", &caseCount);
	for(i = 0; i < caseCount; i++)
	{
		scanf("%d", &numCount);
		memset(slarbo, 0, sizeof(unsigned long)*1000);
		for (j =0 ; j<numCount; j++)
		{
			scanf("%lu", &slarbo[j]);
		}

		printf("Case #%d: ", i+1);
		findSolution();
	}

}

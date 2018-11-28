#include <cstdio>
using namespace std;

unsigned long Recycle(unsigned long num, unsigned long min, unsigned long max)
{
	unsigned long ulStart = num;
	unsigned long tempNum = num;
	unsigned long multiplier = 1;
	int			  digit;
	unsigned long ulNumRecycles = 0;

	// First get the multipler
	while(tempNum != 0)
	{
		multiplier *= 10UL;
		tempNum /= 10;
	}

	multiplier /= 10;
	do
	{
		digit = num % 10UL;
		num /= 10UL;
		num = (digit * multiplier) + num;
		if(num >= min && num <= max && num >= multiplier && num != ulStart)
			ulNumRecycles++;

	} while(num != ulStart);

	return ulNumRecycles;

}

int main()
{
	int			  iNumTestCases;
	int			  iTestCaseIndex;
	unsigned long numRecycles;
	unsigned long ulMin;
	unsigned long ulMax;

	scanf("%d", &iNumTestCases);
	
	for(iTestCaseIndex = 0; iTestCaseIndex < iNumTestCases; iTestCaseIndex++)
	{
		scanf("%ld %ld", &ulMin, &ulMax);
		numRecycles = 0;

		for(unsigned long i = ulMin; i <= ulMax; i++)
		{
			numRecycles += Recycle(i, ulMin, ulMax);
		}

		numRecycles /= 2UL;
		printf("Case #%d: %ld\n", iTestCaseIndex + 1, numRecycles);
	}

	return 0;
}
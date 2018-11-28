#include <iostream>
#include "stdio.h"
using namespace std;

//#define DBGOUT printf
void DBGOUT(...) { } 


unsigned long mul2(unsigned long n)
{
	unsigned long ret = 1;
	for (int i = 0; i < n; i++)
		ret *= 2;

	return ret;
}

int findSolution(unsigned long n, unsigned long k)
{
	unsigned long loop  = mul2(n);

	//printf("loop=%lu\n", loop);

	if ((k % loop) == loop - 1)
		return 1;

	return 0;
}

int main()
{
	unsigned long NN, KK;
	int caseCount;
	int i,j;

	scanf("%d", &caseCount);
	for (i = 0; i < caseCount; i++)
	{
		scanf("%lu %lu", &NN, &KK);

		printf("Case #%d: ", i+1);
		printf("%s\n", (findSolution(NN, KK) > 0 ? "ON" : "OFF"));
	}
}





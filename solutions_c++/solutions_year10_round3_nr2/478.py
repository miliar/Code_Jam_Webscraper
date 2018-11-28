#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int casos, res;
	long long unsigned int L, C, P; 
	double log102 = log10(2);
	scanf("%d", &casos);
	for (int c = 1; c <= casos; c++)
	{
		scanf("%llu %llu %llu", &L, &P, &C);
		res = 0;
		while (P > L)
		{
			L = L*C;
			res++;
		}
		res = (int)ceil(log10(res)/log102);
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}

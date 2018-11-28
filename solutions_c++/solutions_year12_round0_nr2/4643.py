#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctime>

char GetMaxGooglers(char nGooglers, char nSurprise, char nLeast)
{
	char	iter, nRes = 0;
	char	nZero = 0, nCandidate = 0, nObvious = 0;
	int		nPoint;

	for(iter=0; iter<nGooglers; iter++)
	{
		scanf("%d", &nPoint);

		if(0 == nPoint) nZero++;
		
		if(nPoint >= 3*nLeast-2)
		{
			nObvious++;
		}
		else if(nPoint >= 3*nLeast-4)
		{
			nCandidate++;
		}
	}

	switch(nLeast)
	{
	case 0:
		nRes = nGooglers;
		break;
	case 1:
		nRes = nGooglers - nZero;
		break;
	default:
		nRes = nObvious + ((nCandidate > nSurprise) ? nSurprise : nCandidate);
	}

	return nRes;
}


int main(void)
{
    clock_t				start_time = clock();
	char				iter;
	int					nCounts, nGooglers, nSurprise, nLeast;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d\n", &nCounts);

	for(iter=0; iter<nCounts; iter++)
	{
		scanf("%d %d %d", &nGooglers, &nSurprise, &nLeast);

		printf("Case #%d: %d\n", iter+1, GetMaxGooglers(nGooglers, nSurprise, nLeast));
	}	

	fcloseall();
	fprintf(stderr, "Elapsed time : %.3fsec\n", (double)(clock()-start_time)/CLOCKS_PER_SEC);

	return 0;
}
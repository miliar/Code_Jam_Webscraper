#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(GCJ10Q-1,"Code Jam 2010-Q01")
#endif


#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int testNo;
	int N,K;
	scanf("%d", &testNo);
	for(int t=1; t <= testNo; t++)
	{
		scanf("%d%d", &N, &K);
		int B = (1 << N);
		K %= (1 << N);
		printf("Case #%d: %s\n", t, K == (B-1) ? "ON" : "OFF" );
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif
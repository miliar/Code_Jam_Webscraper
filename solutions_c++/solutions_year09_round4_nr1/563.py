#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> 

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(GCJ9-R2A,"Code Jam 2009-R2 A")
#endif

const int MAX_N = 40;
int Values[MAX_N];
template <typename T> T min(T a, T b) { return a < b ? a : b; }
template <typename T> T abs(T a) { return a > 0 ? a : -a; }

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int TestCases;
	scanf("%d", &TestCases);
	for(int test=1; test<=TestCases; test++)
	{
		int N;
		scanf("%d", &N);
		for(int k=0; k < N; k++)
		{
			int v = 0;
			for(int i=0; i < N; i++)
			{
				int d;
				scanf("%1d", &d);
				if( d == 1) v = i;
			}
			Values[k] = v;
		}
		int swapCount = 0;
		for(int i=0; i < N; i++)
		{
			int m = -1;
			for(int j = i; j < N; j++) 
			{
				if( Values[j] <= i ) 
				{
					m = j;
					break;
				}
			}
			swapCount += m - i;
			int val = Values[m];
			for(int k=m; k > i; k--) Values[k] = Values[k-1];
			Values[i] = val;
		}
		printf("Case #%d: %d\n", test, swapCount);
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif
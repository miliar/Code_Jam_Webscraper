#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(99903,"Code Jam 03")
#endif

const int MAX_SIZE = 19;
const char Sample[MAX_SIZE+1] = "welcome to code jam";

int result[MAX_SIZE+1];

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int T ;
	scanf("%i\n", &T);
	for(int k=1; k <= T; k++)
	{
		char c;
		result[0]=1;
		for(int i=1; i <= MAX_SIZE; i++) result[i] = 0;
		while( ((c=getchar()) != '\0') && (c != '\n') && (c != '\r'))
		{
			for(int i=0; i <= MAX_SIZE; i++)
			{
				if( c == Sample[i])
				{
					result[i+1] += result[i];
					result[i+1] %= 10000;
				}
			}
		}
		int r = result[MAX_SIZE];
		printf("Case #%i: %i%i%i%i\n", k, r/1000, (r/100 %10), (r/10 %10), (r%10));
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif
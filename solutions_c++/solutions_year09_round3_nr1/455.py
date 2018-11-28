#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(GCJ9-R1B1,"Code Jam 2009-R1B1")
#endif

const int MAX_LEN = 64;

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int T;
	scanf("%i", &T);
	for(int t=0; t < T; t++)
	{
		char buf[MAX_LEN];
		char lettres[MAX_LEN];
		int base = 0;
		scanf("%s", buf);
		int len = strlen(buf);
		int result[MAX_LEN];
		for(int i=0; i < len; i++)
		{
			bool bNew = true;
			for(int k=0; k < base; k++) 
			{
				if( lettres[k] == buf[i])
				{
					bNew = false;
					if( k == 0) result[i] = 1;
					else if( k == 1) result[i] = 0;
					else result[i] = k;
					break;
				}
			}
			if( bNew)
			{
				if( base == 0) result[i] = 1;
				else if( base == 1) result[i] = 0;
				else result[i] = base;
				lettres[base++] = buf[i];
			}
		}
		base = base == 1 ? 2 : base;
		long long int res = 0;
		long long int b = 1;
		for(int i=len-1; i >= 0; i--)
		{
			res += (long long int) b*result[i];
			b *= base;
		}
		printf("Case #%d: %lli\n", t+1, res);
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(99901,"Code Jam 01")
#endif

const int NUM_WORDS = 5000;
const int MAX_LEN = 15+1;

char Words[NUM_WORDS][MAX_LEN];
int nL,nD,nN;

int compare(const void *a, const void *b)
{
	return strcmp((const char*)a, (const char*)b);
}

int find(const char * str, int N)
{
	int low = 0;
	int high = nD-1;
	int mid;
	while( low <= high)
	{
		mid = (low + high)/2;
		int diff = strncmp(Words[mid], str, N );
		if( diff == 0)
		{
			return mid;
		}
		if( diff < 0 )
		{
			low = mid + 1;
		}
		else
		{
			high = mid - 1;
		}
	}
	return -1;
}

char val[MAX_LEN];
int gCount;
void Count(char *str, int lvl = 0)
{
	if( lvl > 0)
	{
		if(find(val, lvl) == -1) return;
	}
	switch(*str)
	{
	case '\0':
		{
			val[lvl] = '\0';
			if( find(val, lvl) != -1)
			{
				gCount += 1;
			}
		}
		break;
	case '(':
		{
			char * pos = strchr(str, ')');
			for(char * s = str + 1; s != pos; s++)
			{
				val[lvl] = *s;
				Count(pos+1, lvl+1);
			}
		}
		break;
	default:
		val[lvl] = *str;
		Count(str+1, lvl+1);
	}
}

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	scanf("%i %i %i\n", &nL, &nD, &nN);
	for(int i=0; i < nD; i++)
	{
		scanf("%s\n", Words[i]);
	}
	qsort(Words, nD, sizeof(char)*MAX_LEN, compare);
	char sample[1024];
	for(int i=1; i <= nN; i++)
	{
		scanf("%s\n", sample);
		gCount = 0;
		Count(sample);
		printf("Case #%i: %i\n", i, gCount);
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif
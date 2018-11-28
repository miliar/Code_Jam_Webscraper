#include <iostream>
#include <cstdio>
#include <algorithm>
#define MAX_L 1000
using namespace std;

int freq[MAX_L];

int compare(const void *a, const void *b)
{
	return *(int *)b - *(int *)a;
}

int main()
{
	int i, j;
	int t, T;
	int P,K,L;
	int repeat;
	long long result;
	
	scanf("%d", &T);

	for(t=1;t<=T;t++)
	{

		scanf("%d %d %d", &P, &K, &L);

		for(i=0;i<L;i++)
		{
			scanf("%d", &freq[i]);
		}
		qsort(freq, L, sizeof(int), compare);
		result = 0;
		repeat = 0;
		for(i=0;i<L;i++)
		{
			if( i % K==0 )
				repeat++;
			result += repeat * freq[i];
		}

		printf("Case #%d: %lld\n", t, result);
	}
	return 0;
}

#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, n) for( int i = 0; i < (int)(n); i++)

void main()
{
	int testCaseNum = 0;

	

	FILE* input = fopen("C:\\Projects\\Input\\C-small-attempt0.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\C-small-attempt0.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		uint64 range[10001] = { 0 };
		uint64 L = 0, H = 0;
		int possible = 0;
		uint64 N, min = -1;

		fscanf(input, "%llu %llu %llu", &N, &L, &H);

		FOR(j, N)
		{
			fscanf(input, " %llu", &range[j]);
		}
		
		for(uint64 j = L; j <= H; j++)
		{
			FOR(k, N)
			{
				if (!(range[k] % j == 0 || j % range[k] == 0))
				{
					break;
				}

				if(k == N-1)
				{
					min = j;
				}
			}

			if(min != -1)
			{
				possible = 1;
				break;
			}
		}

		if(possible)
		{
			fprintf(output, "Case #%d: %llu\r\n", i, min);
		}
		else
		{
			fprintf(output, "Case #%d: NO\r\n", i);
		}
		
	}
}
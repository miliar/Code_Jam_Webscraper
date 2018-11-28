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
	int N;

	FILE* input = fopen("C:\\Projects\\Input\\B-small-attempt1.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\B-small-attempt1.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		int C = 0, N = 0, L;
		uint64 types[10001] = { 0 };
		uint64 t = 0;

		fscanf(input, "%d %llu %d %d", &L, &t, &N, &C);

		FOR(j, C)
		{
			fscanf(input, " %llu", &types[j]);
		}

		uint64 sum = 0;
		uint64 idx = 0;
		FOR(j, N)
		{
			sum += types[j % C] * 2;
			if(sum >= t)
			{
				idx = j;
				break;
			}
		}

		uint64 max1 = (sum - t)/2;
		uint64 max1idx = idx;
		uint64 max2 = 0;
		uint64 max2idx = 0;
		for(uint64 j = idx + 1; j < N; j++)
		{
			if(types[j % C] > max1)
			{
				max2 = max1;
				max2idx = max1idx;
				max1 = types[j % C];
				max1idx = j;
			}
			else if(types[j % C] > max2 && L > 1)
			{
				max2 = types[j % C];
				max2idx = j;
			}
		}

		sum = 0;
		FOR(j, N)
		{
			sum += types[j % C] * 2;
		}

		if(L == 2)
		{
			sum = sum - max1 - max2;
		}
		else if (L == 1)
		{
			sum = sum - max1;
		}

		fprintf(output, "Case #%d: %llu\r\n", i, sum);
	}
}
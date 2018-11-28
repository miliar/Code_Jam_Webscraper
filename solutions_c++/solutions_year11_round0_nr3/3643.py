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

void main()
{
	int testCaseNum = 0;
	int N;

	FILE* input = fopen("C:\\Projects\\Input\\C-large.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\C-large.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		uint64 res = 0;
		int candy;
		uint64 sum = 0;
		int64 min = 0xFFFFFFFF;

		fscanf(input, "%d", &N);

		for (int j = 0; j < N; j++)
		{
			fscanf(input, " %d", &candy);
			
			if (candy < min)
			{
				min = candy;
			}

			res ^= candy;
			sum += candy;
		}

		if (res == 0)
		{
			fprintf(output, "Case #%d: %llu\r\n", i, sum-min);
		} 
		else
		{
			fprintf(output, "Case #%d: %s\r\n", i, "NO");
		}

		
	}
}
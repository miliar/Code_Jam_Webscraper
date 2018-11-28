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

void Dancing()
{
	int testCaseNum = 0;

	FILE* input = fopen("..\\..\\Input\\B-large.in", "rt");
	FILE* output = fopen("..\\..\\Output\\B-large.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		int N = 0;
		int S = 0;
		int p = 0;
		int googlers[101] = { 0 };
		int res = 0;
		int minRegular = 0;
		int minSpecial = 0;

		fscanf(input, "%d %d %d ", &N, &S, &p);

		minRegular = max(3*p - 2, 0);
		minSpecial = max(3*p - 4, 0);

		FOR(j, N)
		{
			fscanf(input, "%d ", &googlers[j]);
		}

		sort(googlers, googlers + N, greater<int>());

		FOR(j, N)
		{
			if(googlers[j] < minRegular)
			{
				break;
			}
			else if(googlers[j] == 0 && p > 0)
			{
				break;
			}
			res++;
		}

		int tempres = res;
		
		for(int j = tempres; j < tempres + S && j < N; j++)
		{
			if(googlers[j] < minSpecial)
			{
				break;
			}
			else if(googlers[j] == 0 && p > 0)
			{
				break;
			}
			res++;
		}

		fprintf(output, "Case #%d: %d\r\n", i, res);
	}
}
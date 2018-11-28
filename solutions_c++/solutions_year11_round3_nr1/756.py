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

	FILE* input = fopen("C:\\Projects\\Input\\A-large.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\A-large.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		int R = 0, C = 0;
		char grid[51][51] = { 0 };
		int possible = 1;

		fscanf(input, "%d %d", &R, &C);
		FOR(j, R)
		{
			FOR(k, C)
			{
				fscanf(input, " %c", &grid[j][k]);
			}
		}

		FOR(j, R)
		{
			FOR(k, C)
			{
				if(grid[j][k] == '#' && grid[j][k + 1] == '#' && grid[j + 1][k] == '#' && grid[j + 1][k + 1] == '#')
				{
					grid[j][k] = '/';
					grid[j][k+1] = '\\';
					grid[j+1][k] = '\\';
					grid[j+1][k+1] = '/';
				}
			}
		}

		FOR(j, R)
		{
			FOR(k, C)
			{
				if(grid[j][k] == '#')
				{
					possible = 0;
				}
			}
		}

		if(possible)
		{
			fprintf(output, "Case #%d: \r\n", i);
			FOR(j, R)
			{
				FOR(k, C)
				{
					fprintf(output, "%c", grid[j][k]);
				}
				fprintf(output, "\r\n");
			}
		}
		else
		{
			fprintf(output, "Case #%d: \r\nImpossible\r\n", i);
		}
	}
}
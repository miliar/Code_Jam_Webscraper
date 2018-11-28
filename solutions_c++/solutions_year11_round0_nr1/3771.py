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

typedef struct _pos
{
	char type;
	int pos;
	int lastTimeMoved;
} pos;

void main()
{
	int testCaseNum = 0;
	int N;

	FILE* input = fopen("C:\\Projects\\Input\\A-large.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\A-large.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		fscanf(input, "%d", &N);

		int timePassed = 0;
		pos bPos = { 'B', 1, 0 }, oPos = { 'O', 1, 0 };
		pos nextPos = { 0, 0, 0 };

		for (int j = 0; j < N; j++)
		{
			fscanf(input, " %c %d", &nextPos.type, &nextPos.pos);

			pos *posByType;

			if (nextPos.type == 'O')
			{
				posByType = &oPos;
			}
			else
			{
				posByType = &bPos;
			}

			if ( abs(nextPos.pos - posByType->pos) <= (timePassed - posByType->lastTimeMoved) )
			{
				timePassed += 1;
			}
			else
			{
				timePassed += abs(nextPos.pos - posByType->pos) - (timePassed - posByType->lastTimeMoved) + 1;
			}

			posByType->pos = nextPos.pos;
			posByType->lastTimeMoved = timePassed;
		}

		fprintf(output, "Case #%d: %d\r\n", i, timePassed);
	}
}
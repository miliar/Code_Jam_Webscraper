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
	char teams[101][101] = { '.' };
	

	FILE* input = fopen("C:\\Projects\\Input\\A-large.in", "rt");
	FILE* output = fopen("C:\\Projects\\Output\\A-large.out", "wt");	

	fscanf(input, "%d", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		fscanf(input, "%d", &N);
		double RPI[101] = { 0 };
		double OP[101] = { 0 };
		double WP[101] = { 0 };
		double OWP[101] = { 0 };
		double OOWP[101] = { 0 };

		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < N; k++)
			{
				fscanf(input, " %c", &teams[j][k]);

				if (teams[j][k] != '.')
				{
					OP[j]++;
					WP[j] += teams[j][k] - '0';
				}
			}

			if (OP[j] != 0) WP[j] = WP[j] / OP[j];
		}

		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < N; k++)
			{
				if (teams[j][k] != '.')
				{
					OWP[j] += (WP[k] * OP[k] - teams[k][j] + '0') / (OP[k] - 1);
				}
			}
			if (OP[j] != 0) OWP[j] = OWP[j] / OP[j];
		}

		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < N; k++)
			{
				if (teams[j][k] != '.')
				{
					OOWP[j] += OWP[k];
				}
			}
			if (OP[j] != 0) OOWP[j] = OOWP[j] / OP[j];

			RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
		}

		fprintf(output, "Case #%d: \r\n", i);

		for (int j = 0; j < N; j++)
		{
			fprintf(output, "%f\r\n", RPI[j]);
		}
	}
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <vector>
using namespace std;

FILE *fpIn, *fpOut;

bool *snappers;
bool *hasPower;

bool IsItOn(int N, int K)
{
	bool switch_ = false;

	for (int i = 0; i < N; ++i)
		snappers[i] = false; // initially all snappers is OFF.

	hasPower[0] = true; // left most snapper always has power.
	for (int i = 1; i < N; ++i)
		hasPower[i] = false;

	for (int i = 0; i < K; ++i)
	{
		/*
		for (int j = 1; j < N; ++j)
			if (snappers[j - 1] == true)
				hasPower[j] = true;
			else
				break;*/

		for (int j = 0; j < N; ++j)
		{
			if (hasPower[j] == true)
			{
				if (snappers[j] == true)
				{
					snappers[j] = false;
				}
				else
				{
					snappers[j] = true;
				}
			}
		}

		for (int j = 1; j < N; ++j)
		{
			if (hasPower[j - 1] == true && snappers[j - 1] == true)
			{
				hasPower[j] = true;
			}
			else
			{
				hasPower[j] = false;
				//break;
			}
		}

	}

	// if the last snapper is "ON" and it has power
	if (snappers[N - 1] == true && hasPower[N - 1] == true)
		return true;
	else
		return false;
}

int main()
{
	fpIn = fopen("c:\\gcj\\A-small-attempt0.in", "r");
	fpOut = fopen("c:\\gcj\\A-small-attempt0.out", "w");

	int numOfTestCase;
	fscanf(fpIn, "%d\n", &numOfTestCase);

	snappers = (bool *) malloc(30 * sizeof(bool));
	hasPower = (bool *) malloc(30 * sizeof(bool));

	for (int caseId = 1; caseId <= numOfTestCase; ++caseId)
	{
		printf("\nCase #%d ", caseId);

		int N, K;
		fscanf(fpIn, "%d %d\n", &N, &K);
		
		//////////////////////////////////////////////////

		fprintf(fpOut, "Case #%d: ", caseId);

		if (IsItOn(N, K))
			fprintf(fpOut, "ON");
		else
			fprintf(fpOut, "OFF");

		fprintf(fpOut, "\n");
	}

	free(snappers);
	free(hasPower);

	return 0;
}
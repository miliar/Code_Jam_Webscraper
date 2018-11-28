#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	FILE *pFileIn = fopen ("B.in", "r");
	FILE *pFileOut = fopen ("B_out.txt", "w");

	int nTestCases;
	int nGooglers;
	int nSurprises;
	int nGoal;

	fscanf (pFileIn, "%d", &nTestCases);

	for (int i = 0; i < nTestCases; i++)
	{
		fscanf (pFileIn, "%d%d%d", &nGooglers, &nSurprises, &nGoal);

		int count = 0;
		for (int j = 0; j < nGooglers; j++)
		{
			int nScore;
			fscanf (pFileIn, "%d", &nScore);

			if (nScore == 0 && nGoal != 0) continue;

			int nMedian = nScore / 3;
			int nRest = nScore % 3;
			
			if (nMedian >= nGoal)
				count++;
			else if (nMedian == nGoal - 1 && nRest > 0)
				count++;
			else if (nMedian == nGoal - 1 && nSurprises > 0)
			{
				count++;
				nSurprises--;
			}
			else if (nMedian == nGoal - 2 && nRest == 2 && nSurprises > 0)
			{
				count++;
				nSurprises--;
			}
		}

		fprintf (pFileOut, "Case #%d: %d\n", i + 1, count);
	}


	fclose (pFileIn);
	fclose (pFileOut);

	return 0;
}
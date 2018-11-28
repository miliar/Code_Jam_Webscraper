#pragma warning(disable:4996)

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cerr << "USAGE: " << argv[0] << " <input file name>" << endl;
		return 1;
	}

	FILE* fIn = fopen(argv[1], "r");

	if (fIn == NULL)
	{
		cerr << "CANNOT OPEN FILE: " << argv[1] << endl;
		return 2;
	}

	FILE* fOut = fopen("problemB.out", "w");

	char line[512];
	int noOfSamples = atoi(fgets(line, 512, fIn));

	for (int i=0; i<noOfSamples; i++)
	{
		fprintf(fOut, "Case #%d: ", i+1);

		fgets(line, 512, fIn);

		char *token = strtok(line, " ");
		int noOfDancers = atoi(token);

		token = strtok(NULL, " ");
		int noOfSurprises = atoi(token);

		token = strtok(NULL, " ");
		int bestScore = atoi(token);

		int bestTotal = bestScore >= 1 ? bestScore * 3 - 2 : 0;
		int bestTotalWithSurprises = bestScore >= 2 ? bestTotal - 2 : bestTotal;

		int noOfResults = 0;

		for (int j=0; j<noOfDancers; j++)
		{
			token = strtok(NULL, " ");
			int score = atoi(token);

			if (score >= bestTotal)
			{
				noOfResults++;
			}
			else if (noOfSurprises > 0 && score >= bestTotalWithSurprises)
			{
				noOfResults++;
				noOfSurprises--;
			}
		}

		fprintf(fOut, "%d\n", noOfResults);
	}

	fclose(fIn);
	fclose(fOut);

	return 0;
}

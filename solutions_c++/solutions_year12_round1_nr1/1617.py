#pragma warning(disable:4996)

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#include <vector>

using namespace std;

int powerOfTwo(int n)
{
	int result = 1;
	for (int i=0; i<n; i++)
	{
		result *= 2;
	}
	return result;
}

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

	FILE* fOut = fopen("problemA.out", "w");

	char line[128];
	int noOfSamples = atoi(fgets(line, 128, fIn));

	for (int i=0; i<noOfSamples; i++)
	{
		fprintf(fOut, "Case #%d: ", i+1);

		fgets(line, 128, fIn);

		int inputCharCount;
		int passLength;

		char *token = strtok(line, " \n");
		inputCharCount = atoi(token);
		token = strtok(NULL, " \n");
		passLength = atoi(token);
		//fscanf(fIn, "%d %d", &inputCharCount, &passLength);
printf("%d %d\n", inputCharCount, passLength);

		fgets(line, 128, fIn);
		token = strtok(line, " \n");

		std::vector<double> correctPos;
		int j = 0;
		do
		{
			correctPos.push_back(atof(token));
printf("%lf\n", atof(token));
			token = strtok(NULL, " \n");
			j++;
		}
		while (j < inputCharCount);
printf("\n");

		std::vector<std::vector<double> > matrix;
		for (int j=0; j<inputCharCount+1; j++)
		{
			std::vector<double> tmp;
			matrix.push_back(tmp);
		}

		double best = passLength + 2;
		for (int j=0; j<inputCharCount+1; j++)
		{
			double total = 0.0;

			for (int k=0; k<powerOfTwo(inputCharCount); k++)
			{
				double prob = 1.0;
				bool correct = true;
				for (int l=0; l<inputCharCount; l++)
				{
					if (powerOfTwo(l) & k)
					{ // lth input is false
						prob *= 1.0 - correctPos[l];
						if (inputCharCount - j > l)
						{
							correct = false;
						}
					}
					else
					{
						prob *= correctPos[l];
					}
				}

				int typeCount = correct ? passLength - inputCharCount + j*2 + 1 : 2*passLength - inputCharCount + j*2 + 2;

				total += typeCount * prob;
				printf("%lf : %d: %lf %d: %d %d\n", total, typeCount, prob, correct, inputCharCount, k);
			}
printf("\n");

			if (total < best)
			{
				best = total;
			}
		}

		fprintf(fOut, "%lf\n", best);
	}

	fclose(fIn);
	fclose(fOut);

	return 0;
}

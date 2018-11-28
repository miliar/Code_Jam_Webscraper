#pragma warning(disable:4996)

#include <iostream>
#include <sstream>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

inline int findNoOfDigits(long i)
{
	int result = 0;
	while (i > 0)
	{
		result++;
		i /= 10;
	}
	return result;
}

inline long power(long i, int j)
{
	long result = 1;
	for (int k=0; k<j; k++)
		result *= i;
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

	FILE* fOut = fopen("problemC.out", "w");

	char line[32];
	int noOfSamples = atoi(fgets(line, 32, fIn));

	for (int i=0; i<noOfSamples; i++)
	{
		fprintf(fOut, "Case #%d: ", i+1);

		fgets(line, 32, fIn);

		long minNo = atol(strtok(line, " \n"));
		long maxNo = atol(strtok(NULL, " \n"));

		int noOfDigits = findNoOfDigits(minNo);
		long noOfPairs = 0;

		for (long no=minNo; no<=maxNo; no++)
		{
			long candidate = no;
			set<long> candidates;
			for (int i=1; i<noOfDigits; i++)
			{
				candidate = candidate / 10l + (candidate % 10l) * power(10, noOfDigits-1);
				if (candidate > no && candidate <= maxNo && candidates.find(candidate) == candidates.end())
				{
					noOfPairs++;
					candidates.insert(candidate);
				}
			}
		}

		fprintf(fOut, "%ld\n", noOfPairs);
	}

	fclose(fIn);
	fclose(fOut);

	return 0;
}

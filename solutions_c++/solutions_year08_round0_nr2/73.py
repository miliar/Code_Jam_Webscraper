#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

#define PROB_LETTER "B"
#define INTYPE "large"

string findResult(FILE *inFile)
{
	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);
	int turnaroundTime;
	sscanf(inBuffer, "%d", &turnaroundTime);

	fgets(inBuffer, 1000, inFile);
	int numAToB;
	int numBToA;
	sscanf(inBuffer, "%d %d", &numAToB, &numBToA);

	vector<pair<int, int>> aToBTrips;
	vector<pair<int, int>> bToATrips;
	for(int i = 0; i < numAToB; i++)
	{
		int h1, m1, h2, m2;
		fgets(inBuffer, 1000, inFile);
		sscanf(inBuffer, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
		aToBTrips.push_back(make_pair(h1*60+m1, h2*60+m2));
	}
	for(int i = 0; i < numBToA; i++)
	{
		int h1, m1, h2, m2;
		fgets(inBuffer, 1000, inFile);
		sscanf(inBuffer, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
		bToATrips.push_back(make_pair(h1*60+m1, h2*60+m2));
	}

	sort(aToBTrips.begin(), aToBTrips.end());
	sort(bToATrips.begin(), bToATrips.end());

	int aToBIndex = 0;
	int bToAIndex = 0;

	int numNeededAtA = 0;
	int numNeededAtB = 0;

	int numAtA = 0;
	int numAtB = 0;

	vector<int> arrivalTimesAtA;
	vector<int> arrivalTimesAtB;

	while(1)
	{
		bool useA = true; // if false, use B

		// we're done!
		if (aToBIndex == aToBTrips.size() && bToAIndex == bToATrips.size())
			break;

		if (aToBIndex == aToBTrips.size())
			useA = false;
		else if (bToAIndex == bToATrips.size())
			useA = true;
		else
		{ // both are valid, so check which is earlier
			if (aToBTrips[aToBIndex].first < bToATrips[bToAIndex].first)
				useA = true;
			else
				useA = false;
		}

		if (useA)
		{
			int currentTime = aToBTrips[aToBIndex].first;

			for(int i = 0; i < arrivalTimesAtA.size(); i++)
			{ // handle arrivals
				if (arrivalTimesAtA[i] <= currentTime)
				{
					arrivalTimesAtA.erase(arrivalTimesAtA.begin() + i);
					numAtA++;
					i--;
				}
			}

			if (numAtA == 0)
			{
				numAtA++;
				numNeededAtA++;
			}

			numAtA--;
			arrivalTimesAtB.push_back(aToBTrips[aToBIndex].second + turnaroundTime);

			aToBIndex++;
		}
		else
		{ // use B
			int currentTime = bToATrips[bToAIndex].first;

			for(int i = 0; i < arrivalTimesAtB.size(); i++)
			{ // handle arrivals
				if (arrivalTimesAtB[i] <= currentTime)
				{
					arrivalTimesAtB.erase(arrivalTimesAtB.begin() + i);
					numAtB++;
					i--;
				}
			}

			if (numAtB == 0)
			{
				numAtB++;
				numNeededAtB++;
			}

			numAtB--;
			arrivalTimesAtA.push_back(bToATrips[bToAIndex].second + turnaroundTime);

			bToAIndex++;
		}
	}

	stringstream ss;
	ss << numNeededAtA << " " << numNeededAtB;
	return ss.str();
}

int main()
{
	char *inFilename = PROB_LETTER "-" INTYPE ".in";
	char *outFilename = PROB_LETTER "-" INTYPE ".out";

	FILE *inFile = fopen(inFilename, "r");
	FILE *outFile = fopen(outFilename, "w");

	if (inFile == NULL)
	{
		printf("inFile does not exist!\n");
		system("PAUSE");
		return 1;
	}
	if (outFile == NULL)
	{
		printf("Failed to open outFile!\n");
		system("PAUSE");
		return 1;
	}

	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);

	int numCases;
	sscanf(inBuffer, "%d", &numCases);

	for(int i = 1; i <= numCases; i++)
	{
		string result = findResult(inFile);

		fprintf(outFile, "Case #%d: %s\n", i, result.c_str());
	}

	fclose(inFile);
	fclose(outFile);

	printf("Success!\n");
	system("PAUSE");
}
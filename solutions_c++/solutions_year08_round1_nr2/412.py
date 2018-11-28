#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <math.h>

using namespace std;

#define PROB_LETTER "B"
#define INTYPE "small-attempt0"

#define SQR(x) ((x)*(x))

string readLine(FILE *inFile)
{
	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);
	string result = inBuffer;
	if (result.empty())
		return result;
	if (result[result.size() - 1] == '\n')
		result.resize(result.size() - 1);
	return result;
}

bool isGood(vector<bool> maltedVector, vector<vector<pair<int, bool> > > customerData)
{
	for(int i = 0; i < customerData.size(); i++)
	{
		bool customerGood = false;

		for(int j = 0; j < customerData[i].size(); j++)
		{
			if (maltedVector[customerData[i][j].first-1] == customerData[i][j].second)
			{
				customerGood = true;
				break;
			}
		}

		if (!customerGood)
			return false;
	}
	return true;
}

string findResult(FILE *inFile)
{
	string numFlavorsStr = readLine(inFile);
	string numCustomersStr = readLine(inFile);

	int numFlavors = atol(numFlavorsStr.c_str());
	int numCustomers = atol(numCustomersStr.c_str());

	// for each customer, for each flavor, the flavor followed by malted or not
	vector<vector<pair<int, bool> > > customerData;

	for(int i = 0; i < numCustomers; i++)
	{
		stringstream ssIn = stringstream(readLine(inFile));

		customerData.push_back(vector<pair<int, bool> >());

		int numPrefs;
		ssIn >> numPrefs;
		for(int i = 0; i < numPrefs; i++)
		{
			int flavor;
			bool malted;
			ssIn >> flavor >> malted;
			customerData.back().push_back(make_pair(flavor, malted));
		}
	}

	int bestMalted = 20;
	vector<bool> bestSet;

	for(int i = 0; i < (1 << numFlavors); i++)
	{
		vector<bool> malted;
		for(int j = 0; j < numFlavors; j++)
		{
			if (i & (1 << j))
				malted.push_back(true);
			else
				malted.push_back(false);
		}

		if (isGood(malted, customerData))
		{
			int numMalted = 0;
			for(int k = 0; k < malted.size(); k++)
				if (malted[k])
					numMalted++;

			if (numMalted < bestMalted)
			{
				bestMalted = numMalted;
				bestSet = malted;
			}
		}
	}

	stringstream ss;

	if (bestSet.empty())
	{
		ss << "IMPOSSIBLE";
	}
	else
	{
		for(int i = 0; i < bestSet.size(); i++)
		{
			ss << int(bestSet[i]) << " ";
		}
	}

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
		printf("Done with case #%d\n", i);
	}

	fclose(inFile);
	fclose(outFile);

	printf("Success!\n");
	system("PAUSE");
}
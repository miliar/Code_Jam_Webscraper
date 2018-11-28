#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define PROB_LETTER "A"
#define INTYPE "large"

string findResult(FILE *inFile)
{
	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);

	int numEngines;
	sscanf(inBuffer, "%d", &numEngines);

	vector<string> engines;

	for(int i = 0; i < numEngines; i++)
	{
		fgets(inBuffer, 1000, inFile);
		if (inBuffer[strlen(inBuffer)-1] == '\n')
			inBuffer[strlen(inBuffer)-1] = '\0';
		engines.push_back(inBuffer);
	}

	vector<string> queries;

	fgets(inBuffer, 1000, inFile);
	int numQueries;
	sscanf(inBuffer, "%d", &numQueries);

	for(int i = 0; i < numQueries; i++)
	{
		fgets(inBuffer, 1000, inFile);
		if (inBuffer[strlen(inBuffer)-1] == '\n')
			inBuffer[strlen(inBuffer)-1] = '\0';
		queries.push_back(inBuffer);
	}

	int numChanges = 0;
	
	for(int currentIndex = 0; currentIndex != queries.size();)
	{
		// try all states from this index and see which goes farthest
		int bestEngineDist = 0;
		int bestEngine = -1;

		for(int i = 0; i < engines.size(); i++)
		{ // i is the current engine
			for(int j = currentIndex;; j++)
			{ // j is the location in the queries
				if (j == queries.size() || queries[j] == engines[i])
				{
					if (j - currentIndex > bestEngineDist)
					{
						bestEngineDist = j - currentIndex;
						bestEngine = i;
					}
					break;
				}
			}
		}

		if (bestEngine == -1)
			printf("crap!\n");

		currentIndex += bestEngineDist;
		if (currentIndex == queries.size())
			break;

		numChanges++;
	}

	stringstream ss;
	ss << numChanges;
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
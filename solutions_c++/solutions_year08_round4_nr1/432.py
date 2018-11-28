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

#define PROB_LETTER "A"
#define INTYPE "large"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;

string readLine(FILE *inFile)
{
	static char inBuffer[1000000];
	fgets(inBuffer, 1000000, inFile);
	string result = inBuffer;
	if (result.empty())
		return result;
	if (result[result.size() - 1] == '\n')
		result.resize(result.size() - 1);
	return result;
}

#define MAX_VALUE 2000000000

vector<pair<int, int>> theNodes;

lld numChangesNeeded(int index, int desiredValue)
{
	if (index*2 >= theNodes.size())
	{
		if (desiredValue == theNodes[index].first)
			return 0;
		else
			return MAX_VALUE;
	}
	else
	{
		if (desiredValue)
		{ // looking for true
			if (theNodes[index].first)
			{ // AND gate
				lld withoutChange = numChangesNeeded(index*2, 1) + numChangesNeeded(index*2+1, 1);
				if (withoutChange >= MAX_VALUE)
					withoutChange = MAX_VALUE;

				if (!theNodes[index].second)
					return withoutChange;

				lld withChange = 1 + min(numChangesNeeded(index*2, 1),
										numChangesNeeded(index*2+1, 1));

				return min(withoutChange, withChange);
			}
			else
			{ // OR gate
				lld withoutChange = min(numChangesNeeded(index*2, 1),
										numChangesNeeded(index*2+1, 1));
				if (withoutChange >= MAX_VALUE)
					withoutChange = MAX_VALUE;

				if (!theNodes[index].second)
					return withoutChange;

				lld withChange = 1 + numChangesNeeded(index*2, 1) + numChangesNeeded(index*2+1, 1);

				return min(withoutChange, withChange);
			}
		}
		else
		{ // trying for false
			if (theNodes[index].first)
			{ // AND gate
				lld withoutChange = min(numChangesNeeded(index*2, 0),
										numChangesNeeded(index*2+1, 0));
				if (withoutChange >= MAX_VALUE)
					withoutChange = MAX_VALUE;

				if (!theNodes[index].second)
					return withoutChange;

				lld withChange = 1 + numChangesNeeded(index*2, 0) + numChangesNeeded(index*2+1, 0);

				return min(withoutChange, withChange);
			}
			else
			{ // OR gate
				lld withoutChange = numChangesNeeded(index*2, 0) + numChangesNeeded(index*2+1, 0);
				if (withoutChange >= MAX_VALUE)
					withoutChange = MAX_VALUE;

				if (!theNodes[index].second)
					return withoutChange;

				lld withChange = 1 + min(numChangesNeeded(index*2, 0),
										numChangesNeeded(index*2+1, 0));

				return min(withoutChange, withChange);
			}
		}
	}
}

string findResult(FILE *inFile)
{
	int numNodes, desiredValue;
	sscanf(readLine(inFile).c_str(), "%d %d", &numNodes, &desiredValue);

	theNodes.clear();
	theNodes.push_back(pair<int, int>());

	for(int i = 0; i < (numNodes-1)/2; i++)
	{
		int initValue, changeable;
		sscanf(readLine(inFile).c_str(), "%d %d", &initValue, &changeable);
		theNodes.push_back(make_pair(initValue, changeable));
	}

	for(int i = 0; i < (numNodes+1)/2; i++)
	{
		int boolValue;
		sscanf(readLine(inFile).c_str(), "%d", &boolValue);
		theNodes.push_back(make_pair(boolValue, 0));
	}

	stringstream ss;

	lld result = numChangesNeeded(1, desiredValue);

	if (result == MAX_VALUE)
		ss << "IMPOSSIBLE";
	else
		ss << result;

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
		printf("Done with case %d\n", i);
	}

	fclose(inFile);
	fclose(outFile);

	printf("Success!\n");
	system("PAUSE");
}
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

string findResult(FILE *inFile)
{
	string numItemsStr = readLine(inFile);

	int numItems;
	sscanf(numItemsStr.c_str(), "%d", &numItems);

	vector<int> vectorA;
	vector<int> vectorB;

	stringstream ssIn = stringstream(readLine(inFile));

	for(int i = 0; i < numItems; i++)
	{
		int newValue;
		ssIn >> newValue;
		vectorA.push_back(newValue);
	}

	stringstream ssIn2 = stringstream(readLine(inFile));

	for(int i = 0; i < numItems; i++)
	{
		int newValue;
		ssIn2 >> newValue;
		vectorB.push_back(newValue);
	}

	sort(vectorA.begin(), vectorA.end());
	sort(vectorB.begin(), vectorB.end());

	long long totalSum = 0;

	for(int i = 0; i < vectorA.size(); i++)
	{
		totalSum += vectorA[i] * vectorB[vectorB.size() - 1 - i];
	}

	stringstream ss;

	ss << totalSum;

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
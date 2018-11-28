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

#define PROB_LETTER "D"
#define INTYPE "small-attempt1"

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

string findResult(FILE *inFile)
{
	int permutationLength;
	sscanf(readLine(inFile ).c_str(), "%d", &permutationLength);
	string stringToCompress = readLine(inFile);

	vector<int> currentPermutation;
	for(int i = 0; i < permutationLength; i++)
		currentPermutation.push_back(i);

	lld result = 200000000;

	do
	{
		string newString;
		newString.resize(stringToCompress.size());
		for(int i = 0; i < stringToCompress.size(); i++)
		{
			int startIndex = i / permutationLength * permutationLength;
			newString[i] = stringToCompress[currentPermutation[i-startIndex] + startIndex];
		}

		lld newResult = 0;
		for(int i = 0; i < newString.size(); i++)
		{
			if (i == 0 || newString[i] != newString[i-1])
				newResult++;
		}

		result = min(result, newResult);
	} while(next_permutation(currentPermutation.begin(), currentPermutation.end()));

	stringstream ss;

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
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

#define PROB_LETTER "C"
#define INTYPE "small-attempt0"

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
	llu numItems, m, X, Y, Z;
	sscanf(readLine(inFile).c_str(), "%llu %llu %llu %llu %llu", &numItems, &m, &X, &Y, &Z);

	vector<llu> A;
	for(int i = 0; i < m; i++)
		A.push_back(atol(readLine(inFile).c_str()));

	vector<llu> speedLimitSequence;

	for(int i = 0; i < numItems; i++)
	{
		speedLimitSequence.push_back(A[i % m]);
		A[i % m] = (X * A[i % m] + Y * (i+1)) % Z;
	}

	// how many end in this index?
	vector<llu> numIncreasingSubsequences;

	for(int i = 0; i < speedLimitSequence.size(); i++)
	{
		llu newValue = 1;

		for(int j = 0; j < i; j++)
		{
			if (speedLimitSequence[i] > speedLimitSequence[j])
				newValue += numIncreasingSubsequences[j];
		}

		numIncreasingSubsequences.push_back(newValue % 1000000007);
	}

	stringstream ss;

	ss << accumulate(numIncreasingSubsequences.begin(), numIncreasingSubsequences.end(), 0LL) % 1000000007;

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
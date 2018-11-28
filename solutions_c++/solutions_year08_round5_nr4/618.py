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
#define INTYPE "small-attempt0"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;

vector<string> splitString(string s);
string readLine(FILE *inFile);

map<pair<int, int>, lld> theCache;

lld countWays(int x, int y)
{
	if (x < 0 || y < 0)
		return 0;

	if (theCache.find(make_pair(x, y)) != theCache.end())
		return theCache[make_pair(x, y)];

	lld result = 0;

	result += countWays(x-2, y-1);
	result %= 10007;
	result += countWays(x-1, y-2);
	result %= 10007;

	theCache[make_pair(x, y)] = result;
	return theCache[make_pair(x, y)];
}

string findResult(FILE *inFile)
{
	
	theCache.clear();

	int height, width, numRocks;
	sscanf(readLine(inFile).c_str(), "%d %d %d", &height, &width, &numRocks);

	for(int i = 0; i < numRocks; i++)
	{
		int r, c;
		sscanf(readLine(inFile).c_str(), "%d %d", &r, &c);
		theCache[make_pair(r-1, c-1)] = 0;
	}

	theCache[make_pair(0, 0)] = 1;

	stringstream ss;

	ss << countWays(height-1, width-1);

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

vector<string> splitString(string s)
{
	char *strBuffer = new char[s.size()+1];
	strcpy(strBuffer, s.c_str());
	vector<string> result;

	for(char *theStr = strtok(strBuffer, " "); theStr; theStr = strtok(NULL, " "))
		result.push_back(theStr);

	delete strBuffer;
	return result;
}

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

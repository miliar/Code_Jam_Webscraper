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

string stringToTest;
lld result;

void testValue(vector<int> &operations)
{
	if (operations.size() == stringToTest.size() - 1)
	{
		lld resultValue = 0;

		bool add = true;
		lld tmpValue = stringToTest[0] - '0';
		for(int i = 0; i < operations.size(); i++)
		{
			if (operations[i] == 0)
			{
				tmpValue *= 10;
				tmpValue += stringToTest[i+1] - '0';
			}
			else if (operations[i] == 1) // +
			{
				if (add)
					resultValue += tmpValue;
				else
					resultValue -= tmpValue;
				add = true;
				tmpValue = stringToTest[i+1] - '0';
			}
			else // == 2   -
			{
				if (add)
					resultValue += tmpValue;
				else
					resultValue -= tmpValue;
				add = false;
				tmpValue = stringToTest[i+1] - '0';
			}
		}

		if (add)
			resultValue += tmpValue;
		else
			resultValue -= tmpValue;

		if (resultValue % 2 == 0 || resultValue % 3 == 0 || resultValue % 5 == 0 || resultValue % 7 == 0)
			result++;
		
		return;
	}

	operations.push_back(0);
	testValue(operations);
	operations.pop_back();

	operations.push_back(1);
	testValue(operations);
	operations.pop_back();

	operations.push_back(2);
	testValue(operations);
	operations.pop_back();
}

string findResult(FILE *inFile)
{
	stringToTest = readLine(inFile);
	
	result = 0;

	vector<int> tmp;
	testValue(tmp); 

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
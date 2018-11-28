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
// GMP library available from http://gmplib.org/
//#include <gmp.h>
//#include <gmpxx.h>

using namespace std;

#define PROB_LETTER "B"
#define INTYPE "large"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;
//typedef mpz_class bigint;
//typedef mpq_class bigrat;
//typedef mpf_class bigfloat;

vector<string> splitString(string s);
string readLine(FILE *inFile);
vector<lld> readLongLine(FILE *inFile);
//vector<bigint> readBigintLine(FILE *inFile);

vector<lld> v;

lld d, ins, m, n;
lld dp[300][300];
#define NONE 270

lld mindist(lld a, lld b)
{
	return min(d + ins, abs(a-b));
}

lld calc(lld pos, lld after)
{
	if (pos == -1)
		return 0;
	if (dp[pos][after] == -1)
	{
		lld res = 1LL<<48;

		// remove
		res = min<lld>(res, calc(pos-1, after) + d);

		// insert after
		if (after != NONE)
		{
			for(int i = max<lld>(0, after - m); i <= min<lld>(255, after + m); i++)
			{
				if (i < after && v[pos] < after && v[pos] <= i)
					res = min(res, calc(pos, i) + ins);
				if (i > after && v[pos] > after && v[pos] >= i)
					res = min(res, calc(pos, i) + ins);
			}
		}

		// change
		if (after == NONE)
		{
			for(int i = 0; i <= 255; i++)
				res = min(res, calc(pos-1, i) + mindist(v[pos], i));
		}
		else
		{
			for(int i = max<lld>(0, after - m); i <= min<lld>(255, after + m); i++)
				res = min(res, calc(pos-1, i) + mindist(v[pos], i));
		}
		
		dp[pos][after] = res;
	}
	return dp[pos][after];
}

string findResult(FILE *inFile)
{
	fscanf(inFile, "%lld %lld %lld %lld\n", &d, &ins, &m, &n);

	v = readLongLine(inFile);

	for(int i = 0; i < 300; i++)
	{
		for(int j = 0; j < 300; j++)
			dp[i][j] = -1;
	}

	stringstream ss;

	ss << calc(v.size()-1, NONE);

	return ss.str();
}

int main()
{
	char *inFilename = PROB_LETTER "-" INTYPE ".in";
	char *outFilename = PROB_LETTER "-" INTYPE ".out";

	FILE *inFile = fopen(inFilename, "r");
	if (inFile == NULL)
	{
		printf("inFile does not exist!\n");
		system("PAUSE");
		return 1;
	}

	FILE *outFile = fopen(outFilename, "w");
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

vector<lld> readLongLine(FILE *inFile)
{
	vector<string> v = splitString(readLine(inFile));

	vector<lld> res;

	for(size_t i = 0; i < v.size(); i++)
	{
		lld val;
		sscanf(v[i].c_str(), "%lld", &val);
		res.push_back(val);
	}

	return res;
}
/*
vector<bigint> readBigintLine(FILE *inFile)
{
	vector<string> v = splitString(readLine(inFile));

	vector<bigint> res;

	for(size_t i = 0; i < v.size(); i++)
		res.push_back(bigint(v[i]));

	return res;
}
*/
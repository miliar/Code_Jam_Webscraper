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
// GMP libraries available from http://gmplib.org/
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

#define PROB_LETTER "C"
#define INTYPE "small-attempt0"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;
typedef mpz_class bigint;
typedef mpq_class bigrat;
typedef mpf_class bigfloat;

vector<string> splitString(string s);
string readLine(FILE *inFile);
vector<lld> readLongLine(FILE *inFile);
vector<bigint> readBigintLine(FILE *inFile);

set<pair<int,int> > curset;
set<pair<int,int> > bgset;

string findResult(FILE *inFile)
{
	curset.clear();
	bgset.clear();

	lld m;
	fscanf(inFile, "%lld", &m);

	for(int i = 0; i < m; i++)
	{
		lld x1,y1,x2,y2;
		fscanf(inFile, "%lld %lld %lld %lld", &x1, &y1, &x2, &y2);
		for(int j = min(x1,x2); j <= max(x1,x2); j++)
		{
			for(int k = min(y1,y1); k <= max(y1,y2); k++)
				curset.insert(make_pair(j,k));
		}
	}

	lld res = 0;
	while (curset.size())
	{
		bgset.clear();
		for(set<pair<int,int> >::iterator iter = curset.begin(); iter != curset.end(); iter++)
		{
			if (curset.count(make_pair(iter->first-1, iter->second)) ||
				curset.count(make_pair(iter->first, iter->second-1)))
			{
				bgset.insert(*iter);
			}

			if (curset.count(make_pair(iter->first-1, iter->second+1)))
				bgset.insert(make_pair(iter->first, iter->second+1));
		}
		curset.swap(bgset);
		res++;
	}

	stringstream ss;

	ss << res;

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

vector<bigint> readBigintLine(FILE *inFile)
{
	vector<string> v = splitString(readLine(inFile));

	vector<bigint> res;

	for(size_t i = 0; i < v.size(); i++)
		res.push_back(bigint(v[i]));

	return res;
}

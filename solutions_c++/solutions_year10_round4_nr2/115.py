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

#define PROB_LETTER "B"
#define INTYPE "large"

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


vector<lld> need;
vector<lld> costs;

lld dp[5000][20];

lld calc(lld pos, lld numused)
{
	if (pos >= costs.size())
	{
		if (numused >= need[pos-costs.size()])
			return 0;
		else
			return -2;
	}
	if (dp[pos][numused] == -1)
	{
		lld res = -2;

		for(int use = 0; use < 2; use++)
		{
			lld leftcost = calc(pos*2, numused + use);
			lld rightcost = calc(pos*2+1, numused + use);

			if (leftcost != -2 && rightcost != -2)
			{
				lld newcost = leftcost + rightcost + (use ? costs[pos] : 0);
				if (res == -2 ||
					newcost < res)
				{
					res = newcost;
				}
			}
		}

		dp[pos][numused] = res;
	}
	return dp[pos][numused];
}


string findResult(FILE *inFile)
{
	lld p;
	fscanf(inFile, "%lld", &p);

	need.clear();
	for(int i = 0; i < (1<<p); i++)
	{
		lld val;
		fscanf(inFile, "%lld", &val);
		need.push_back(p-val);
	}

	reverse(need.begin(), need.end());

	for(int i = 0; i < 5000; i++)
	{
		for(int j = 0; j < 20; j++)
			dp[i][j] = -1;
	}
	
	costs.clear();
	for(int i = 0; i < (1<<p)-1; i++)
	{
		lld val;
		fscanf(inFile, "%lld", &val);
		costs.push_back(val);
	}

	costs.push_back(0);
	reverse(costs.begin(), costs.end());

	lld res = calc(1, 0);

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

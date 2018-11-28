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
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

#define PROB_LETTER "A"
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

int dr[4] = { 1, 1, 1, 0, };
int dc[4] = {-1, 0, 1, 1, };

string findResult(FILE *inFile)
{
	vector<string> vs;

	int n, k;
	fscanf(inFile, "%d %d", &n, &k);

	for(int i = 0; i < n ;i++)
	{
		char buf[100000];
		fscanf(inFile, "%s", buf);
		vs.push_back(buf);
	}

	vector<string> newvs(n, string(n, ' '));

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			newvs[j][n-i-1] = vs[i][j];
		}
	}
	for(int i = 0; i < n; i++)
	{
		int nextopen = n-1;
		for(int j = n-1; j >= 0; j--)
		{
			if (newvs[j][i] == 'R' ||
				newvs[j][i] == 'B')
			{
				newvs[nextopen][i] = newvs[j][i];
				if (j != nextopen)
					newvs[j][i] = '.';
				nextopen--;
			}
		}
	}

	bool redwins = false;
	bool bluewins = false;

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			for(int l = 0; l < 4; l++)
			{
				int r = i;
				int c = j;

				bool redgood = true;
				bool bluegood = true;

				for(int m = 0; m < k; m++)
				{
					if (r < 0 || c < 0 || r >= n || c >= n ||
						newvs[r][c] != 'R')
					{
						redgood = false;
						break;
					}
					r += dr[l];
					c += dc[l];
				}
				r = i;
				c = j;
				for(int m = 0; m < k; m++)
				{
					if (r < 0 || c < 0 || r >= n || c >= n ||
						newvs[r][c] != 'B')
					{
						bluegood = false;
						break;
					}
					r += dr[l];
					c += dc[l];
				}

				if (redgood)
					redwins = true;
				if (bluegood)
					bluewins = true;
			}
		}
	}

	stringstream ss;

	if (redwins && bluewins)
		ss << "Both";
	else if (redwins)
		ss << "Red";
	else if (bluewins)
		ss << "Blue";
	else
		ss << "Neither";

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

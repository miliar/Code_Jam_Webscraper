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


string findResult(FILE *inFile)
{
	int k = (int)readLongLine(inFile)[0];

	vector<string> v;

	for(int i = 0; i < 2*k-1; i++)
	{
		v.push_back(readLine(inFile));
		while (v.back().size() < 2*k-1)
			v.back().push_back(' ');
	}
	
	vector<bool> vsym;

	for(int i = 0; i < 2*k-1; i++)
	{
		bool good = true;

		for(int j = 1; i-j >= 0 && i+j < 2*k-1; j++)
		{
			for(int l = 0; l < 2*k-1; l++)
			{
				if (v[l][i+j] != ' ' &&
					v[l][i-j] != ' ' &&
					v[l][i+j] != v[l][i-j])
				{
					good = false;
					break;
				}
			}
			if (!good)
				break;
		}

		vsym.push_back(good);
	}
	
	vector<bool> hsym;
	
	for(int i = 0; i < 2*k-1; i++)
	{
		bool good = true;
		
		for(int j = 1; i-j >= 0 && i+j < 2*k-1; j++)
		{
			for(int l = 0; l < 2*k-1; l++)
			{
				if (v[i+j][l] != ' ' &&
					v[i-j][l] != ' ' &&
					v[i+j][l] != v[i-j][l])
				{
					good = false;
					break;
				}
			}
			if (!good)
				break;
		}

		hsym.push_back(good);
	}
	/*
	int vnewk = -1;

	for(int i = 0; i < vsym.size(); i++)
	{
		if (vsym[i])
		{
			int newval = max<lld>(i, 2*k-1-1-i);
			newval++;
			if (vnewk == -1 ||
				newval < vnewk)
			{
				vnewk = newval;
			}
		}
	}

	
	int hnewk = -1;

	for(int i = 0; i < hsym.size(); i++)
	{
		if (hsym[i])
		{
			int newval = max(i, 2*k-1-1-i);
			newval++;
			if (hnewk == -1 ||
				newval < hnewk)
			{
				hnewk = newval;
			}
		}
	}

	int newk = max(vnewk, hnewk);
	*/
	int newk = -1;

	for(int i = 0; i < vsym.size(); i++)
	{
		for (int j = 0; j < hsym.size(); j++)
		{
			if (vsym[i] && hsym[j])
			{
				//int newval = max(i, max(j, max(2*k-1-1-i, 2*k-1-1-j)));
				//newval++;
				int newval = abs(i - (k-1)) + abs(j - (k-1)) + k;
				if (newk == -1 ||
					newval < newk)
				{
					newk = newval;
				}
			}
		}
	}

	stringstream ss;

	ss << (newk*newk - k*k);

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

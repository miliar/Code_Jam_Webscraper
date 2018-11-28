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
#define INTYPE "small-attempt2"

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

vector<int> primes;

bool isprime(int n)
{
	if (n < 2)
		return false;

	for(int i = 2; i*i <= n; i++)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}

lld pow10[] = {1, 10, 100, 1000, 10000, 100000, 1000000};

string findResult(FILE *inFile)
{
	primes.clear();

	lld d = readLongLine(inFile)[0];

	vector<lld> v = readLongLine(inFile);

	for(int i = 0; i < pow10[d]; i++)
	{
		if (isprime(i))
			primes.push_back(i);
	}

	set<lld> res;

	if (v.size() == 1)
	{
		res.insert(0);
		res.insert(1);
	}
	else
	{
		for(int i = 0; i < primes.size(); i++)
		{
			lld p = primes[i];

			if (v[0] >= p)
				continue;
			for(lld a = 0; a < p; a++)
			{
				lld b = (((v[1] - v[0] * a) % p) + p) % p;

				bool good = true;
				for(int j = 0; j+1 < v.size(); j++)
				{
					if ((v[j] * a + b) % p != v[j+1])
					{
						good = false;
						break;
					}
				}
				if (good)
					res.insert((v.back() * a + b) % p);
			}
		}
	}

	stringstream ss;

	if (res.size() == 0)
		ss << "CRAP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
	else if (res.size() == 1)
		ss << (*res.begin());
	else
		ss << "I don't know.";

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

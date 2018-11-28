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

#define PROB_LETTER "A"
#define INTYPE "large"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;

vector<string> splitString(string s);
string readLine(FILE *inFile);
vector<int> readIntLine(FILE *inFile);

bool good(vector<int> v)
{
	for(int i = 0; i < v.size(); i++)
	{
		if (v[i] > i)
			return false;
	}
	return true;
}

string findResult(FILE *inFile)
{
	int n = readIntLine(inFile)[0];

	vector<string> grid;

	for(int i = 0; i < n; i++)
	{
		grid.push_back(readLine(inFile));
	}

	vector<int> vals;

	for(int i = 0; i < grid.size(); i++)
	{
		int maxv = 0;

		for(int j = 0; j < grid[i].size(); j++)
		{
			if (grid[i][j] == '1')
				maxv = max(maxv, j);
		}
		vals.push_back(maxv);
	}

	int res = 0;

	for(int i = 0; i < vals.size(); i++)
	{
		for(int j = i; j < vals.size(); j++)
		{
			if (vals[j] <= i)
			{
				while(j != i)
				{
					swap(vals[j], vals[j-1]);
					res++;
					j--;
				}
				break;
			}
		}
	}

	//while(!good(vals))
	//{
	//	res++;
	//	int maxi = max_element(vals.begin(), vals.end()) - vals.begin();

	//	while(vals[maxi] > maxi)
	//	{
	//		swap(vals[maxi], vals[maxi+1]);
	//		maxi++;
	//	}

	//	vals.resize(maxi);
	//}

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

vector<int> readIntLine(FILE *inFile)
{
	vector<string> v = splitString(readLine(inFile));

	vector<int> res;

	for(size_t i = 0; i < v.size(); i++)
	{
		int val;
		sscanf(v[i].c_str(), "%d", &val);
		res.push_back(val);
	}

	return res;
}

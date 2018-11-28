#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

//const string PATH = "C-small-attempt0";
const string PATH = "C-small-attempt1";
//const string PATH = "C-large";
//const string PATH = "C";

int m[501][501];
int b[501][501];

int binomial(int n, int k)
{
	if(k == 0)
		return 1;
	if(n == 0)
		return 0;
	if(b[n][k] == -1)
	{
		b[n][k] = (binomial(n - 1, k - 1) + binomial(n - 1, k)) % 100003;
	}
	return b[n][k];
}

int f(int n, int k)
{
	if(k == 1)
	{
		return 1;
	}
	if(m[n][k] == -1)
	{
		m[n][k] = 0;
		for(int i = 0; i < n - k; i++)
		{
			if(k - i - 1 > 0)
			{
				m[n][k] = (m[n][k] + binomial(n - k - 1, i) * f(k, k - i - 1)) % 100003;
			}
		}
	}
	return m[n][k];
}

int main()
{
	memset(m, -1, sizeof(m));
	memset(b, -1, sizeof(m));
	stringstream inPath;
	inPath << PATH.c_str() << ".in";
	stringstream outPath;
	outPath << PATH.c_str() << ".out";
	ifstream inFile(inPath.str());
	ofstream outFile(outPath.str());
	int T;
	inFile >> T;
	for(int i = 0; i < T; i++)
	{
		int n;
		inFile >> n;
		int res = 0;
		for(int j = 1; j < n; j++)
		{
			res = (res + f(n, j)) % 100003;
		}
		outFile << "Case #" << (i+1) << ": " << res << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
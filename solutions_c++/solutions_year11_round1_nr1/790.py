#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int gcd(int m,int n)
{
	while(true)
	{
		if((m = m%n) == 0)
		{
			return n;
		}
		if((n = n%m) == 0)
		{
			return m;
		}
	}
}

void yuefen(int& a, int& b)
{
	int c = gcd(a, b);
	while (c != 1)
	{
		a /= c;
		b /= c;

		c = gcd(a, b);
	}
}

void solve()
{
	int caseNum;
	scanf("%d", &caseNum);

	for (int caseId = 1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ", caseId);

		long long n;
		int pd, pg;
		scanf("%I64d %d %d", &n, &pd, &pg);

		if (pd != 100 && pg == 100 ||
			pd != 0 && pg == 0)
		{
			printf("Broken\n");
			continue;
		}
		
		int c = 100;
		yuefen(pd, c);

		bool bOK = false;
		if (n >= c)
		{
			bOK = true;
		}
		if (bOK)
		{
			printf("Possible\n");
		}
		else
		{
			printf("Broken\n");
		}
	}
}

int main()
{
	char directoryName[] = "C:\\Documents and Settings\\GaoGuang\\My Documents\\Downloads\\";
	char dataFileName[]= "A-large";
	char inputFileName[256];
	char outputFileName[256];
	strcpy(inputFileName, directoryName);
	strcat(inputFileName, dataFileName);
	strcat(inputFileName, ".in");

	strcpy(outputFileName, directoryName);
	strcat(outputFileName, dataFileName);
	strcat(outputFileName, ".out");

	freopen(inputFileName, "r", stdin);
	freopen(outputFileName, "w", stdout);

	solve();

	return 0;
}
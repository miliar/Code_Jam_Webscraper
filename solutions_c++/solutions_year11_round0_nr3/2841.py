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

void solve(const vector<int>& candy)
{
	int cnt  = candy.size();
	int ans = -1;
	for (int i =  (1 << cnt) - 2; i > 0; i--)
	{
		int sa, sb;
		sa = sb = 0;
		int ta, tb;
		ta = tb = 0;

		for (int j = 0; j < cnt; j++)
		{
			if ((i & (1 << j)) == 0)
			{
				sa ^= candy[j];
				ta += candy[j];
			}
			else
			{
				sb ^= candy[j];
				tb += candy[j];
			}
		}

		if (sa == sb && max(ta, tb) > ans)
		{
			ans = max(ta, tb);
		}
	}

	if (-1 == ans)
	{
		printf("NO\n");
	}
	else
	{
		printf("%d\n", ans);
	}
}

void solve()
{
	int caseNum;
	scanf("%d", &caseNum);

	for (int caseId = 1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ", caseId);

		int num;
		scanf("%d", &num);
		vector<int> candy;
		candy.resize(num);
		for (int i = 0; i < num; i++)
		{
			scanf("%d", &candy[i]);
		}

		solve(candy);
	}
}

int main()
{
	char directoryName[] = "C:\\Documents and Settings\\GaoGuang\\My Documents\\Downloads\\";
	char dataFileName[]= "C-small-attempt0";
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
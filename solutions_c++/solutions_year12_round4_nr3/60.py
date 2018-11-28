#pragma comment (linker, "/STACK:64000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int n;
int x[2010];
double par[2010];
int result[2010];
vector<vector<int> > ch;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		cin >> n;
		ch.clear();
		ch.resize(n);
		for (int i = 0; i < n - 1; i++)
		{
			cin >> x[i];
			x[i]--;
			ch[x[i]].push_back(i);
		}
		int fail = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (x[i] > j && x[j] > x[i])
					fail = 1;
		if (!fail)
		{
			par[n - 1] = 0;
			result[n - 1] = 1000000000;
			for (int i = n - 1; i >= 0; i--)
			{
				double p = par[i];
				for (int j = 0; j < ch[i].size(); j++)
				{
					int cur = ch[i][j];
					result[cur] = int(result[i] - 1 - (i - cur) * p);
					par[cur] = p = 1.0 * (result[i] - result[cur]) / (i - cur);
				}
			}
			printf("Case #%d: ", testCount + 1);
			for (int i = 0; i < n; i++)
				printf("%d ", result[i]);
			printf("\n");

			//////
			int ff = 0;
			for (int i = 0; i < n; i++)
			{
				if (result[i] < 0)
					ff = 1;
				double t = 1.0 * (result[x[i]] - result[i]) / (x[i] - i);
				for (int j = i + 1; j < n; j++)
					if (j != x[i] && 1.0 * (result[j] - result[i]) / (j - i) >= t)
						ff = 1;
			}
			if (ff)
				printf("FAIL\n");
			/////
		}
		else
			printf("Case #%d: Impossible\n", testCount + 1);
	}
	return 0;
}
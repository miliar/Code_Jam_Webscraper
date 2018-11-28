#define _USE_MATH_DEFINES
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;
#pragma warning(disable : 4996 4018)
#pragma comment(linker, "/STACK:16777216")

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	string w = "welcome to code jam";

	char bf[1000];
	gets(bf);
	int T;
	sscanf(bf, "%i", &T);

	for(int t = 0; t < T; t++)
	{
		int DP[19] = {};
		gets(bf);
		for(int i = 0; bf[i]; i++)
		{
			for(int j = 0; j < 19; j++)
			{
				if(bf[i] != w[j])
					continue;
				if(j)
					DP[j] = (DP[j] + DP[j - 1]) % 10000;
				else
					DP[j]++;
			}
		}
		printf("Case #%i: %04i\n", t + 1, DP[18]);
	}

	return 0;
}

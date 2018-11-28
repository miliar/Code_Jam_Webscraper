//Made by diver_ru, made with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <memory.h>
#include <fstream>

std::string NAME = "B-large";
using namespace std;

typedef long long int64;

int N, P;
int maxMiss[1050];
int cost[20][1050];
bool b[20][1050];

int64 tab[20][1010][20];

int64 rec(int level, int id, int missed)
{
	int64 &res = tab[level][id][missed];
	if (res != -1)
		return res;
	res = 2000000000;
	if (level == P && missed <= maxMiss[id])
		res = 0;
	else if (level < P)
	{
		res = cost[level][id] + rec(level + 1, id * 2, missed)
				+ rec(level + 1, id * 2 + 1, missed);
		res = min(res, rec(level + 1, id * 2, missed + 1) + rec(level + 1, id * 2 + 1, missed + 1));
	}
	return res;
}

int solve()
{
	return (int)rec(0, 0, 0);
}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cin >> P;
		N = 1 << P;
		memset(b, 0, sizeof b);
		memset(tab, -1, sizeof tab);
		int t = N / 2;
		for (int j = 0; j < N; ++j)
			cin >> maxMiss[j];
		for (int j = P - 1; j >= 0; --j, t /= 2)
		{
			for (int k = 0; k < t; ++k)
				cin >> cost[j][k];
		}

		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}
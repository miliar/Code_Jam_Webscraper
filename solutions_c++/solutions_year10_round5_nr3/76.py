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

std::string NAME = "C-small-attempt0";
using namespace std;

typedef long long int64;

map<int, int> a;

int solve()
{
	int res = 0;
	while (true)
	{
		map<int, int>::iterator it = a.begin();
		while (it != a.end() && it->second == 1)
			++it;
		if (it == a.end())
			return res;
		int x = it->first, v = it->second;
		if (v == 2)
			a.erase(it);
		else
			it->second -= 2;
		++a[x - 1];
		++a[x + 1];
		++res;
	}
}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}

	int testCount;
	cin >> testCount;
	for (int testNo = 1; testNo <= testCount; ++testNo)
	{
		int C;
		cin >> C;
		a.clear();
		for (int i = 0; i < C; ++i)
		{
			int x, v;
			cin >> x >> v;
			a[x] = v;
		}
		int64 res = solve();
		if (res == -1)
			cout << "Case #" << testNo << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << testNo << ": " << res << endl;
	}

	return 0;
}
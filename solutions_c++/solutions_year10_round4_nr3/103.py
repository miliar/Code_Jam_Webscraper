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

bool a[2][110][110];

int solve()
{
	int res = 1;
	int cur = 0;
	for (; ; ++res, cur = 1 - cur)
	{
		int next = 1 - cur;
		memset(a[next], 0, sizeof a[next]);
		bool was = false;
		for (int i = 0; i <= 100; ++i)
			for (int j = 0; j <= 100; ++j)
			{
				if (a[cur][i][j])
					a[next][i][j] = i > 0 && a[cur][i - 1][j] || j > 0 && a[cur][i][j - 1];
				else
					a[next][i][j] = i > 0 && j > 0 && a[cur][i - 1][j] && a[cur][i][j - 1];
				was |= a[next][i][j];
			}
		if (!was)
			break;
	}
	return res;
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
		int R;
		cin >> R;
		memset(a, 0, sizeof a);
		for (int j = 0; j < R; ++j)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int y = y1; y <= y2; ++y)
				for (int x = x1; x <= x2; ++x)
					a[0][y][x] = true;
		}
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}
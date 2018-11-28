#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <functional>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF = 1000000000;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

int n, m;
int bmask;
int a[10];

int d[11][1025];

int rec (int row, int cannot)
{
	if (row == n)
		return 0;
	
	if (d[row][cannot] != -1)
		return d[row][cannot];

	int res = rec (row+1, a[row+1]);
	int gmask = (~cannot) & bmask;
	for (int mask = gmask; mask != 0; mask = (mask - 1) & gmask)
	{
		bool ok = true;
		for (int i = 1; i < m; ++i)
			if ((mask & (1 << i)) && (mask & (1 << (i-1))))
			{
				ok = false;
				break;
			}
		if (!ok)
			continue;

		int nmask = 0;
		int cc = 0;
		for (int i = 0; i < m; ++i)
			if (mask & (1 << i))
			{
				++cc;
				//nmask |= 1 << i;
				if (i > 0) nmask |= 1 << (i-1);
				if (i < m - 1) nmask |= 1 << (i+1);
			}

		res = max(res, rec(row + 1, nmask | a[row+1]) + cc);
	}

	return d[row][cannot] = res;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cerr << test << endl;
		cin >> n >> m;
		bmask = (1 << m) - 1;
		for (int i = 0; i < n; ++i)
		{
			string s;
			cin >> s;
			int cur = 0;
			for (int j = 0; j < m; ++j)
				if (s[j] == 'x')
					cur |= 1 << j;
			a[i] = cur;
		}

		memset(d, 255, sizeof d);

		printf("Case #%d: %d\n", test, rec(0, a[0]));
	}

}
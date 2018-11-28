#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
typedef long long lint;
const int INF = 2000000000;

int n;
const int MAXW = 250;
bool f[MAXW][MAXW];

pair<int, int> die[100000], born[100000];
int dc = 0, bc = 0;

bool check()
{
	bool ok = true;
	for (int i = 0; i < MAXW && ok; i++)
		for (int j = 0; j< MAXW && ok; j++)
			ok = !f[i][j];
	return !ok;
}

void go()
{
	dc = 0; bc = 0;
	for (int i = 0; i < MAXW; i++)
		for (int j = 0; j < MAXW; j++)
			if (f[i][j])
			{
				if (!f[i - 1][j] && !f[i][j - 1])
					die[dc++] = mp(i, j);
			}
			else
				if (f[i - 1][j] && f[i][j - 1])
					born[bc++] = mp(i, j);

	for (int i = 0; i < dc; i++)
		f[die[i].first][die[i].second] = false;

	for (int i = 0; i < bc; i++)
		f[born[i].first][born[i].second] = true;
}

bool solve(int case_num)
{
	memset(f, 0, sizeof(f));
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int r = y1; r <= y2; r++)
			for (int c = x1; c <= x2; c++)
				f[r][c] = true;
	}

	int ans = 0;
	while (check())
	{
		ans++;
		go();
	}

	printf("Case #%d: ", case_num);
	//answer
	printf("%d", ans);
	//======
	printf("\n");
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
		solve(i + 1);
	return 0;
}
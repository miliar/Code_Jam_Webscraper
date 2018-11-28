#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <set>
#include <queue>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair

char grid[5][5];

bool isAll(int i, int j, int di, int dj, char x)
{
	while(i < 4 && i >= 0 && j < 4 && j >= 0)
	{
		if(grid[i][j] == x || grid[i][j] == 'T') i+=di, j+=dj;
		else return false;
	}
	return true;
}

const char* solve()
{
	int comp = 1;
	int xwin = 0, ywin = 0;

	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(grid[i][j] == '.') comp = 0;

	for(int i = 0; i < 4; ++i)
	{
		if(isAll(i, 0, 0, 1, 'X')) xwin = 1;
		if(isAll(i, 0, 0, 1, 'O')) ywin = 1;
		if(isAll(0, i, 1, 0, 'X')) xwin = 1;
		if(isAll(0, i, 1, 0, 'O')) ywin = 1;
	}

	if(isAll(0, 0, 1, 1, 'X')) xwin = 1;
	if(isAll(0, 0, 1, 1, 'O')) ywin = 1;
	if(isAll(0, 3, 1, -1, 'X')) xwin = 1;
	if(isAll(0, 3, 1, -1, 'O')) ywin = 1;

	if(xwin) return "X won";
	else if(ywin) return "O won";
	else if(comp) return "Draw";
	else return "Game has not completed";
}

int main (void)
{
	int n;
	cin >> n;

	for(int c = 1; c <= n; ++c)
	{
		for(int i = 0; i < 4; ++i) cin >> grid[i];

		printf("Case #%d: %s\n", c, solve());
	}

	return 0;
}

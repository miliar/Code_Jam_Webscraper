#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.1415926535;

int t;
string d[4];

bool check(char c)
{
	for (int i = 0; i < 4; ++i)
	{
		bool temp = true;
		for (int j = 0; j < 4; ++j)
			if (d[i][j] != c && d[i][j] != 'T')
				temp = false;
		if (temp)
			return true;
	}
	for (int j = 0; j < 4; ++j)
	{
		bool temp = true;
		for (int i = 0; i < 4; ++i)
			if (d[i][j] != c && d[i][j] != 'T')
				temp = false;
		if (temp)
			return true;
	}
	bool temp = true;
	for (int i = 0; i < 4; ++i)
		if (d[i][i] != c && d[i][i] != 'T')
			temp = false;
	if (temp)
		return true;
	temp = true;
	for (int i = 0; i < 4; ++i)
		if (d[i][3-i] != c && d[i][3-i] != 'T')
			temp = false;
	if (temp)
		return true;
	return false;
}

bool is_draw()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (d[i][j] == '.')
				return false;
	return true;
}

int main()
{
#ifdef MYLOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cin >> t;
	for (int cnt = 0; cnt < t; ++cnt)
	{
		for (int i = 0; i < 4; ++i)
			cin >> d[i];
		cout << "Case #" << cnt+1 << ": ";
		if (check('X'))
			cout << "X won\n";
		else if (check('O'))
			cout << "O won\n";
		else if (is_draw())
			cout << "Draw\n";
		else
			cout << "Game has not completed\n";
	}

	return 0;
}
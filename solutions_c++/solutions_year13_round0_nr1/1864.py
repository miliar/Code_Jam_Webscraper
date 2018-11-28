#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

char s[10][10];

bool check(char c)
{
	int i, j;
	for (i = 0; i < 4; ++i)
	{
		for (j = 0; j < 4 && (s[i][j] == c || s[i][j] == 'T'); ++j);
		if (j == 4)
			return true;
	}
	for (i = 0; i < 4 && (s[i][i] == c || s[i][i] == 'T'); ++i);
	if (i == 4)
		return true;
	for (i = 0; i < 4 && (s[i][4 - i - 1] == c || s[i][4 - i - 1] == 'T'); ++i);
	if (i == 4)
		return true;
	return false;
}

void solve(int t)
{
	int i, j, u;
	for (i = 0; i < 4; ++i)
		scanf("%s", s[i]);
	printf("Case #%d: ", t + 1);
	for (u = 0; u < 2; ++u)
	{
		if (check('X'))
		{
			printf("X won\n");
			return;
		}
		if (check('O'))
		{
			printf("O won\n");
			return;
		}
		for (i = 0; i < 4; ++i)
			for (j = i; j < 4; ++j)
				swap(s[i][j], s[j][i]);
	}
	for (i = 0; i < 4; ++i)
		for (j = 0; j < 4; ++j)
			if (s[i][j] == '.')
			{
				printf("Game has not completed\n");
				return;
			}
	printf("Draw\n");
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, i;
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
	{
		solve(i);
	}
	return 0;
}
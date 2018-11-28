//============================================================================
// Name        : A.cpp
// Author      : kangaroo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
using namespace std;

char a[10][10];

bool win(char ch)
{
	int cnt, T = 0;
	for (int i = 0; i < 4; ++i)
	{
		cnt = T = 0;
		for (int j = 0; j < 4; ++j){
			if (a[i][j] == ch)
				cnt++;
			if (a[i][j] == 'T')
				cnt++;
		}
		if (cnt == 4 || (cnt == 3 && T == 1))
			return true;
	}

	for (int j = 0; j < 4; ++j)
	{
		cnt = T = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (a[i][j] == ch)
				cnt++;
			if (a[i][j] == 'T')
				cnt++;
		}
		if (cnt == 4 || (cnt == 3 && T == 1))
			return true;
	}

	cnt = T = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (a[i][i] == ch)
			cnt++;
		if (a[i][i] == 'T')
			cnt++;
	}
	if (cnt == 4 || (cnt == 3 && T == 1))
			return true;

	cnt = T = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (a[i][3 - i] == ch)
			cnt++;
		if (a[i][3 - i] == 'T')
			cnt++;
	}
	if (cnt == 4 || (cnt == 3 && T == 1))
			return true;

	return false;
}

bool full()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (a[i][j] == '.') return false;
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int casenum = 1; casenum <= T; ++casenum)
	{
		for (int i = 0; i < 4; ++i)
			scanf("%s\n", a[i]);
		printf("Case #%d: ", casenum);
		if (win('X'))
			printf("X won\n");
		else if (win('O'))
			printf("O won\n");
		else if (full())
			printf("Draw\n");
		else printf("Game has not completed\n");
	}
	scanf("\n");
	return 0;
}

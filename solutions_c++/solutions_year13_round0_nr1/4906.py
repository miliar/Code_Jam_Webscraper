#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n = 4;
char a[4][4];

inline bool check_row(int row, char ch)
{
	int t = 0, c = 0;
	for (int j = 0; j < n; ++j)
	{
		if (a[row][j] == ch) ++c;
		if (a[row][j] == 'T') ++t;
	}
	return c == 4 || (c == 3 && t == 1);
}

inline bool check_col(int col, char ch)
{
	int t = 0, c = 0;
	for (int i = 0; i < n; ++i)
	{
		if (a[i][col] == ch) ++c;
		if (a[i][col] == 'T') ++t;
	}
	return c == 4 || (c == 3 && t == 1);
}

inline bool check_d1(char ch)
{
	int t = 0, c = 0;
	for (int i = 0; i < n; ++i)
	{
		if (a[i][i] == ch) ++c;
		if (a[i][i] == 'T') ++t;
	}
	return c == 4 || (c == 3 && t == 1);
}

inline bool check_d2(char ch)
{
	int t = 0, c = 0;
	for (int i = 0; i < n; ++i)
	{
		if (a[i][n - 1 - i] == ch) ++c;
		if (a[i][n - 1 - i] == 'T') ++t;
	}
	return c == 4 || (c == 3 && t == 1);
}

inline string solve()
{
	for (int i = 0; i < n; ++i)
		scanf("%s\n", a[i]);
	for (int i = 0; i < n; ++i)
		if (check_row(i, 'O')) return "O won";
	for (int j = 0; j < n; ++j)
		if (check_col(j, 'O')) return "O won";
	for (int i = 0; i < n; ++i)
		if (check_row(i, 'X')) return "X won";
	for (int j = 0; j < n; ++j)
		if (check_col(j, 'X')) return "X won";
	if (check_d1('O') || check_d2('O')) return "O won";
	if (check_d1('X') || check_d2('X')) return "X won";
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (a[i][j] == '.') return "Game has not completed";
	return "Draw";
}

int main()
{
	int tt;
	scanf("%d\n", &tt);
	for (int t = 0; t < tt; ++t)
		printf("Case #%d: %s\n", t + 1, solve().c_str());
	return 0;
}

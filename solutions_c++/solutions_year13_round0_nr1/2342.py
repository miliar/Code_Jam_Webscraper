#ifndef CANT_USE_TEMPLATE
#define  _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

#define MP make_pair
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()
#define sqr(x) ((x)*(x))
#endif

#define  TASK ""

const int N = 4;
char a[N][N];

int res()
{
	if (a[0][0] == a[1][1] && a[1][1] == a[2][2] && a[2][2] == a[3][3] && a[0][0] != '.')
		return a[0][0] == 'X' ? 1 : 2;
	if (a[0][3] == a[1][2] && a[1][2] == a[2][1] && a[2][1] == a[3][0] && a[0][3] != '.')
		return a[0][3] == 'X' ? 1 : 2;
	for (int i = 0; i < 4; i++)
		if (a[i][0] == a[i][1] && a[i][1] == a[i][2] && a[i][2] == a[i][3] && a[i][0] != '.')
			return a[i][0] == 'X' ? 1 : 2;
	for (int j = 0; j < 4; j++)
		if (a[0][j] == a[1][j] && a[1][j] == a[2][j] && a[2][j] == a[3][j] && a[0][j] != '.')
			return a[0][j] == 'X' ? 1 : 2;
	return 0;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(TASK ".in", "r", stdin);
	//freopen(TASK ".out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int k = 0; k < t; k++)
	{
		int I = -1, J = -1;
		bool flag = false;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
			{
				cin >> a[i][j];
				if (a[i][j] == 'T')
					I = i, J = j;
				flag |= a[i][j] == '.';
			}
		
		if (I != -1 && J != -1)
			a[I][J] = 'X';
		cout << "Case #" << k + 1 << ": ";
		if (res() == 1)
		{
			cout << "X won\n";
			continue;
		}
		if (res() == 2)
		{
			cout << "O won\n";
			continue;
		}
		if (I != -1 && J != -1)
			a[I][J] = 'O';
		if (res() == 1)
		{
			cout << "X won\n";
			continue;
		}
		if (res() == 2)
		{
			cout << "O won\n";
			continue;
		}
		if (flag)
			cout << "Game has not completed\n";
		else
			cout << "Draw\n";
	}
	return 0;
}
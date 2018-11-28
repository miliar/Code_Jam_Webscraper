#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>
#include <memory.h>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

#define INF 1234567890

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned int uint;

struct p3d
{
	int x, y, z;
	p3d(int _x, int _y, int _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}
};

struct p3d_d
{
	double x, y, z;
	p3d_d(double _x, double _y, double _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}
};

int64 C(int n, int k = 4)
{
	if (n < k)
		return 0;

	int64 res = 1;
	for (int i = n; i > n - k; --i)
		res *= i;
	for (int i = 1; i <= k; ++i)
		res /= i;

	return res;
}

int bs(int val, vector <int> &ar)
{
	int l = 0, r = ar.size() - 1;
	int res = ar.size();
	while (l <= r)
	{
		int m = (r + l) >> 1;

		if (ar[m] >= val)
		{
			res = m;
			r = m - 1;
		}
		else if (ar[m] < val)
			l = m + 1;
	}

	return res;
}

string str[4];

int chk_winner()
{
	char p = 'X', w = 'O';
	bool s1 = true, s2 = true, s3 = true, s4 = true;
	bool t1 = true, t2 = true, t3 = true, t4 = true;
	bool full = true;
	for (int i = 0; i < 4; ++i)
	{
		if (str[i][i] != 'T' && str[i][i] != p)
			s3 = false;
		if (str[i][3 - i] != 'T' && str[i][3 - i] != p)
			s4 = false;

		if (str[i][i] != 'T' && str[i][i] != w)
			t3 = false;
		if (str[i][3 - i] != 'T' && str[i][3 - i] != w)
			t4 = false;

		s1 = true, s2 = true;
		t1 = true, t2 = true;
		for (int j = 0; j < 4; ++j)
		{
			if (str[i][j] != p && str[i][j] != 'T')
				s1 = false;
			if (str[j][i] != p && str[j][i] != 'T')
				s2 = false;

			if (str[i][j] != w && str[i][j] != 'T')
				t1 = false;
			if (str[j][i] != w && str[j][i] != 'T')
				t2 = false;

			if (str[i][j] == '.')
				full = false;
		}

		if (s1 || s2)
			return 1; /// X won

		if (t1 || t2)
			return 2; /// O won
	}

	if (s3 || s4)
			return 1; /// X won

	if (t3 || t4)
		return 2; /// O won

	if (full)
		return 3; /// Draw

	return 0; /// Game has not completed
}

char res[4][50] = {"Game has not completed", "X won", "O won", "Draw"};

void task(int X)
{
	for (int i = 0; i < 4; ++i)
		cin >> str[i];
	
	cout << "Case #" << X << ": " << res[chk_winner()] << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
		task(i + 1);

	return 0;
}
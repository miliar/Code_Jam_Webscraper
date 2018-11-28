#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <limits.h>
#include <string>

using namespace std;

typedef long long int64;

int tmp[1200][1200];
int m[1200];
int d[1200][1200][12];
int mm[1200][1200];

int getMin(int l, int r)
{
	if (l == r)
		return m[l];
	if (mm[l][r] != -1)
		return mm[l][r];
	int r1 = l + (r - l + 1) / 2;
	int l1 = r1 - 1;
	return mm[l][r] = min(getMin(l, l1), getMin(r1, r));
}

int get(int l, int r, int c)
{
	if (d[l][r][c] != -1)
		return d[l][r][c];
	if (l == r)
		return 0;
	int mm = getMin(l, r);
	int r1 = l + (r - l + 1) / 2;
	int l1 = r1 - 1;
	if (mm == c)
	{
		return d[l][r][c] = tmp[l][r] + get(l, l1, c) + get(r1, r, c);
	}
	return d[l][r][c] = min(tmp[l][r] + get(l, l1, c) + get(r1, r, c), get(l, l1, c + 1) + get(r1, r, c + 1));
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		memset(tmp, 255, sizeof tmp);
		memset(d, 255, sizeof d);
		memset(mm, 255, sizeof mm);
		int  p;
		cin >> p;
		int sz = (1 << p);
		for (int i = 0; i < sz; i++)
		{
			scanf("%d", &m[i]);
		}
		for (int i = 0; i < p; i++)
		{
			for (int j = 0; j < sz; j += (1 << (i + 1)))
			{
				scanf("%d", &tmp[j][j + (1 << (i + 1)) - 1]);
			}
		}
		printf("Case #%d: ", test + 1);
		cout << get(0, sz - 1, 0) << endl;
	}
	return 0;
}
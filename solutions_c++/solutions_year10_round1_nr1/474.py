#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mp make_pair
typedef long long lint;

using namespace std;

char mas[51][51], ar[51][51];
int n, k;

int check1(int a, int b)
{
	if(a + k - 1 >= n)
		return 0;
	char now = ar[a][b];
	if(now != 'R' && now != 'B')
		return 0;
	int flag;
	if(now == 'R')
		flag = 1;
	else
		flag = 2;
	for(int i = a; i < a + k; ++i)
		if(ar[i][b] != now)
		{
			flag = 0;
			break;
		}
	return flag;
}

int check2(int a, int b)
{
	if(b + k - 1 >= n)
		return 0;
	char now = ar[a][b];
	if(now != 'R' && now != 'B')
		return 0;
	int flag;
	if(now == 'R')
		flag = 1;
	else
		flag = 2;
	for(int i = b; i < b + k; ++i)
		if(ar[a][i] != now)
		{
			flag = 0;
			break;
		}
	return flag;
}

int check3(int a, int b)
{
	if(a + k - 1 >= n || b + k - 1 >= n)
		return 0;
	char now = ar[a][b];
	if(now != 'R' && now != 'B')
		return 0;
	int flag;
	if(now == 'R')
		flag = 1;
	else
		flag = 2;
	for(int i = 0; i < k; ++i)
		if(ar[a + i][b + i] != now)
		{
			flag = 0;
			break;
		}
	return flag;
}

int check4(int a, int b)
{
	if(a + k - 1 >= n || b + 1 - k < 0)
		return 0;
	char now = ar[a][b];
	if(now != 'R' && now != 'B')
		return 0;
	int flag;
	if(now == 'R')
		flag = 1;
	else
		flag = 2;
	for(int i = 0; i < k; ++i)
		if(ar[a + i][b - i] != now)
		{
			flag = 0;
			break;
		}
	return flag;
}

int Solution()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		char x;
		scanf("%d%d", &n, &k);
		for(int j = 0; j < n; ++j)
		{
			scanf("%c", &x);
			for(int ind = 0; ind < n; ++ind)
				scanf("%c", &mas[j][ind]);
		}
		for(int j = 0; j < n; ++j)
			for(int p = 0; p < n; ++p)
				ar[j][p] = '.';
		for(int j = n - 1; j >= 0; --j)
		{
			int ind = n - 1;
			for(int l = n - 1; l >= 0; --l)
				if(mas[j][l] != '.')
				{
					ar[ind][n - 1 - j] = mas[j][l];
					ind--;
				}
		}
		int f1 = 0, f2 = 0;
		for(int j = 0; j < n; ++j)
			for(int ind = 0; ind < n; ++ind)
			{
				int p = check1(j, ind);
				if(p == 1)
					f1 = 1;
				if(p == 2)
					f2 = 2;

				p = check2(j, ind);
				if(p == 1)
					f1 = 1;
				if(p == 2)
					f2 = 2;

				p = check3(j, ind);
				if(p == 1)
					f1 = 1;
				if(p == 2)
					f2 = 2;

				p = check4(j, ind);
				if(p == 1)
					f1 = 1;
				if(p == 2)
					f2 = 2;
			}
		if(f1 && f2)
			printf("Case #%d: Both\n", i);
		if(f1 && !f2)
			printf("Case #%d: Red\n", i);
		if(!f1 && f2)
			printf("Case #%d: Blue\n", i);
		if(!f1 && !f2)
			printf("Case #%d: Neither\n", i);
	}
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	Solution();
	return 0;
}

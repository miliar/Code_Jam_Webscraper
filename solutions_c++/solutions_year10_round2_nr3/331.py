//Made by diver_ru, made with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <memory.h>
#include <fstream>

std::string NAME = "test";
using namespace std;

typedef long long int64;

const int MOD = 100003;

int tab[510][510];
int ctab[510][510];

int N;

int C(int n, int k)
{
	int &res = ctab[n][k];
	if (res != -1)
		return res;
	res = 0;
	if (k <= n)
	{
		if (k == n || k == 0)
			res = 1;
		else
			res = C(n - 1, k - 1) + C(n - 1, k);
	}
	return res %= MOD;
}

int rec(int n, int pos)
{
	int &res = tab[n][pos];
	if (res != -1)
		return res;
	int64 r = 0;
	if (pos == 1)
		r = 1;
	else
	{
		for (int j = max(1, pos - (n - pos)); j < pos; ++j)
		{
			r += rec(pos, j) * C(n - pos - 1, pos - j - 1);
			r %= MOD;
		}
	}
	return res = r % MOD;
}

int solve()
{
	int res = 0;
	for (int i = 1; i < N; ++i)
		res += rec(N, i);
	return res % MOD;
}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}
	int T;
	cin >> T;
	memset(tab, -1, sizeof tab);	
	memset(ctab, -1, sizeof ctab);
	for (int t = 1; t <= T; ++t)
	{
		cin >> N;
		cout << "Case #" << t << ": " << solve() << endl;
	}

	return 0;
}
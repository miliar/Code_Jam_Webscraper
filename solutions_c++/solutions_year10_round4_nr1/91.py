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

std::string NAME = "A-large";
using namespace std;

typedef long long int64;

int N, S;

vector<vector<char> > v;

inline void getSymOne(int &i, int &j)
{
	swap(i, j);
	i = S - i - 1;
	j = S - j - 1;
}

inline void getSymTwo(int &i, int &j)
{
	swap(i, j);
}

bool canBeGood(int si, int sj)
{
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			int ai = i + si, aj = j + sj;
			getSymOne(ai, aj);
			ai -= si; aj -= sj;
			if (ai >= 0 && aj >= 0 && ai < N && aj < N)
			{
				if (v[i][j] != v[ai][aj])
					return false;
			}
		}
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			int ai = i + si, aj = j + sj;
			getSymTwo(ai, aj);
			ai -= si; aj -= sj;
			if (ai >= 0 && aj >= 0 && ai < N && aj < N)
			{
				if (v[i][j] != v[ai][aj])
					return false;
			}
		}
	return true;
}

int solve()
{
	for (S = N; ; ++S)
	{
		for (int i = 0; i <= S - N; ++i)
			for (int j = 0; j <= S - N; ++j)
			{
				if (canBeGood(i, j))
					return S * S - N * N;
			}
	}
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
	for (int t = 1; t <= T; ++t)
	{
		cin >> N;
		v.assign(N, vector<char>());

		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j <= i; ++j)
			{
				int x;
				cin >> x;
				v[j].push_back(x + '0');
			}
		}
		for (int i = 1; i < N; ++i)
		{
			for (int j = i; j < N; ++j)
			{
				int x;
				cin >> x;
				v[j].push_back(x + '0');
			}
		}
		cout << "Case #" << t << ": " << solve() << endl;
	}

	return 0;
}
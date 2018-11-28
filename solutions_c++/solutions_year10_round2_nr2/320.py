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

int N, K, B, Tm;
vector<int> X, V;

int solve()
{
	int res = 0;
	while (N > 0 && (B - X.back()) <= V.back() * Tm)
	{
		--N;
		--K;
		X.pop_back();
		V.pop_back();
	}
	int cnt = 0;
	for (int i = N - 1; i >= 0 && K > 0; --i)
	{
		if ((B - X[i]) <= V[i] * Tm)
		{
			res += cnt;
			--K;
		}
		else
			++cnt;
	}
	return K > 0 ? -1 : res;
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
		cin >> N >> K >> B >> Tm;
		X.resize(N);
		for (int i = 0; i < N; ++i)
			cin >> X[i];
		V.resize(N);
		for (int i = 0; i < N; ++i)
			cin >> V[i];

		int res = solve();
		cout << "Case #" << t << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << endl;
	}

	return 0;
}
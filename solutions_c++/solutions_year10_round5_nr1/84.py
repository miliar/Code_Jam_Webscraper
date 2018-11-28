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


int a[20];
int K, D;
bool pr[1000010];

int64 powMod(int64 a, int p, int M)
{
	int64 res = 1;
	for (; p > 0; p /= 2)
	{
		if (p & 1)
			(res *= a) %= M;
		(a *= a) %= M;

	}
	return res;
}

int64 rev(int64 a, int p)
{
	return powMod(a, p - 2, p);
}

int64 norm(int64 a, int p)
{
	return (a % p + p) % p;
}

int solve()
{
	if (K == 1)
		return -1;
	if (K == 2)
		return a[0] == a[1] ? a[0] : -1;
	int start = 2;
	for (int i = 0; i < K; ++i)
		start = max(start, a[i]);
	int pw = 1;
	for (int i = 0; i < D; ++i)
		pw *= 10;
	int res = -1;
	for (int i = max(2, start + 1); i <= pw; ++i)
	{
		if (pr[i])
			continue;
		int64 A = norm(norm(a[1] - a[2], i) * rev(norm(a[0] - a[1], i), i), i);
		int64 B = ((a[1] - a[0] * A) % i + i) % i;
		bool ok = true;
		for (int j = 0; ok && j < K - 1; ++j)
			ok &= (a[j] * A + B) % i == a[j + 1];
		if (!ok)
			continue;
		int64 last = (a[K - 1] * A + B) % i;
		if (res == -1)
			res = (int)last;
		else if (res != last)
			return -1;
	}
	return res;
}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}

	for (int i = 2; i <= 1000000; ++i)
	{
		if (pr[i]) continue;
		for (int j = i + i; j <= 1000000; j += i)
			pr[j] = true;
	}


	int testCount;
	cin >> testCount;
	for (int testNo = 1; testNo <= testCount; ++testNo)
	{
		cin >> D >> K;
		for (int i = 0; i < K; ++i)
			cin >> a[i];
		int res = solve();
		if (res == -1)
			cout << "Case #" << testNo << ": " << "I don't know." << endl;
		else
			cout << "Case #" << testNo << ": " << res << endl;
	}

	return 0;
}
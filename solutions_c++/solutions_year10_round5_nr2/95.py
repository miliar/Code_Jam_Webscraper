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

std::string NAME = "B-small-attempt0";
using namespace std;

typedef long long int64;


int64 L;
int a[110];
int can[1001000];
int N;

int64 solve()
{
	int64 res = 0;
	sort(a, a + N);
	int64 x = a[N - 1];
	int64 cnt = L / x + 1;
	while (cnt > 0)
	{
		if (L - x * cnt > 1000000)
		{
			L -= x * cnt;
			res += cnt;
		}
		else
			cnt /= 2;
	}
	memset(can, 0, sizeof can);
	can[0] = 1;
	for (int i = 0; i < L; ++i)
	{
		if (!can[i])
			continue;
		for (int j = 0; j < N; ++j)
		{
			if (!can[i + a[j]] || can[i + a[j]] > can[i] + 1)
				can[i + a[j]] = can[i] + 1;
		}
	}
	if (can[L])
		return res + can[L] - 1;
	else
		return -1;
	}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}

	int testCount;
	cin >> testCount;
	for (int testNo = 1; testNo <= testCount; ++testNo)
	{
		cin >> L >> N;
		for (int i = 0; i < N; ++i)
			cin >> a[i];
		int64 res = solve();
		if (res == -1)
			cout << "Case #" << testNo << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << testNo << ": " << res << endl;
	}

	return 0;
}
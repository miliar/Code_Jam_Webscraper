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

/*/#ifndef ONLINE_JUDGE
FILE *fi = freopen("input.txt", "r", stdin), fo = *freopen("output.txt", "w", stdout);
#endif /**/
using namespace std;

typedef long long int64;

int R, k, N;
vector<int> g;

int64 modelStep(int &head)
{
	int oldHead = head;
	int64 am = 0;
	do
	{
		if (am + g[head] > k)
			break;
		am += g[head];
		(head += 1) %= N;
	}
	while (head != oldHead);
	return am;
}

int64 solve2()
{
	int head = 0;
	int64 res = 0;
	for (int i = 0; i < R; ++i)
	{
		res += modelStep(head);
	}
	return res;
}

int64 solve()
{
	vector<int64> was(N, -1);
	vector<int> trips(N, 0);
	int head = 0;
	int64 res = 0;
	int i = 0;

	for (; i < R; ++i)
	{
		if (was[head] != -1)
		{
			int64 delta = res - was[head];
			int cnt = i - trips[head];
			int skip = (R - i) / cnt;
			i += skip * cnt;
			res += delta * skip;
			break;
		}
		was[head] = res;
		trips[head] = i;
		
		res += modelStep(head);
	}		
	for (; i < R; ++i)
	{
		res += modelStep(head);
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cin >> R >> k >> N;
		g.resize(N);
		for (int j = 0; j < N; ++j)
			cin >> g[j];
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}
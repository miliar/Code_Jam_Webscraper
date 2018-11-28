#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int M;
int G[11000];
int C[11000];

PII F(int v)
{
	if (v >= (M+1)/2)
	{
		if (G[v] == 0)
			return PII(0, 100000);
		else
			return PII(100000, 0);
	}
	else
	{
		PII r1, r2;
		r1 = F(v*2);
		r2 = F(v*2+1);
		PII res(100000, 100000);
		if (G[v] == 0)
		{
			res.first = min(res.first, r1.first + r2.first);
			res.second = min(res.second, r1.first + r2.second);
			res.second = min(res.second, r1.second + r2.first);
			res.second = min(res.second, r1.second + r2.second);
			if (C[v] == 1)
			{
				res.second = min(res.second, r1.second + r2.second + 1);
				res.first = min(res.first, r1.first + r2.second + 1);
				res.first = min(res.first, r1.second + r2.first + 1);
				res.first = min(res.first, r1.first + r2.first + 1);
			}
		}
		else
		{
			res.second = min(res.second, r1.second + r2.second);
			res.first = min(res.first, r1.first + r2.second);
			res.first = min(res.first, r1.second + r2.first);
			res.first = min(res.first, r1.first + r2.first);
			if (C[v] == 1)
			{
				res.first = min(res.first, r1.first + r2.first + 1);
				res.second = min(res.second, r1.first + r2.second + 1);
				res.second = min(res.second, r1.second + r2.first + 1);
				res.second = min(res.second, r1.second + r2.second + 1);
			}
		}
		return res;
	}
}

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int V;
		scanf("%d%d", &M, &V);
		int i;
		int sz = (M-1)/2;
		for (i = 1; i <= sz; ++i)
		{
			scanf("%d%d", &G[i], &C[i]);
		}
		for (i; i <= M; ++i)
			scanf("%d", &G[i]);
		PII r = F(1);
		printf("Case #%d: ", t+1);
		if (V == 0)
		{
			if (r.first > M)
				printf("IMPOSSIBLE\n");
			else
				printf("%d\n", r.first);
		}
		else
		{
			if (r.second > M)
				printf("IMPOSSIBLE\n");
			else
				printf("%d\n", r.second);
		}

	}

	return 0;
};

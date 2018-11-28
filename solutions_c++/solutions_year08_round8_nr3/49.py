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

//#pragma comment(linker, "/STACK:100000000")

VInt E[530];

#define MOD 1000000009

int P[530];

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	vector<PII> A;
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int N;
		Int K;
		scanf("%d%lld", &N, &K);
		int i;
		A.clear();
		for (i = 0; i < N; ++i)
			E[i].clear();
		for (i = 0; i < N-1; ++i)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			--a;
			--b;
			A.PB(PII(a, b));
			E[a].PB(b);
			E[b].PB(a);
		}
		Int res = 1;
		queue<int> Q;
		Q.push(0);
		CLEAR(P, -1);
		while (!Q.empty())
		{
			int a = Q.front();
			Q.pop();
			Int m = K;
			if (P[a] != -1)
				m -= E[P[a]].size();
			if (m <= 0)
				m = 0;
			for (i = 0; i < SIZE(E[a]); ++i)
			{
				int b = E[a][i];
				if (b != P[a])
				{
					P[b] = a;
					Q.push(b);
					res = (res*m)%MOD;
					--m;
				}
			}
		}

		printf("Case #%d: %lld\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}


	return 0;
};

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

int K[2100];
int Q[2100][3100][2];
int U[2100];
int N, M;

int Mel[2100];

inline int getMel()
{
	int i, j;
	for (i = 0; i < M; ++i)
		if (U[i] == 0)
		{
			int r, k;
			k = 0;
			r = -1;
			for (j = K[i]-1; j >= 0; --j)
				if (Mel[Q[i][j][0]] == 0)
				{
					++k;
					if (Q[i][j][1] == 1)
						r = Q[i][j][0];
				}
			if (k == 1 && r != -1)
				return r;
		}
	return -1;
}

inline void setMel(int a)
{
	int i, j;
	for (i = 0; i < M; ++i)
		if (U[i] == 0)
		{
			for (j = K[i]-1; j >= 0; --j)
				if (Q[i][j][0] == a && Q[i][j][1] == 1)
				{
					U[i] = 1;
				}
		}
}

bool impossible()
{
	int i, j;
	for (i = 0; i < M; ++i)
		if (U[i] == 0)
		{
			int k;
			k = 0;
			for (j = K[i]-1; j >= 0; --j)
				if (Mel[Q[i][j][0]] == 0 && Q[i][j][1] == 0)
				{
					++k;
				}
			if (k == 0)
				return true;
		}
	return false;
}

int main()
{
//	freopen("B-small.in", "r", stdin);
//	freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		scanf("%d%d", &N, &M);
		int i, j;

		for (i = 0; i < M; ++i)
		{
			U[i] = 0;
			scanf("%d", &K[i]);
			for (j = 0; j < K[i]; ++j)
			{
				scanf("%d%d", &Q[i][j][0], &Q[i][j][1]);
				--Q[i][j][0];
			}
		}

		CLEAR(Mel, 0);
		int a;
		while ((a = getMel()) != -1)
		{
			Mel[a] = 1;
			setMel(a);
		}
		printf("Case #%d:", t+1);
		if (impossible())
			printf(" IMPOSSIBLE\n");
		else
		{
			for (i = 0; i < N; ++i)
				printf(" %d", Mel[i]);
			printf("\n");
		}

		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
};

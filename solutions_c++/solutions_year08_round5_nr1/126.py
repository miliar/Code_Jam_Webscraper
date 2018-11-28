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

int Mv[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0} };

#define MAX 6100
#define off 3050

int Y[MAX][MAX];
int KY[MAX];
int X[MAX][MAX];
int KX[MAX];

int P[MAX][MAX] = {0};

char S[40];

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	CLEAR(P, -1);

	for (t = 0; t < T; ++t)
	{
		int L;
		scanf("%d", &L);
		int N;
		int j, i;
		CLEAR(KY, 0);
		CLEAR(KX, 0);

		int x, y;
		x = y = 0;
		int d = 0;
		int nx, ny;
		for (j = 0; j < L; ++j)
		{
			scanf("%s%d", S, &N);
			int k;
			for (k = 0; k < N; ++k)
			{
				for (i = 0; S[i]; ++i)
				{
					if (S[i] == 'F')
					{
						nx = x + Mv[d][0];
						ny = y + Mv[d][1];
						if (x == nx)
						{
							int a = min(y, ny) + off;
							Y[a][KY[a]] = x + off;
							++KY[a];
						}
						else
						{
							int a = min(x, nx) + off;
							X[a][KX[a]] = y + off;
							++KX[a];
						}
						x = nx;
						y = ny;
						continue;
					}
					if (S[i] == 'R')
					{
						d = (d+1) & 3;
					}
					if (S[i] == 'L')
					{
						d = (d+3) & 3;
					}
				}
			}
		}
		int res = 0;
		for (i = 0; i < MAX; ++i)
			if (KY[i])
			{
				sort(Y[i], Y[i] + KY[i]);
				for (j = 1; j+1 < KY[i]; j += 2)
				{
					int e = Y[i][j+1];
					for (x = Y[i][j]; x < e; ++x)
					{
						if (P[x][i] != t)
						{
							++res;
							P[x][i] = t;
						}
					}
				}
			}
		for (i = 0; i < MAX; ++i)
			if (KX[i])
			{
				sort(X[i], X[i] + KX[i]);
				for (j = 1; j+1 < KX[i]; j += 2)
				{
					int e = X[i][j+1];
					for (y = X[i][j]; y < e; ++y)
					{
						if (P[i][y] != t)
						{
							++res;
							P[i][y] = t;
						}
					}
				}
			}
			printf("Case #%d: %d\n", t+1, res);
			fprintf(stderr, "%d\n", t+1);
	}

	return 0;
};

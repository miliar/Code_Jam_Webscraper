#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

#pragma comment(linker, "/STACK:47000000")

int Mv[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int B[110][110];
PII P[110][110];
int C[110][110];
PII F(PII a)
{
	if (a == P[a.first][a.second])
		return a;
	return P[a.first][a.second] = F(P[a.first][a.second]);
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
		int H, W;
		scanf("%d%d", &H, &W);
		int i, j;
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
				scanf("%d", &B[i][j]);
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
				P[i][j] = PII(i, j);
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
			{
				int d = -1;
				int mr = 1000000;
				int q;
				for (q = 0; q < 4; ++q)
				{
					int x = i + Mv[q][0];
					int y = j + Mv[q][1];
					if (x < 0 || x >= H || y < 0 || y >= W)
						continue;
					if (B[x][y] < mr)
					{
						mr = B[x][y];
						d = q;
					}
				}
				if (d != -1)
				{
					int x = i + Mv[d][0];
					int y = j + Mv[d][1];
					if (B[x][y] < B[i][j])
					{
						PII pa = F(PII(i, j));
						PII pb = F(PII(x, y));
						P[pa.first][pa.second] = pb;
					}
				}
			}

		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
				C[i][j] = -1;
		int cur = 0;
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
			{
				PII p = F(PII(i, j));
				if (C[p.first][p.second] == -1)
					C[p.first][p.second] = cur++;
			}
		if (cur > 26)
			throw 0;
		printf("Case #%d:\n", t+1);
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
			{
				PII p = F(PII(i, j));
				char c = 'a' + C[p.first][p.second];
				printf("%c%c", c, j == W-1 ? '\n' : ' ');
			}

		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}
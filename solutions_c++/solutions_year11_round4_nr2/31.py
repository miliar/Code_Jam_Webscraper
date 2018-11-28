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

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

char A[1 << 10][1 << 10];
Int SX[1 << 10][1 << 10];
Int SY[1 << 10][1 << 10];
Int SZ[1 << 10][1 << 10];

Int F(Int S[1 << 10][1 << 10], int x, int y, int xx, int yy)
{
	return S[xx][yy] + S[x][y] - S[xx][y] - S[x][yy];
}

int SolveTest(int test)
{
	int r, c, d;
	scanf("%d%d%d", &r, &c, &d);

	int i, j, k;
	FOR(i, 0, r)
		scanf("%s", A[i]);

	CLEAR(SX, 0);
	CLEAR(SY, 0);
	FOR(i, 0, r)
		FOR(j, 0, c)
		{
			SX[i + 1][j + 1] = SX[i + 1][j] + SX[i][j + 1] - SX[i][j] + (A[i][j] - '0' + d)*(i + i);
			SY[i + 1][j + 1] = SY[i + 1][j] + SY[i][j + 1] - SY[i][j] + (A[i][j] - '0' + d)*(j + j);
			SZ[i + 1][j + 1] = SZ[i + 1][j] + SZ[i][j + 1] - SZ[i][j] + (A[i][j] - '0' + d);
		}

	RFOR(k, r + 1, 3)
		FOR(i, 0, r + 1 - k)
			FOR(j, 0, c + 1 - k)
			{
				Int sx = F(SX, i, j, i + k, j + k) - F(SX, i, j, i + 1, j + 1) - F(SX, i, j + k - 1, i + 1, j + k) - F(SX, i + k - 1, j, i + k, j + 1) - F(SX, i + k - 1, j + k - 1, i + k, j + k);
				Int sy = F(SY, i, j, i + k, j + k) - F(SY, i, j, i + 1, j + 1) - F(SY, i, j + k - 1, i + 1, j + k) - F(SY, i + k - 1, j, i + k, j + 1) - F(SY, i + k - 1, j + k - 1, i + k, j + k);
				Int sz = F(SZ, i, j, i + k, j + k) - F(SZ, i, j, i + 1, j + 1) - F(SZ, i, j + k - 1, i + 1, j + k) - F(SZ, i + k - 1, j, i + k, j + 1) - F(SZ, i + k - 1, j + k - 1, i + k, j + k);

				if(sx % sz != 0 || sx/sz != i + i + k - 1)
					continue;
				if(sy % sz != 0 || sy/sz != j + j + k - 1)
					continue;

				printf("Case #%d: %d\n", test + 1, k);
				return 0;
			}

	printf("Case #%d: IMPOSSIBLE\n", test + 1);

	return 0;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};

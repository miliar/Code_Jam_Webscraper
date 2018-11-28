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

#define MAX 128
#define INF (1 << 30)

const int DX[] = {0, -1, 1, 0};
const int DZ[] = {0, 0, 0, 1};

int A[MAX];
int B[MAX];
int R[MAX][MAX][MAX];

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);

	int i, j, k;
	FOR(i, 0, N)
	{
		char buf[4];
		int a;
		scanf("%s%d", buf, &a);

		A[i] = a - 1;
		B[i] = buf[0] == 'O' ? 0 : 1;
	}

	FOR(i, 0, MAX)
		FOR(j, 0, MAX)
			FOR(k, 0, MAX)
				R[i][j][k] = INF;

	R[0][0][0] = 0;
	queue< pair<int, PII> > Q;
	Q.push(MP(0, PII(0, 0)));
	while(!Q.empty())
	{
		int x = Q.front().second.first;
		int y = Q.front().second.second;
		int z = Q.front().first;
		Q.pop();

		if(z == N)
		{
			printf("Case #%d: %d\n", test + 1, R[z][x][y]);
			return 0;
		}

		FOR(i, 0, 4)
			FOR(j, 0, 4)
			{
				int xx = x + DX[i];
				int yy = y + DX[j];
				int zz = z + DZ[i] + DZ[j];

				if(xx < 0 || xx >= MAX || yy < 0 || yy >= MAX)
					continue;
				if(DZ[i] != 0 && (A[z] != x || B[z] != 0))
					continue;
				if(DZ[j] != 0 && (A[z] != y || B[z] != 1))
					continue;
				if(R[zz][xx][yy] != INF)
					continue;

				R[zz][xx][yy] = R[z][x][y] + 1;
				Q.push(MP(zz, PII(xx, yy)));
			}
	}

	printf("Case #%d: %d\n", test + 1, -1);
	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

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

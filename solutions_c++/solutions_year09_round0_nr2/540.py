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

const int DX[] = {-1, 0, 0, 1};
const int DY[] = {0, -1, 1, 0};

int A[128][128];
vector<PII> Edge[128][128];
char R[128][128];

int SolveTest(int test)
{
	int H, W;
	scanf("%d%d", &H, &W);

	int i, j, k;
	FOR(i, 0, H)
		FOR(j, 0, W)
			scanf("%d", &A[i][j]);

	FOR(i, 0, H)
		FOR(j, 0, W)
		{
			int x = i;
			int y = j;
			FOR(k, 0, 4)
			{
				int xx = i + DX[k];
				int yy = j + DY[k];

				if(xx < 0 || xx >= H || yy < 0 || yy >= W || A[xx][yy] >= A[x][y])
					continue;

				x = xx;
				y = yy;
			}

			Edge[i][j].PB(PII(x, y));
			Edge[x][y].PB(PII(i, j));
		}

	CLEAR(R, 0);
	char c = 'a';
	FOR(i, 0, H)
		FOR(j, 0, W)
			if(R[i][j] == 0)
			{
				R[i][j] = c;
				++c;
				queue<PII> Q;
				Q.push(PII(i, j));
				while(!Q.empty())
				{
					int x = Q.front().first;
					int y = Q.front().second;
					Q.pop();

					FOR(k, 0, SIZE(Edge[x][y]))
					{
						int xx = Edge[x][y][k].first;
						int yy = Edge[x][y][k].second;

						if(R[xx][yy] == 0)
						{
							R[xx][yy] = R[x][y];
							Q.push(PII(xx, yy));
						}
					}
				}
			}

	FOR(i, 0, H)
		FOR(j, 0, W)
			Edge[i][j].clear();

	printf("Case #%d:\n", test + 1);
	FOR(i, 0, H)
		FOR(j, 0, W)
			printf("%c%c", R[i][j], j == W - 1 ? '\n' : ' ');

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
		SolveTest(t);

	return 0;
};

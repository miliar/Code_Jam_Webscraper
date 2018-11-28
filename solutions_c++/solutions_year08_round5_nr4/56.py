#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
using namespace std;

int dp[101][101];

int N;
int R, C;

set< pair<int, int> > mis;

int main()
{
	int t, ti;
	scanf("%d", &t);
	int i, j;
	for (ti = 1;ti <= t;ti++)
	{
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		mis.clear();
		scanf("%d %d %d", &R, &C, &N);

		for (i = 0;i < N;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q); p--; q--;
			mis.insert(make_pair(p, q));
		}

		for (i = 0;i < R;i++)
		{
			for (j = 0;j < C;j++)
			{
				{
					int nr = i + 2;
					int nc = j + 1;
					if (nr < R && nc < C && mis.find(make_pair(nr, nc)) == mis.end())
					{
						dp[nr][nc] += dp[i][j];
						dp[nr][nc] %= 10007;
					}
				}
				{
					int nr = i + 1;
					int nc = j + 2;
					if (nr < R && nc < C && mis.find(make_pair(nr, nc)) == mis.end())
					{
						dp[nr][nc] += dp[i][j];
						dp[nr][nc] %= 10007;
					}
				}
			}
		}
		printf("Case #%d: %d\n", ti, dp[R - 1][C - 1]);
	}
	return 0;
}

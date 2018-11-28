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

int dp[11][1 << 10];
char data[11][11];
int R, C;

int main()
{
	int t, ti;
	scanf("%d", &t);
	int i, j, k, l;
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d %d", &R, &C);
		for (i = 0;i < R;i++)
			scanf("%s", data[i]);

		memset(dp, 0x80, sizeof(dp));
		dp[0][0] = 0;

		for (i = 0;i < R;i++)
		{
			for (j = 0;j < (1 << C);j++)
			{
				if (dp[i][j] < 0)
					continue;
				for (k = 0;k < (1 << C);k++)
				{
					if (j & k)
						continue;
					int s = 0;
					for (l = 0;l < C;l++)
					{
						if (l != C - 1 && (k >> l) % 2 == 1 && (k >> (l + 1)) % 2 == 1)
							break;
						if (data[i][l] != '.' && (k >> l) % 2 == 1)
							break;
						s += (k >> l) % 2;
					}
					if (l != C)
						continue;
					int ne = (k >> 1) | ((k << 1) % (1 << C));
					if (dp[i + 1][ne] < dp[i][j] + s)
						dp[i + 1][ne] = dp[i][j] + s;
					if (ne == 511 && i + 1 == 9 && dp[i + 1][ne] == 47)
						i = i;
				}
			}
		}

		int ans = 0;
		for (j = 0;j < (1 << C);j++)
		{
			if (ans < dp[R][j])
				ans = dp[R][j];
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}

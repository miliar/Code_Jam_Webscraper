#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const int MAX_SIZE = 5;
int n, m;
int num[MAX_SIZE][MAX_SIZE];
int ans;
int bitCount(int x)
{
	return x > 0 ? bitCount(x >> 1) + (x & 1) : 0;
}
void dfs(int r, int cnt)
{
	if (r > n / 2 && cnt <= ans)
		return;
	if (r == n)
	{
		bool valid = true;
		for (int i = 0; i < n && valid; i++)
			for (int j = 0; j < m && valid; j++)
				if (num[i][j] != 0)
					valid = false;
		if (valid)
			ans = max(ans, cnt);
		return;
	}
	for (int s = 0; s < (1 << m); s++)
	{
		for (int i = max(0, r - 1); i <= min(n - 1, r + 1); i++)
			for (int j = 0; j < m; j++)
				num[i][j] -= (j > 0 && ((s >> (j - 1)) & 1) == 1)
					+ (((s >> j) & 1) == 1)
					+ (j < m - 1 && ((s >> (j + 1)) & 1) == 1);
		bool valid = true;
		for (int i = max(0, r - 1); i <= min(n - 1, r + 1) && valid; i++)
			for (int j = 0; j < m && valid; j++)
				if (num[i][j] < 0)
					valid = false;
		if (valid)
			dfs(r + 1, (r == n / 2) ? bitCount(s) : cnt);
		for (int i = max(0, r - 1); i <= min(n - 1, r + 1); i++)
			for (int j = 0; j < m; j++)
				num[i][j] += (j > 0 && ((s >> (j - 1)) & 1) == 1)
					+ (((s >> j) & 1) == 1)
					+ (j < m - 1 && ((s >> (j + 1)) & 1) == 1);
	}
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &num[i][j]);
		ans = 0;
		dfs(0, 0);
		printf("Case #%d: %d\n", testInd + 1, ans);
	}
	return 0;
}

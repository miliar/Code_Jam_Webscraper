#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;
int price[105][25];
int mat[105][105];

int mark[105], match[105];

int dfs(int root, int n)
{
	for (int i = 0; i < n; ++i) if (mark[i] == 0 && mat[root][i])
	{
		mark[i] = 1;
		if (match[i] == -1 || dfs(match[i], n))
		{
			match[i] = root;
			return 1;
		}
	}
	return 0;
}
int main()
{
freopen("r2\\C-large.in", "r", stdin);
freopen("r2\\C-large.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int id = 1;
	while (cas--)
	{
		int n, k;scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i) for (int j = 0; j < k; ++j) scanf("%d", price[i]+j);
		memset(mat, 0, sizeof mat);
		
		for (int i = 0; i < n; ++i) for (int j = i+1; j < n; ++j)
		{
			if (price[j][0] < price[i][0])
			{
				for (int s = 0; s < k; ++s) swap(price[i][s], price[j][s]);
			}
		}
		for (int i = 0; i < n; ++i) for (int j = i+1; j < n; ++j)
		{
			int ok = 1;
			for (int s = 0; s < k; ++s) if (price[j][s] <= price[i][s]) {ok = 0; break;}
			mat[i][j] = ok;
		}
		
		int ans = 0;
		memset(match, 255, sizeof match);
		for (int i = 0; i < n; ++i)
		{
			memset(mark, 0, sizeof mark);
			if (dfs(i, n)) ++ans;
		}
		printf("Case #%d: %d\n", id++, n - ans);
	}
	return 0;
}

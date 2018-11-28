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

const int MAX_N = 100000;
const int INF = 100000;

int n, x;
int f[MAX_N + 1][2];
int v[MAX_N + 1];
int c[MAX_N + 1];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d", &n, &x);
		for (int i = 1; i <= (n - 1) / 2; i++)
			scanf("%d%d", &v[i], &c[i]);
		int offset = (n - 1) / 2;
		for (int i = offset + 1; i <= offset + (n + 1) / 2; i++)
		{
			scanf("%d", &v[i]);
			f[i][v[i]] = 0;
			f[i][!v[i]] = INF;
		}
		for (int i = (n - 1) / 2; i >= 1; i--)
			for (int j = 0; j < 2; j++)
			{
				f[i][j] = INF;
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
					{
						if ((x & y) == j && (v[i] == 1 || c[i] == 1))
							f[i][j] = min(f[i][j], f[i * 2][x] + f[i * 2 + 1][y] + (v[i] != 1));
						if ((x | y) == j && (v[i] == 0 || c[i] == 1))
							f[i][j] = min(f[i][j], f[i * 2][x] + f[i * 2 + 1][y] + (v[i] != 0));
					}
			}
		if (f[1][x] >= INF)
			printf("Case #%d: %s\n", testInd + 1, "IMPOSSIBLE");
		else
			printf("Case #%d: %d\n", testInd + 1, f[1][x]);
	}
	return 0;
}

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

const int MAX_N = 16;
const int MAX_L = 50000;
const int INF = 500000;

int n, l;
char line[MAX_L];
int f[MAX_N][1 << MAX_N];
int g[MAX_N][MAX_N];

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d", &n);
		scanf("%s", line);
		l = strlen(line);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				for (int x = i, y = j; x < l && y < l; x += n, y += n)
					g[i][j] += (line[x] == line[y]);
		int answer = -INF;
		for (int start = 0; start < n; start++)
		{
			for (int i = 0; i < n; i++)
				fill(f[i], f[i] + (1 << n), -INF);
			f[start][1 << start] = 0;
			for (int s = 0; s < (1 << n); s++)
				for (int i = 0; i < n; i++)
					if (((s >> i) & 1))
					{
						for (int j = 0; j < n; j++)
							if (((s >> j) & 1) && f[j][s ^ (1 << i)] >= 0 && i != j)
								f[i][s] = max(f[i][s], f[j][s ^ (1 << i)] + g[j][i]);
					}
			for (int finish = 0; finish < n; finish++)
				if (f[finish][(1 << n) - 1] >= 0)
				{
					int cur = f[finish][(1 << n) - 1];
					for (int x = finish, y = start + n; x < l && y < l; x += n, y += n)
						cur += (line[x] == line[y]);
					answer = max(answer, cur);
				}
		}
		printf("Case #%d: %d\n", testInd + 1, l - answer);
	}
	return 0;
}

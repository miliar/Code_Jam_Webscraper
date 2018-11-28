#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define maxn 20
#define maxp 2000

int n, m;
int f[maxn][maxn];

int valid(int a, int b)
{
	for (int i = 0; i < m - 1; i++)
		if (((a >> i) % 2) && ((a >> (i + 1)) % 2))
			return 0;
	if (b == -1)
		return 1;
	for (int i = 0; i < m - 1; i++)
	{
		if (((a >> i) % 2) && ((b >> (i + 1)) % 2))
			return 0;
		if (((b >> i) % 2) && ((a >> (i + 1)) % 2))
			return 0;
	}
	return 1;
}

int vv(int a, int level)
{
	for (int i = 0; i < m; i++)
		if (((a >> i) % 2) && !f[level][i])
			return 0;
	return 1;
}

int cntv(int a)
{
	int res = 0;
	for (int i = 0; i < m; i++)
		res += (a >> i) % 2;
	return res;
}

int res[maxn][maxp];

int solve()
{
	for (int i = 0; i < (1 << m); i++)
		if (valid(i, -1) && vv(i, 0))
			res[0][i] = cntv(i);
		else
			res[0][i] = 0;
	for (int i = 1; i < n; i++)
		for (int j = 0; j < (1 << m); j++)
			if (valid(j, -1) && vv(j, i))
			{
				int best = -1;
				for (int k = 0; k < (1 << m); k++)
					if (valid(j, k))
						if (best == -1 || best < res[i - 1][k] + cntv(j))
							best = res[i - 1][k] + cntv(j);
				if (best + 1)
					res[i][j] = best;
				else
					res[i][j] = 0;
			}
			else
				res[i][j] = 0;
	int best = 0;
	for (int i = 0; i < (1 << m); i++)
		best = max(best, res[n - 1][i]);
	return best;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			char ss[maxn];
			scanf("%s", ss);
			for (int j = 0; j < m; j++)
				f[i][j] = ss[j] == '.';
		}
		printf("Case #%d: %d\n", test_count + 1, solve());
	}
	return 0;
}
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
#define maxn 32000

int c[maxn];
int g[maxn];
int a[maxn];
int m, v;

int min2(int a, int b)
{
	if (a == -1)
		return b;
	if (b == -1)
		return a;
	return min(a, b);
}

int find(int p)
{
	if (p > m / 2)
		if (a[p] == v)
			return 0;
		else
			return -1;
	int l = find(p * 2);
	int r = find(p * 2 + 1);
	if (l == -1 && r == -1)
		return -1;
	if (g[p] != v)
		return min2(l, r);
	if (l == -1 || r == -1)
		if (c[p])
			return min2(l, r) + 1;
		else
			return -1;
	if (min2(l, r) + 1 < l + r && c[p])
		return min2(l, r) + 1;
	return l + r;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d%d", &m, &v);
		for (int i = 1; i <= m / 2; i++)
			scanf("%d%d", &g[i], &c[i]);
		for (int i = m / 2 + 1; i <= m; i++)
			scanf("%d", &a[i]);
		int res = find(1);
		if (res + 1)
			printf("Case #%d: %d\n", test_count + 1, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", test_count + 1);
	}
	return 0;
}
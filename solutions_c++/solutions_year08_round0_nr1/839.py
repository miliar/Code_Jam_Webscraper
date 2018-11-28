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

#define MAX_N 201
#define MAX_M 2001

vs names;
vs q;
int n, m;

int a[MAX_M][MAX_N];

int solve()
{
	for (int i = 0; i <= m; i++)
		for (int j = 0; j < n; j++)
			a[i][j] = 1000000001;
	for (int i = 0; i < n; i++)
		a[0][i] = 0;
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
				if (k != j)
					a[i + 1][k] = min(a[i + 1][k], a[i][j] + 1);
			if (q[i] != names[j])
				a[i + 1][j] = min(a[i + 1][j], a[i][j]);
		}
	int res = 1000000001;
	for (int i = 0; i < n; i++)
		res = min(res, a[m][i]);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	char ss[32001];
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d", &n);
		gets(ss);
		names.resize(n);
		for (int i = 0; i < n; i++)
		{
			gets(ss);
			names[i] = ss;
		}
		scanf("%d", &m);
		gets(ss);
		q.resize(m);
		for (int i = 0; i < m; i++)
		{
			gets(ss);
			q[i] = ss;
		}
		printf("Case #%d: %d\n", test_count + 1, solve());
	}
	return 0;
}
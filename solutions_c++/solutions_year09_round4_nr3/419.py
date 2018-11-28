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

long long r[100][100];
int a[100][100];
int n, k;

void get_a()
{
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
		{
			int fail = 0;
			if (r[i][0] == r[j][0])
				fail = 1;
			for (int ii = 1; ii < k; ii++)
				if ((r[i][ii] - r[j][ii]) * (r[i][ii - 1] - r[j][ii - 1]) <= 0)
					fail = 1;
			a[i][j] = a[j][i] = !fail;
		}
}

int is_complete(int mask)
{
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			if ((mask >> i) % 2 == 1 && (mask >> j) % 2 == 1 && !a[i][j])
				return 0;
	return 1;
}

int solve()
{
	get_a();
	int res[80000];
	for (int i = 0; i < (1 << n); i++)
	{
		if (is_complete(i))
		{
			res[i] = 1;
			continue;
		}
		res[i] = 80000;
		for (int j = ((i - 1) & i); j; j = ((j - 1) & i))
			if (res[j] + res[i - j] < res[i])
				res[i] = res[j] + res[i - j];
	}
	return res[(1 << n) - 1];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				scanf("%lld", &r[i][j]);
		printf("Case #%d: %d\n", testCount + 1, solve());
	}
	return 0;
}
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

char f[80][80];
int a[80];
int n;

int solve()
{
	memfill(a, 0);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (f[i][j] == '1')
				a[i] = j;
	int used[80];
	memfill(used, 0);
	int p[80];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (!used[j] && a[j] <= i)
			{
				p[i] = j;
				used[j] = 1;
				break;
			}
	int w[80];
	for (int i = 0; i < n; i++)
		w[i] = i;
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		int st = 0;
		for (int j = 0; j < n; j++)
			if (w[j] == p[i])
				st = j;
		while (st != i)
		{
			swap(w[st], w[st - 1]);
			st--;
			res++;
		}
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", f[i]);
		printf("Case #%d: %d\n", testCount + 1, solve());
	}
	return 0;
}
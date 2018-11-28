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
#define maxn 130

int w, h;
long long f[maxn][maxn];

void setp(int x, int y, long long v)
{
	if (f[x][y] == -1)
		return;
	f[x][y] = (f[x][y] + v) % 10007;
}

long long solve()
{
	f[0][0] = 1;
	for (int i = 0; i < w; i++)
		for (int j = 0; j < h; j++)
			if (f[i][j] > 0)
			{
				setp(i + 2, j + 1, f[i][j]);
				setp(i + 1, j + 2, f[i][j]);
			}
	return f[w - 1][h - 1] % 10007;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		int r;
		scanf("%d%d%d", &w, &h, &r);
		memfill(f, 0);
		for (int i = 0; i < r; i++)
		{
			int ww, hh;
			scanf("%d%d", &ww, &hh);
			f[ww - 1][hh - 1] = -1;
		}
		printf("Case #%d: %lld\n", test_count + 1, solve());
	}
	return 0;
}
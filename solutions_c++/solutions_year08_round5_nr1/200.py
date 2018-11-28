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
#define maxn 1000000
#define maxm 210

int dirs[4][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};

char path[maxn];
int len;

int h[maxm][maxm];
int v[maxm][maxm];

int f[maxm][maxm];

void presolve()
{
	int x = 105, y = 105, d = 0;
	memfill(h, 0);
	memfill(v, 0);
	memfill(f, 0);
	for (int i = 0; i < len; i++)
	{
		switch (path[i])
		{
		case 'F':
			if (d == 0)
				v[y - 1][x] = 1;
			if (d == 1)
				h[y][x - 1] = 1;
			if (d == 2)
				v[y][x] = 1;
			if (d == 3)
				h[y][x] = 1;
			x += dirs[d][0];
			y += dirs[d][1];
			break;
		case 'L':
			d = (d + 1) % 4;
			break;
		case 'R':
			d = (d + 3) % 4;
			break;
		}
	}
	int u, w, last;
	for (int i = 0; i < maxm; i++)
	{
		u = w = 0;
		last = -1;
		for (int j = 0; j < maxm; j++)
			if (v[i][j])
				last = j;
		for (int j = 0; j <= last; j++)
		{
			if (!u && w)
				f[i + 1][j] = 1;
			if (v[i][j])
				u = !u;
			if (u)
				w = 1;
		}
	}
	for (int i = 0; i < maxm; i++)
	{
		u = w = 0;
		last = -1;
		for (int j = 0; j < maxm; j++)
			if (h[j][i])
				last = j;
		for (int j = 0; j <= last; j++)
		{
			if (!u && w)
				f[j][i + 1] = 1;
			if (h[j][i])
				u = !u;
			if (u)
				w = 1;
		}
	}
}

long long solve()
{
	presolve();
	long long res = 0;
	for (int i = 0; i < maxm; i++)
		for (int j = 0; j < maxm; j++)
			res += f[i][j];
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		int l;
		scanf("%d", &l);
		len = 0;
		for (int i = 0; i < l; i++)
		{
			char ss[80];
			int rn;
			scanf("%s%d", ss, &rn);
			int slen = strlen(ss);
			for (int j = 0; j < rn; j++)
			{
				memcpy(path + len, ss, slen);
				len += slen;
			}
		}
		printf("Case #%d: %lld\n", test_count + 1, solve());
	}
	return 0;
}
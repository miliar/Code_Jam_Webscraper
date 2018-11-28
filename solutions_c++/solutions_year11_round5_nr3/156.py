#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 1

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;

const int dx[] = {1, 0, 1,  1, -1,  0, -1, -1};
const int dy[] = {0, 1, 1, -1,  0, -1, -1,  1};
const char ch[] = "|-\\/";
const int N = 101;
int n, m;
int res[N][N];
int dir[N][N];
char s[N][N];
ll ans;

void move(int x, int y, int & x1, int & y1, int dir)
{
	x1 = (x + dx[dir] + n) % n;
	y1 = (y + dy[dir] + m) % m;
}

bool dfs(int x, int y, int p)
{
//	dbg("dfs(%d %d %d)\n", x, y, p);
	if (res[x][y] != -1)
		return res[x][y] == p;

	res[x][y] = p;
	int x1, y1;
	move(x, y, x1, y1, dir[x][y] + p * 4);
//	dbg("x1 = %d y1 = %d\n", x1, y1);
	for (int i = 0; i < 8; ++i)
	{
		int x2, y2;
		move(x1, y1, x2, y2, i);
		if (x2 == x && y2 == y)
			continue;
//		dbg(" x2 = %d y2 = %d dir = %d\n", x2, y2, dir[x2][y2]);
		if (dir[x2][y2] == i % 4)
		{
			if (!dfs(x2, y2, int(i >= 4)))
			{
//				dbg("ret false\n");
				return false;
			}
		}
	}
//	dbg("-----\n");
	return true;
}

int getDir(char c)
{
	int i = 0;
	while (i < 4 && ch[i] != c)
		++i;
	if (i == 4)
		throw 42;
	return i;
}

void brute(int x, int y)
{
zzz:
//	dbg("brute(%d %d)\n", x, y);
	if (x == n && y == 0)
	{
		++ans;
		return ;
	}

	int x1 = x;
	int y1 = y;
	++y1;
	if (y1 == m)
	{
		++x1;
		y1 = 0;
	}

	if (res[x][y] == -1)
	{
		int res2[N][N];
		memcpy(res2, res, sizeof(res));
		if (dfs(x, y, 0))
			brute(x1, y1);
		memcpy(res, res2, sizeof(res));
		if (dfs(x, y, 1))
			brute(x1, y1);
		memcpy(res, res2, sizeof(res));
	}
	else
	{
		x = x1;
		y = y1;
		goto zzz;
	}
}

int main()
{
#ifdef DBG1
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				dir[i][j] = getDir(s[i][j]);
			}
		fill(res, 0xFF);
		ans = 0;
		brute(0, 0);
		printf("Case #%d: %d\n", ii, int(ans % 1000003));
	}

	return 0;
}

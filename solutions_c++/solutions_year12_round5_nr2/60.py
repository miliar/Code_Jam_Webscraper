#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>
#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;
using namespace std;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
const int mx[] = { 1, 1, 0,-1,-1, 0};
const int my[] = { 0, 1, 1, 0,-1,-1};
const int maxn = 3000 + 10, maxm = 10000 + 100;
int f[maxn * 2][maxn * 2];
short g[maxn * 2][maxn * 2];
bool b[maxn * 2][maxn * 2];
//bool c[maxn * 2][maxn * 2];
int xb[maxm], yb[maxm];
int s, m;
int ffork,fbridge,fring;
const char *str[] = {"",
"bridge",
"fork",
"bridge-fork",
"ring",
"bridge-ring",
"fork-ring",
"bridge-fork-ring"};
inline int id(int x, int y)
{
	return (x << 12) | y;
}
inline int getx(int d)
{
	return d >> 12;
}
inline int gety(int d)
{
	return d & ((1 << 12) - 1);
}
short special(int x, int y)
{
	if (x == 1 && y == 1) return 1 << 0;
	if (x == s && y == 1) return 1 << 1;
	if (x == s * 2 - 1 && y == s) return 1 << 2;
	if (x == s * 2 - 1 && y == s * 2 - 1) return 1 << 3;
	if (x == s && y == s * 2 - 1) return 1 << 4;
	if (x == 1 && y == s) return 1 << 5;
	if (y == 1) return 1 << 6;
	if (x - y == s - 1) return 1 << 7;
	if (x == s * 2 - 1) return 1 << 8;
	if (y == s * 2 - 1) return 1 << 9;
	if (y - x == s - 1) return 1 << 10;
	if (x == 1) return 1 << 11;
	return 0;
}
bool valid(int x,int y)
{
	if (x <= 0 || y <= 0 || x>= s * 2 || y >= s * 2) return false;
	if (x - y >= s || y - x >= s) return false;
	return true;
}
int bits(int x)
{
	int r = 0;
	while(x)
	{
		if (x & 1) ++r;
		x >>= 1;
	}
	return r;
}
int find(int x, int y)
{
	int d = id(x, y);
	if (f[x][y] == d) return d;
	return f[x][y] = find(getx(f[x][y]), gety(f[x][y]));
}
void combine(int x1, int y1, int x2, int y2)
{
	int p = find(x1, y1);
	int q = find(x2, y2);
	if (p == q) return;
	f[getx(p)][gety(p)] = q;
	g[getx(q)][gety(q)] |= g[getx(p)][gety(p)];
}
void solve()
{
	scanf("%d%d", &s, &m);
	//memset(g, 0, sizeof(g));
	memset(b, 0, sizeof(b));
	//memset(c, 0, sizeof(c));
	ffork = fbridge = fring = m + 1;
	rep(i, s * 2) rep(j, s * 2)
	{
		if (!valid(i, j)) continue;
		f[i][j] = id(i, j);
		g[i][j] = special(i, j);
		//printf("%d,%d %d\n",i,j,g[i][j]);
	}

	rep(i, m)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		xb[i] = x;
		yb[i] = y;
		b[x][y] = true;
		rep(k, 6)
		{
			int tx = x + mx[k], ty = y + my[k];
			if (!valid(tx, ty)) continue;
			if (!b[tx][ty]) continue;
			combine(x, y, tx, ty);
		}
		int p = find(x, y);
		int q = g[getx(p)][gety(p)];
		//printf("%d,%d %d\n",x,y,q);
		if (bits(q & 63) >= 2 && fbridge > m) fbridge = i + 1;
		if (bits(q >> 6) >= 3 && ffork > m) ffork = i + 1;
	}
	VI bd;
	rep(i, s * 2) rep(j, s * 2)
	{
		if (!valid(i, j)) continue;
		f[i][j] = id(i, j);
		g[i][j] = special(i, j);
	}
	for (int x = 1; x < s * 2; ++x)
		for (int y = 1; y < s * 2; ++y)
		{
			if (b[x][y]) continue;
			rep(k, 6)
			{
				int tx = x + mx[k], ty = y + my[k];
				if (!valid(tx, ty)) continue;
				if (b[tx][ty]) continue;
				combine(x, y, tx, ty);
			}
		}
//	for (int x = 1; x < s * 2; ++x)
//		for (int y = 1; y < s * 2; ++y)
//		{
//			if (b[x][y]) continue;
//			int p = find(x, y);
//			if (!c[getx(p)][gety(p)]) fring = m;
//		}
	for (int i = m - 1; i >= 0; --i)
	{
		int x = xb[i], y =yb[i];
		//printf("%d:%d,%d\n",i,x,y);
		rep(j, 6)
		{
			int xt = x + mx[j], yt = y + my[j];
			if (!valid(xt, yt)) continue;
			if (b[xt][yt]) continue;
			int p = find(xt, yt);
			//printf("  %d,%d %d\n", xt,yt,g[getx(p)][gety(p)]);
			if (g[getx(p)][gety(p)] == 0) fring = i + 1;
		}
		rep(j, 6)
		{
			int xt = x + mx[j], yt = y + my[j];
			if (!valid(xt, yt)) continue;
			if (b[xt][yt]) continue;
			combine(x, y, xt, yt);
		}
		b[x][y] = false;
	}
	int z = min(ffork, min(fbridge, fring));
	if (z > m)
	{
		puts("none");
		return;
	}
	//printf("bridge=%d fork=%d ring=%d\n",fbridge,ffork,fring);
	int ans = 0;
	if (z == fbridge) ans |= 1;
	if (z == ffork) ans |= 2;
	if (z == fring) ans |= 4;
	printf("%s in move %d\n", str[ans], z);
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		printf("Case #%d: ", cs);
		solve();
	}
	return 0;
}

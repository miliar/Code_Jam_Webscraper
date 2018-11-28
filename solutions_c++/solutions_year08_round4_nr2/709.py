#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

struct dot
{
	int x, y;
	dot(int xx = 0, int yy = 0) : x(xx), y(yy) {}
};

inline int xmult(const dot& a, const dot& b)
{
	return a.x * b.y - a.y * b.x;
}

inline int abs(int x) {if (x > 0) return x; else return -x;}
inline int max(int a, int b) {if (a > b) return a; else return b;}

inline int calcArea(const dot& b, const dot& c)
{
	return abs(xmult(b, c));
}

bool Solve(dot& a, dot& b, dot& c, int m, int n, int area)
{
	a = dot(0, 0);
	for (b.x=0;b.x<=n;b.x++)
		for (b.y=0;b.y<=m;b.y++)
			for (c.x=0;c.x<=n;c.x++)
				for (c.y=0;c.y<=m;c.y++)
					if (calcArea(b, c) == area)
						return true;
	return false;
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for (int i=0;i<tt;i++)
	{
		printf("Case #%d: ", i + 1);
		int n, m, area;
		scanf("%d%d%d", &n, &m, &area);
		dot a, b, c;
		bool flag = Solve(a, b, c, m, n, area);
		if (flag)
		{
			printf("%d %d %d %d %d %d\n", a.x, a.y, b.x, b.y, c.x, c.y);
		} else printf("IMPOSSIBLE\n");
	}
	return 0;
}
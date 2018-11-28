#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int xmax, ymax;
int area;

struct SPoint
{
	int x, y;
};

int cross(int x1, int y1, int x2, int y2)
{
	return x1*y2 - x2*y1;
}

int cals(SPoint &a, SPoint &b1, SPoint &b2)
{
	return cross(b1.x-a.x, b1.y-a.y, b2.x-a.x, b2.y-a.y);
}

SPoint a, b, c;

bool solve()
{
	int i, j, k;

	if (xmax*ymax < area) return false;

	for (a.x = 0; a.x <= xmax; a.x ++) {
	for (b.x = 0; b.x <= xmax; b.x ++) {
	for (c.x = 0; c.x <= xmax; c.x ++) {
	for (a.y = 0; a.y <= ymax; a.y ++) {
	for (b.y = 0; b.y <= ymax; b.y ++) {
	for (c.y = 0; c.y <= ymax; c.y ++) {
		if (abs(cals(a, b, c)) == area) {
			return true;
		}
	}
	}
	}
	}
	}
	}

	return false;
}

int main()
{
	int i, j, k;
	int t;
	int nowt;
	int temp;

	freopen("B-small-attempt0.in.txt", "r", stdin);
	freopen("B-small-attempt0.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;

		scanf("%d%d%d", &xmax, &ymax, &area);

		if (solve())
			printf("Case #%d: %d %d %d %d %d %d\n", nowt, a.x, a.y, b.x, b.y, c.x, c.y);
		else
			printf("Case #%d: IMPOSSIBLE\n", nowt);
	}

	return 0;
}

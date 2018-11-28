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
#define vvi vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define eq(p, q) (fabs(p - q) < 1e-8)

struct point
{
	double x, y;
};

point t1[3];
point t2[3];

double scalar(point o, point a, point b)
{
	return (a.x - o.x) * (b.x - o.x) + (a.y - o.y) * (b.y - o.y);
}

point center(point a, point b)
{
	point p;
	p.x = (a.x + b.x) / 2;
	p.y = (a.y + b.y) / 2;
	return p;
}



int check()
{
	if (!eq(atan2(t1[1].y - t1[0].y, t1[1].x - t1[0].x) - atan2(t1[2].y - t1[0].y, t1[2].x - t1[0].x), 
		atan2(t2[1].y - t2[0].y, t2[1].x - t2[0].x) - atan2(t2[2].y - t2[0].y, t2[2].x - t1[0].x)))
		return 0;
	if (!eq(dist(t1[0], t1[1]) / dist(t1[0], t1[2]), dist(t2[0], t2[1]) / dist(t2[0], t2[2])))
		return 0;
	if (!eq(dist(t1[0], t1[1]) / dist(t1[1], t1[2]), dist(t2[0], t2[1]) / dist(t2[1], t2[2])))
		return 0;
	return 1;
}

void solve()
{
	/*if (!check())
	{
		swap(t1[0], t1[1]);
		if (!check())
		{
			swap(t1[1], t1[2]);
			if (!check())
			{
				swap(t1[0], t1[1]);
				if (!check())
				{
					swap(t1[1], t1[2]);
					if (!check())
						swap(t1[0], t1[1]);
				}
			}
		}
	}*/

	double ar = atan2(t2[1].y - t2[0].y, t2[1].x - t2[0].x) - atan2(t1[1].y - t1[0].y, t1[1].x - t1[0].x);
	double xt = t2[0].x - t1[0].x;
	double yt = t2[0].y - t1[0].y;
	double dt = dist(t1[0], t2[0]);
	double at = atan2(t2[0].y - t1[0].y, t2[0].x - t1[0].x);
	double sc = dist(t2[0], t2[1]) / dist(t1[0], t1[1]);

	for (int i = 0; i < 10000000; i++)
	{
		double angle = atan2(t1[1].y - t1[0].y, t1[1].x - t1[0].x);
		double di = dist(t1[0], t1[1]);
		point p, q;
		p.x = t1[0].x + dt * cos(at);
		p.y = t1[0].y + dt * sin(at);
		angle += ar;
		di *= sc;
		dt *= sc;
		at += ar;
		q.x = p.x + di * cos(angle);
		q.y = p.y + di * sin(angle);
		t1[0] = p;
		t1[1] = q;
	}
	printf("%lf %lf", t1[0].x, t1[0].y);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%lf%lf%lf%lf%lf%lf", &t1[0].x, &t1[0].y, &t1[1].x, &t1[1].y, &t1[2].x, &t1[2].y);
		scanf("%lf%lf%lf%lf%lf%lf", &t2[0].x, &t2[0].y, &t2[1].x, &t2[1].y, &t2[2].x, &t2[2].y);
		printf("Case #%d: ", testCount + 1);
		solve();
		printf("\n");
	}
	return 0;
}
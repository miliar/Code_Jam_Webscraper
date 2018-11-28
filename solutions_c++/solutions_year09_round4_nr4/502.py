#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Point
{
	double x,y;
	Point(){}
	Point(double x,double y):x(x),y(y){}
} pts[3];
bool operator==(const Point &a, const Point &b){return a.x==b.x&&a.y==b.y;}
Point operator -(const Point &p,const Point &q){return Point(p.x-q.x,p.y-q.y);}
double r[3];

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

double calc(int i, int j)
{
	return dist(pts[i].x, pts[i].y, pts[j].x, pts[j].y) + r[i] + r[j];
}

int main()
{
	int T, N;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		double res = 0.0;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%lf %lf %lf", &pts[i].x, &pts[i].y, &r[i]);
			if (r[i] > res) res = r[i];
		}
		if (N <= 2)
			printf("Case #%d: %.6f\n", t_case, res);
		else
		{
			double t = 1e300;
			double a = max(calc(0, 1), r[2]), b = max(calc(0, 2), r[1]), c = max(calc(1, 2), r[0]);
			if (a < t) t = a;
			if (b < t) t = b;
			if (c < t) t = c;
			printf("Case #%d: %.6f\n", t_case, t / 2);
		}
	}
	return 0;
}

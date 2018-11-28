#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int t;
int n;

struct point{
	double x, y, r;
};

point b[3];

inline double dist(double x1, double y1, double x2, double y2)
{
	return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

int main()
{
	scanf("%d", &t);
	REP(tt, t)
	{
		scanf("%d", &n);
		if (n == 1)
		{
			double x, y, r;
			scanf("%lf%lf%lf", &x, &y, &r);
			printf("Case #%d: %.6lf\n", tt + 1, r);
		}
		else if (n == 2)
		{
			double x, y, r;
			scanf("%lf%lf%lf", &x, &y, &r);
			double mx = r;
			scanf("%lf%lf%lf", &x, &y, &r);
			mx = max(mx, r);
			printf("Case #%d: %.6lf\n", tt + 1, mx);
		}
		else
		{
			double x1,y1,r1,x2,y2,r2,x3,y3,r3;
			scanf("%lf%lf%lf%lf%lf%lf%lf%lf%lf",&x1,&y1,&r1,&x2,&y2,&r2,&x3,&y3,&r3);
			double rt = min(max(dist(x1,y1,x2,y2)+r1+r2,r3),min(max(dist(x1,y1,x3,y3)+r1+r3,r2), max(dist(x2,y2,x3,y3)+r2+r3,r1)));
			printf("Case #%d: %.6lf\n", tt + 1, rt / 2.0);
		}
	}
}

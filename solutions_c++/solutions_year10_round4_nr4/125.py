#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

int max(int a, int b)
{
	if(a > b)
		return a;
	return b;
}

int min(int a, int b)
{
	if(a < b)
		return a;
	return b;
}

typedef struct{
	double x, y;
}Point;

int maze[105][105];
int temp[105][105];

double dist(Point a, Point b)
{
	return(sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)));
}

int main()
{
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);

	//freopen("D-large.in", "rt", stdin);
	//freopen("D-large.out", "wt", stdout);

	int inp, kase, i, j, k;
	int n, m;
	Point c1, c2, p;
	double r1, r2, d;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &m);
		scanf("%lf %lf", &c1.x, &c1.y);
		scanf("%lf %lf", &c2.x, &c2.y);

		printf("Case #%d:", kase);
		for(i = 0; i < m; i++)
		{
			scanf("%lf %lf", &p.x, &p.y);
			r1 = dist(c1, p);
			r2 = dist(c2, p);

			d = dist(c1, c2);
			if(r1 + r2 <= d)
			{
				printf(" 0.0");
				continue;
			}
			double angc2 = 2 * acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d));
			double angc1 = 2 * acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d));

			double area = 0.5 * angc2 * r2 * r2 - 0.5 * r2 * r2 * sin(angc2);
			area += (0.5 * angc1 * r1 * r1 - 0.5 * r1 * r1 * sin(angc1));
			printf(" %.8lf", area);
		}
		printf("\n");
		
		
	}
	
	return 0;

}

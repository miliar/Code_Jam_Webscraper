#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

struct node
{
	double x, y, r;
};

int n;
node data[100];
double result;

double dis(node &n1, node &n2)
{
	double re;
	
	re = (n1.r + n2.r + sqrt((n1.x - n2.x) * (n1.x - n2.x) + (n1.y - n2.y) * (n1.y - n2.y))) / 2.0;
	return re;
}

int main()
{
	int tcase, tno, i, j;
	
	scanf("%d", &tcase);
	for (tno = 1; tno <= tcase; tno++)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%lf%lf%lf", &data[i].x, &data[i].y, &data[i].r);
		if (n != 3)
		{
			result = 0;
			for (i = 0; i < n; i++)
				result = max(result, data[i].r);
		}
		else
		{
		result = MAXINT;
		result = min(result, max(data[0].r, dis(data[1], data[2])));
		result = min(result, max(data[1].r, dis(data[0], data[2])));
		result = min(result, max(data[2].r, dis(data[1], data[0])));
		}
		printf("Case #%d: %lf\n", tno, result);
	}
	
	return 0;
}

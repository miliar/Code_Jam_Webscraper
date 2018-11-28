#include <iostream>
#include <string>
#include <map>
#include <cassert>
#include <math.h>
#include <algorithm>
using namespace std;

int t, test;
double l, p, c;
int ans;

void init()
{
	scanf("%lf%lf%lf", &l, &p, &c);
}

void process()
{
	ans = 0;
	while (p / l > c)
	{
		double r = floor(sqrt(p * l));
		double tmp;
		if (abs((r + 1)*(r + 1) - p * l) < abs(r * r - p * l))
			tmp = r + 1;
		else
			tmp = r;
		if (tmp / l < p / tmp)
			l = tmp;
		else
			p = tmp;
		ans++;
	}
}

void print()
{
	printf ( "Case #%d: %d\n", test + 1, ans);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	for (test = 0; test < t; test++)
	{
		init();
		process();
		print();
	}
	return 0;
}
// d.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int t,n;

struct Point
{
	double x;
	double y;
	double r;
};
vector<Point> vec;

double dis(Point a, Point b)
{
	double res =  sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2)) + a.r + b.r;
	return res / 2.0;
}

int main()
{

	freopen("D-small-attempt2.in", "r",stdin);
	freopen("D-small-attempt2.out","w",stdout);

	cin >> t;
	for (int caseId = 1; caseId <= t; caseId++)
	{
		cin >> n;
		vec.clear();
		for (int i = 0; i < n; i++)
		{
			double x, y, r;
			cin >> x >> y >> r;
			Point p;
			p.x = x;
			p.y = y;
			p.r = r;
			vec.push_back(p);
		}

		double rr = 10000.0;
		if (n == 1)
		{
			rr = vec[0].r;
		}
		else if (n == 2)
		{
			rr = max(vec[0].r, vec[1].r);
		}
		else if (n == 3)
		{
			double dis01 = dis(vec[0],vec[1]);
			double dis02 = dis(vec[0],vec[2]);
			double dis12 = dis(vec[1],vec[2]);

			rr = min(rr, max(dis01, vec[2].r));
			rr = min(rr, max(dis02, vec[1].r));
			rr = min(rr, max(dis12, vec[0].r));
		}
		
		printf("Case #%d: %.6f\n", caseId, rr);

	}
	return 0;
}


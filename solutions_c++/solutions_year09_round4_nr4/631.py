#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

struct Point
{
	double x,y,r;
	Point()
	{}
	Point(double x1, double y1)
	{
		x = x1;
		y = y1;
	}
};

double Dist(Point a, Point b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

int n,t;
int main()
{
	freopen("test2.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;
	for (int k = 1; k <=t; k ++)
	{
		cin >> n;
		vector <Point> arr;
		arr.resize(n);
		double l = 0;
		double r = 1e5;	
		for (int i = 0 ;i < n;i ++)
		{
			cin >> arr[i].x >> arr[i].y >> arr[i].r;
			l = max(l,arr[i].r);
		}
		if (n == 1)
		{
			printf("Case #%d: %.6lf\n", k, arr[0].r);
			continue;
		}
		if (n == 2)
		{
			printf("Case #%d: %.6lf\n", k, max(arr[0].r,arr[1].r));
			continue;
		}
		if (n == 3)
		{
			double ans = 1e9;
			ans = min(ans, max(arr[0].r,  Dist(arr[1],arr[2])+arr[1].r+arr[2].r) /2);
			ans = min(ans, max(arr[1].r,  Dist(arr[0],arr[2])+arr[0].r+arr[2].r)/2);
			ans = min(ans, max(arr[2].r,  Dist(arr[1],arr[0])+arr[1].r+arr[0].r)/2);
			printf("Case #%d: %.6lf\n", k, ans);
		}


	}


	return 0;
}

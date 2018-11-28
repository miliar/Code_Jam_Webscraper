// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <cmath>
using namespace std;

const int N = 50;

class Plant
{
public:
	double x, y;
	double r;
};
Plant plant[N];

double distance(int i, int j)
{
	double tmp;
	double x1, y1, y2, x2;
	x1 = plant[i].x;
	x2 = plant[j].x;

	y1 = plant[i].y;
	y2 = plant[j].y;

	tmp = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

	return tmp;
}
double compute(int i, int j, int k)
{
	double tmp = 100000000;

	double x1, y1, y2, x2;
	x1 = plant[i].x;
	x2 = plant[j].x;

	y1 = plant[i].y;
	y2 = plant[j].y;

	tmp = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) + plant[i].r + plant[j].r;

	return (tmp > plant[k].r ? tmp: plant[k].r) / 2;
}
void solve()
{
	static int cas = 1;
	int n;
	cin>>n;

	for(int i = 0;i<n;i++)
	{
		cin >> plant[i].x >> plant[i].y >> plant[i].r;
	}

	if(n == 1)
	{
		printf("Case #%d: %.6lf\n", cas ++ , plant[0].r);
		return ;
	}

	if(n == 2)
	{
		double r1, r2;
		r1 = plant[0].r;
		r2 = plant[1].r;

		printf("Case #%d: %.6lf\n", cas ++ , r1 > r2 ? r1 : r2);
		return ;
	}
	double ans = 100000000;

	ans = ans < compute(0, 1, 2) ? ans : compute(0, 1, 2);
	ans = ans < compute(0, 2, 1) ? ans : compute(0, 2, 1);
	ans = ans < compute(1, 2, 0) ? ans : compute(1, 2, 0);

	//cout << ans << endl;
	printf("Case #%d: %.6lf\n", cas ++ , ans);
}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	int t;
	cin>>t;

	for(int i = 0;i<t;i++)
	{
		solve();
	}

	return 0;
}


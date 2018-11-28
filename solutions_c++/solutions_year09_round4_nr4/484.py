#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>

using namespace std;


double x[10],y[10],r[10];
int N;

double dist(double x1,double y1,double x2,double y2)

{
	return sqrt((x1-x2)*(x1-x2) + (y1-y2) * (y1-y2));
}
int main()
{
	int C;

	cin >> C ;
	for (int cc = 1; cc <= C ;cc ++)
	{
		cin >> N;
		for (int i = 0;i<N;i++) cin >> x[i] >> y [i] >> r[i];

		double ans = 0;
	if (N == 1) ans = r[0];
	else if (N ==2 ) ans = max(r[0],r[1]);
	else
	{
		ans = 1e100;
		double m;
		m = max(dist(x[0],y[0],x[1],y[1]) + r[0]+r[1], r[2]*2); if (m < ans) ans = m;
		m = max(dist(x[2],y[2],x[1],y[1]) + r[2]+r[1], r[1]*2); if (m < ans) ans = m;
		m = max(dist(x[0],y[0],x[2],y[2]) + r[0]+r[2], r[0]*2); if (m < ans) ans = m;
		ans /= 2;
	}

		printf("Case #%d: %.6f\n", cc, ans);
	}
	return 0;
}
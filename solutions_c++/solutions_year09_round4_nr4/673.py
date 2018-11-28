#include <iostream>
#include <math.h>
using namespace std;

struct Plant 
{
	double x, y, r;
};

int N;
Plant plants[40];

double dist(Plant p1, Plant p2)
{
	return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

double cover2(Plant p1, Plant p2)
{
	double d = dist(p1, p2);
	if (d+p1.r<=p2.r) return p2.r;
	if (d+p2.r<=p1.r) return p1.r;
	return (d+p1.r+p2.r)/2;
}

double getac()
{
	if (N==1) return plants[0].r;
	else if (N==2) return max(plants[0].r, plants[1].r);
	else if (N==3)
	{
		double ret = max(cover2(plants[0], plants[1]), plants[2].r);
		double t = max(cover2(plants[0], plants[2]), plants[1].r);
		if (ret > t) ret = t;
		t = max(cover2(plants[1], plants[2]), plants[0].r);
		if (ret > t) ret = t;
		return ret;
	}
	else
		return 0;
}

int main()
{

	int T;
	scanf("%d", &T);
	for (int tt = 0; tt < T; tt++)
	{
		scanf("%d", &N);
		for (int i =0 ; i < N; i++)
		{
			scanf("%lf%lf%lf", &plants[i].x, &plants[i].y, &plants[i].r);
		}
		printf("Case #%d: %.6lf\n", tt+1, getac());
	}
	return 0;
}
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>

using namespace std;

double xc, yc, zc;
double x, y, z;

const double eps = 1e-12;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		xc = yc = zc = 0;
		x=y=z=0;
		int n;
		scanf("%d",&n);
		for(int i=0; i<n; ++i)
		{
			double t1, t2, t3, t4, t5, t6;
			scanf("%lf%lf%lf%lf%lf%lf", &t1,&t2,&t3,&t4,&t5,&t6);
			x+=t1;
			y+=t2;
			z+=t3;
			xc+=t4;
			yc+=t5;
			zc+=t6;
		}
		x/=n;y/=n;z/=n;
		xc/=n;yc/=n;zc/=n;

		double t;

		if(abs(xc*xc + yc*yc + zc*zc) < eps)
			t = 0;
		else
			t = -1* (xc*x + yc*y+zc*z) / (xc*xc + yc*yc + zc*zc);
		
		if(t < 0)
			t = 0;
		
		double d = sqrt((xc*t+x)*(xc*t+x) + (yc*t+y)*(yc*t+y) + (zc*t+z)*(zc*t+z));

		printf("Case #%d: %lf %lf\n", c, d, t);
	}

	return 0;
}

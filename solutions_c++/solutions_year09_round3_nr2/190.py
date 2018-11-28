// qa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "memory.h"
#include "cmath"
using namespace std;

int main()
{
	freopen("e:\\B-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int zz,n;
	int i,j;

	scanf("%d",&zz);

	for (int ttz = 1; ttz <= zz; ttz++)
	{		
		double x = 0,y = 0,z = 0;
		double vx = 0,vy = 0,vz = 0;
		double tx,ty,tz,tvx,tvy,tvz;
		double t,d;
		double a,b,c;

		scanf("%d",&n);

		for (i = 0; i < n; i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf",&tx,&ty,&tz,&tvx,&tvy,&tvz);
			x += tx,y += ty, z += tz;
			vx += tvx,vy += tvy,vz += tvz;
		}

		a = vx * vx + vy * vy + vz * vz;
		b = 2 * vx * x + 2 * vy * y + 2 * vz * z;
		t = a == 0.0 ? 0 : -b / (2 * a);
		t += 0.0;
		if (t < 0) t = 0;
		a = (x + vx * t);
		b = (y + vy * t);
		c = (z + vz * t);
		//printf("%lf %lf %lf\n",a,b,c);
		d = a * a + b * b + c * c;
		d = sqrt(d) / (double)n;
		printf("Case #%d: %.7lf %.7lf\n",ttz,d,t);
	}

	return 0;
}
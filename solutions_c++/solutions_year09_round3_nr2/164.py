#include<stdio.h>
#include<map>
#include<cmath>

using namespace std;


double x[500],y[500],z[500],vx[500],vy[500],vz[500];

int main(void)
{
	freopen("E:\\B-small.in","r",stdin);
	freopen("E:\\B-small.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tcase;
	for(tcase = 1 ; tcase <= t; tcase ++)
	{
		int n;
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf%lf%lf%lf",x+i,y+i,z+i,vx+i,vy+i,vz+i);
		double mx=0,my=0,mz=0,mvx=0,mvy=0,mvz=0;
		for(i=0;i<n;i++)
		{
			mx += x[i];
			my += y[i];
			mz += z[i];
			mvx += vx[i];
			mvy += vy[i];
			mvz += vz[i];
		}
		mx /=n;
		my/= n;
		mz /= n;
		mvx /= n;
		mvy /= n;
		mvz /= n;
		double tmin,dmin;
		if(mvx == 0 && mvy == 0 && mvz == 0)
		{
			tmin = 0;
		}
		else
		{
			double tt = -(mvx*mx+mvy*my+mvz*mz)/(mvx*mvx+mvy*mvy+mvz*mvz);
			if(tt < 0)
				tmin = 0;
			else
				tmin = tt;
		}
		dmin = sqrt((mx+mvx*tmin)*(mx+mvx*tmin)+(my+mvy*tmin)*(my+mvy*tmin)+(mz+mvz*tmin)*(mz+mvz*tmin));
		printf("Case #%d: %lf %lf\n",tcase,dmin,tmin);
	}
	return 0;
}
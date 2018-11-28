#include<iostream>
#include<cmath>
#define err 1e-6
using namespace std;
struct pt
{
	int x,y,z;
};
typedef struct pt pt;
struct com
{
	long double x,y,z;
};
typedef struct com com;
int main()
{
	int i,j,k,q,t,n;
	pt p,v;
	com comp,comv;
	long double dmin,tmin;
	scanf("%d",&t);
	for(q=1;q<=t;q++)
	{
		scanf("%d",&n);
		comp.x=comp.y=comp.z=comv.x=comv.y=comv.z=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d%d%d",&p.x,&p.y,&p.z,&v.x,&v.y,&v.z);
			comp.x+=p.x;
			comp.y+=p.y;
			comp.z+=p.z;
			comv.x+=v.x;
			comv.y+=v.y;
			comv.z+=v.z;
		}
		comp.x/=n;
		comp.y/=n;
		comp.z/=n;
		comv.x/=n;
		comv.y/=n;
		comv.z/=n;
		if((comv.x<err&&comv.x>-err)&&(comv.y<err&&comv.y>-err)&&(comv.z<err&&comv.z>-err))
		{
			dmin=sqrt(comp.x*comp.x+comp.y*comp.y+comp.z*comp.z);
			tmin=0;
		}
		else
		{
			tmin=-(comp.x*comv.x+comp.y*comv.y+comp.z*comv.z);
			tmin/=(comv.x*comv.x+comv.y*comv.y+comv.z*comv.z);
			if(tmin<err)
			{
				tmin=0;
			}
			comp.x+=(comv.x*tmin);
			comp.y+=(comv.y*tmin);
			comp.z+=(comv.z*tmin);
			dmin=sqrt(comp.x*comp.x+comp.y*comp.y+comp.z*comp.z);
		}
		printf("Case #%d: %.8Lf %.8Lf\n",q,dmin,tmin);
	}
}
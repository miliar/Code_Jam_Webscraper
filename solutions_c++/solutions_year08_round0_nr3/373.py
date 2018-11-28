#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <cmath>
using namespace std;
double intf(double a , double b , double y , double r)
{
	double x;
	x = a;
	a = 1./2.*x*sqrt(r*r-x*x)+1./2.*r*r*atan(1./sqrt(r*r-x*x)*x)-y*x;
	x = b;
	b = 1./2.*x*sqrt(r*r-x*x)+1./2.*r*r*atan(1./sqrt(r*r-x*x)*x)-y*x;
	return b - a;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca;
	double f,R,t,r,g,pi =acos(0.)*2. , rr , x , y , ans , lim , k1 , k2;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		ans = 0.0;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		if (g<=f*2.)
		{
			printf("Case #%d: %.6lf\n",ca,1.);
			continue;
		}
		rr = R - t - f;
		for (x = r+f ; x < rr ; x += 2.*r+g)
		{
			lim = rr*rr-x*x;
			for (y = r+f ; y*y < lim ; y += 2.*r + g)
			{
				if ( (x+g-2.*f)*(x+g-2.*f)+(y+g-2.*f)*(y+g-2.*f)<=rr*rr)
				{
					ans += (g-2.*f)*(g-2.*f);
				}
				else
				{
					if ((y+g-2.*f)*(y+g-2.*f)<=lim)
					{
						k2 = sqrt(rr*rr-y*y);
						k1 = sqrt(rr*rr-(y+g-2.*f)*(y+g-2.*f));
						if (x+g-2.*f <= k2)
						{
							ans += (g-2.*f)*(k1-x) + intf(k1,x+g-2.*f,y,rr);
						}
						else
						{
							ans += (g-2.*f)*(k1-x) + intf(k1,k2,y,rr);
						}
					}
					else if ((x+g-2.*f)*(x+g-2.*f)<=rr*rr-y*y)
					{
						ans += intf(x,x+g-2.*f,y,rr);
					}
					else
					{
						ans += intf(x,sqrt(rr*rr-y*y),y,rr);
					}
				}
			}
		}
		printf("Case #%d: %.6lf\n",ca,1.-4.*ans/pi/R/R);
	}
	return 0;
}

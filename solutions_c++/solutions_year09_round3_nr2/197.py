#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

long double x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;

long double dist(long double t)
{
	return (x+vx*t)*(x+vx*t) + 
		   (y+vy*t)*(y+vy*t) +
		   (z+vz*t)*(z+vz*t);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++)
	{
		int n;
		cin>>n;
		x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;
		for(int i=0;i<n;i++)
		{
			long double xx, yy, zz, vxx, vyy, vzz;
			cin>>xx>>yy>>zz>>vxx>>vyy>>vzz;
			x += xx;
			y += yy;
			z += zz;
			vx += vxx;
			vy += vyy;
			vz += vzz;
		}
		x/=n;
		y/=n;
		z/=n;
		vx/=n;
		vy/=n;
		vz/=n;
		long double l = 0, h = 1e9, m1, m2;
		if(fabs(vx) < 1e-6 && fabs(vy) < 1e-6 && fabs(vz) < 1e-6)
		{
			h = 0;
		}
		else 
		{
			for(int i=0;i<100000;i++)
			{
				m1 = (2*l + h) / 3;
				m2 = (l + 2*h) / 3;
				if(dist(m1) < dist(m2))
				{
					h = m2;
				}
				else
				{
					l = m1;
				}
			}
		}
   	    cout << fixed;
		cout << setprecision (8)<< "Case #"<<t<<": "<<sqrt(dist((l+h)/2))<<" "<<(l+h)/2<<endl;
		//printf("Case #%d: %.8lf %.8lf\n", t, sqrt(dist((l+h)/2)), (l+h)/2);
	}
	return 0;
}
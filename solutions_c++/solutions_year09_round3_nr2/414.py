#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

double x,y,z,dx,dy,dz;
int a,b,c,va,vb,vc,t,n;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d", &t);
fr(q,t)
	{
	scanf("%d", &n);
	x = y = z = dx = dy = dz = 0;
	fr(i,n)
		{
		scanf("%d%d%d%d%d%d", &a, &b, &c, &va, &vb, &vc);
		x+=a;
		y+=b;
		z+=c;
		dx+=va;
		dy+=vb;
		dz+=vc;
		}
	x/=n;
	y/=n;
	z/=n;
	dx/=n;
	dy/=n;
	dz/=n;
//	cout<<"Data: "<<x<<" "<<y<<" "<<z<<" "<<dx<<" "<<dy<<" "<<dz<<endl;
	double a1,b1,c1;
	a1 = dx*dx+dy*dy+dz*dz;
	b1 = 2*(x*dx+y*dy+z*dz);
	c1 = x*x+y*y+z*z;
//	cout<<"Koeffs: "<<a1<<" "<<b1<<" "<<c1<<endl;
	double d,t_min;
	if(a1!=0)
		{
		t_min = (-b1)/(2*a1);
		if(t_min<=0) t_min = 0;
		d = a1*t_min*t_min+b1*t_min+c1;
		if(d<0) d = 0;
		d = sqrt(d);
		}
	else
		{
		t_min = 0;
		d = sqrt(c1);
		}
	printf("Case #%d: %.8f %.8f\n", (q+1), d,t_min);
	}
return 0;
}

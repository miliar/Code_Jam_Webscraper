
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
/////////////////////////POINT
struct point{
	ld x,y;
	bool real;
	point(ld x_ =0 ,ld y_ =0 )
	{
		x = x_;
		y = y_;
		real = true;
	}
	friend ostream& operator<<(ostream& out, const point& a);
	ld dist_to(const point& A)const 
	{
		return sqrt((x-A.x)*(x-A.x) + (y - A.y)*(y- A.y));
	}
	operator bool()
	{
		return real;
	}
};
ostream& operator<<(ostream& out, const point& a)
{
	out<<"("<<a.x<<","<<a.y<<")";
	return out;
}

////////////////////////////LINE
bool nula(ld x)
{
	return x>-epsylon && x < epsylon;
}
struct line{
	ld a,b,c;
	line(const point A,const point B)
	{
		if(nula(A.x - B.x))
		{
			a = 1.0;
			b = 0.0;
			c = -A.x;
		}
		else
		{
			b = 1.0;
			a = b*(B.y - A.y)/(A.x - B.x);
			c = -a*A.x - b*A.y;
		}
	}

};
int sign(ld x)
{
	if(x<-epsylon)
		return -1;
	if(x>epsylon)
		return 1;
	return 0;
}
line perpend(const line& a, const point& A)
{
	point B;
	B.x = A.x + a.a;
	B.y = A.y + a.b;
	return line(A,B);
}
point intersect(const line& A ,const line& B)
{
	ld tmp1 = A.b*B.a - A.a*B.b,tmp2=A.a*B.c - A.c*B.a;
	point tmp;
	if(nula(tmp1))
	{
		tmp.real = false;
		return tmp;
	}
	tmp.y = tmp2/tmp1;
	if(nula(A.a))
	{
		tmp.x = (-B.b*tmp.y - B.c)/B.a;
	}
	else
	{
		tmp.x = (-A.b*tmp.y - A.c)/A.a;
	}
	return tmp;
}
/////////////////////SEGMENT
struct segment
{
	point a,b;
	segment(const point& x, const point& y)
	{
		a = x;
		b = y;
	}
	ld length()const 
	{
		return a.dist_to(b);
	}
};
bool between(ld x,ld nachalo,ld krai)
{
	return x > nachalo - epsylon && x < krai + epsylon;
}
point intersect(const segment& a,const segment& b)
{
	line x(a.a,a.b);
	line y(b.a,b.b);
	point tmp = intersect(x,y);
	if(!between(tmp.x,a.a.x,a.b.x)&&!between(tmp.x,a.b.x,a.a.x))
		tmp.real = false;
	if(!between(tmp.y,a.a.y,a.b.y)&&!between(tmp.y,a.b.y,a.a.y))
		tmp.real = false;
	if(!between(tmp.x,b.a.x,b.b.x)&&!between(tmp.x,b.b.x,b.a.x))
		tmp.real = false;
	if(!between(tmp.y,b.a.y,b.b.y)&&!between(tmp.y,b.b.y,b.a.y))
		tmp.real = false;
	return tmp;
}
///////////////////////AREA
ld area(point a,point b,point c)
{
	return (a.x*b.y + a.y * c.x + b.x * c.y - a.y * b.x - a.x * c.y - b.y * c.x)*0.5;
}
///////////////////CIRCLES
struct circle
{
	point center;
	ld radius;
	circle()
	{
	}
	circle(const point& c,ld r)
	{
		center = c;
		radius = r;
	}
	bool contains(const point& a) const
	{
		return center.dist_to(a) <  radius + epsylon;
	}
};
vector<point> intersect(const line& a,const circle& c)
{
	line b = perpend(a,c.center);
	point A = intersect(a,b);
	vector<point> res;
	if(!A || (A.dist_to(c.center) - c.radius) > epsylon)
		return res;
	if(fabs(A.dist_to(c.center) - c.radius) < epsylon)
	{
		res.push_back(A);
		return res;
	}
	ld deg = c.radius*c.radius - A.dist_to(c.center)*A.dist_to(c.center);
	ld len = sqrt(deg);
	point AB = A,AC = A;
	ld val = (len) / sqrt(a.a*a.a + a.b*a.b);
	AB.x += -a.b*val;
	AB.y += a.a*val;
	AC.x += a.b*val;
	AC.y += -a.a*val;
	res.push_back(AB);
	res.push_back(AC);
	return res;
}
vector<point> intersect(const circle& b,const circle& a)
{
	ld d = b.center.dist_to(a.center);
	vector<point> res;
	if(d > b.radius + a.radius + epsylon)
		return res;
	else if(fabs(d - (b.radius + a.radius)) < epsylon)
	{
		point intersect;
		ld sum = b.radius + a.radius;
		intersect.x = (b.center.x * a.radius)/sum + (a.center.x * b.radius)/sum;
		intersect.y = (b.center.y * a.radius)/sum + (a.center.y * b.radius)/sum;
		res.push_back(intersect);
	}
	else
	{

		segment central(b.center,a.center);
		ld sa,sb,sc;
		sa = b.radius;
		sb = a.radius;
		sc = central.length();
		ld p = (sa + sb + sc)*0.5;
		ld S = (p-sa)*(p-sb)*(p-sc)*p;
		ld h = (4.0*S/(sc*sc));
		if(sa*sa + sc*sc - sb*sb < -epsylon)
		{
			ld o = sqrt(sa*sa -h);
			ld sum = sc + o;
			ld suma = sum + o;
			point d;
			d.x = (sum*b.center.x - o*a.center.x) /sc;
			d.y = (sum*b.center.y - o*a.center.y) /sc;
			line temp = perpend(line(central.a,central.b),d);
			return intersect(temp,a);
		}
		else if(sb*sb + sc*sc - sa*sa < -epsylon)
		{
			ld o = sqrt(sb*sb -h);
			ld sum = sc + o;
			ld suma = sum + o;
			point d;
			d.x = (-o*b.center.x + sum*a.center.x) /sc;
			d.y = (-o*b.center.y + sum*a.center.y) /sc;
			line temp = perpend(line(central.a,central.b),d);
			return intersect(temp,a);
		}
		else
		{
			ld o = sqrt(sa*sa - h);
			point d;
			ld left = sc - o;
			d.x = (b.center.x*left + a.center.x*o)/sc;
			d.y = (b.center.y*left + a.center.y*o)/sc;
			line temp = perpend(line(central.a,central.b),d);
			return intersect(temp,a);
		}
	}

}
int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D-small.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n;
		cin>>n;
		vector<circle> a(n);
		for(int i=0;i<n;i++)
		{
			cin>>a[i].center.x>>a[i].center.y>>a[i].radius;
		}
		if(n < 3)
		{
			ld mx = 0;
			for(int i=0;i<n;i++)
			mx = max(mx,a[i].radius);
			printf("Case #%d: %.8llf\n",it,mx);

			//cout<<"Case #"<<it<<": "<<0.0<<endl;
		}
		else
		{
			ld mx = 1e+9;
			mx = min(mx,(a[0].center.dist_to(a[1].center) + a[0].radius + a[1].radius)*0.5);
			mx = min(mx,(a[0].center.dist_to(a[2].center) + a[0].radius + a[2].radius)*0.5);
			mx = min(mx,(a[2].center.dist_to(a[1].center) + a[2].radius + a[1].radius)*0.5);
			mx = max(mx,a[0].radius);
			mx = max(mx,a[1].radius);
			mx = max(mx,a[2].radius);
			printf("Case #%d: %.8llf\n",it,mx);
		}

	}
	return 0;
}

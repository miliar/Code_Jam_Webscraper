#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <vector>
using namespace std;

#define	EPS	1e-10

const double pi = 2. * acos(0.);

bool inside(double radius, double x, double y)
{
	return (fabs(radius * radius - (x * x + y * y)) < EPS) || (radius * radius > (x * x + y * y));
}

int inside(double radius, double *x,double *y)
{
	int	i,c = 0;
	
	for(i = 0; i < 4; i++)
		if(inside(radius,x[i],y[i]))
			c++;		
			
	return c;
}

typedef pair<double,double>	POINT;
#define	X	first
#define	Y	second

double Distance(const POINT &p1,const POINT &p2)
{
	return sqrt((p1.X - p2.X) * (p1.X - p2.X) +
				(p1.Y - p2.Y) * (p1.Y - p2.Y)); 
}

double area(vector <POINT> vp)
{
	int	i,s = vp.size();
	double	a = 0;
	
	for(i = 0; i < s; i++)
		a += vp[i].X * vp[(i + 1) % s].Y - vp[(i+1)%s].X * vp[i].Y;
	
	return a / 2.0;
}

double chordArea(double radius, double chordLen)
{
	double	angle,ca,ct;
	
	angle = (2 * radius * radius - chordLen * chordLen) / (2 * radius * radius);
	angle = acos(angle);
	
	ca = (angle * radius * radius) / 2.0;
	ct = (radius * radius * sin(angle)) / 2.0;
	
	return ca - ct; 
}

double intersectX(double radius, double y)
{
	return sqrt(radius * radius - y * y);
}

double intersectY(double radius, double x)
{
	return sqrt(radius * radius - x * x);
}

POINT intersect(double radius, const POINT &p1,const POINT &p2)
{
	if(fabs(p1.X - p2.X) < EPS)
		return make_pair(p1.X, intersectY(radius, p1.X));
	else
		return make_pair(intersectX(radius, p1.Y), p1.Y);
}

double getArea(double radius, double l,double r,double t,double b)
{
	double	x[4],y[4];
	
	x[0] = l, y[0] = b;
	x[1] = r, y[1] = b;
	x[2] = r, y[2] = t;
	x[3] = l, y[3] = t;
	
	if((r - l) * (t - b) < EPS) return 0.0;
	
	int	in = inside(radius, x,y);
	if(in == 4) 
		return fabs(r - l) * fabs(t - b);
	else if(in == 0)
		return 0.0;
	else
	{
		vector <POINT>	vp;
		int	i,c = 0;
		POINT	cp[2];
		
		for(i = 0; i < 4; i++)
		{
			if(inside(radius,x[i],y[i])) vp.push_back(make_pair(x[i],y[i]));
			
			bool	p,q;
			
			p = inside(radius, x[i], y[i]) ? 1 : 0;
			q = inside(radius,x[(i+1)%4],y[(i+1)%4]) ? 1 : 0;
			
			if(p ^ q)
			{
				cp[c] = intersect(radius, make_pair(x[i],y[i]),make_pair(x[(i+1)%4],y[(i+1)%4]));
//				fprintf(stderr,"%lf %lf %d\n",cp[c].X,cp[c].Y ,c);
				if(c > 0)
				{
					if(Distance(cp[c - 1],cp[c]) > EPS)
					{
						c++;
						vp.push_back(cp[c - 1]);
					}
				}
				else
				{
					c++;
					vp.push_back(cp[c - 1]);
				}
			}
		}
		
		//fprintf(stderr,"size: %d, c = %d\n",vp.size(),c);

if(c == 1) return fabs(r - l) * fabs(t - b);
		
		assert(c == 2);
		
		return chordArea(radius, Distance(cp[0],cp[1])) + area(vp); 
	}
}

int main(int argc, char **argv) {
	double	f,R,t,r,g;
	double	x,y,s,a;
	int		T,cs;
	
	freopen("/home/sidky/Desktop/C-large.in","rt",stdin);
	freopen("/home/sidky/out.txt","wt",stdout);
	
	scanf("%d",&T);
	
	for(cs = 1; cs <= T; cs++)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		
//		fprintf(stderr, "-----\n");
		
		if(g < 2 * f || (R - t < f))
		{
			printf("Case #%d: %.6lf\n",cs,1.0);
			continue;
		}
		
		s = a = 0;
		
		for(x = 0.0; x < R; x += g + 2 * r)
		{
			for(y = 0.0; y < R; y += g + 2 * r)
			{
//				fprintf(stderr, "(%lf-%lf) x (%lf-%lf)\n",x + r + f,x + r + g - f,
//					y + r + f,y + r + g - f);
					
				s += getArea(R - t - f, 
						x + r + f, 
						x + r + g - f,
						y + r + g - f,
						y + r + f);
//				fprintf(stderr, "area: %lf\n",s);
					
			}
		}
		
		s *= 4;
		
		a = pi * R * R;
//		fprintf(stderr,"%lf %lf\n",s,a);
		
		printf("Case #%d: %.6lf\n",cs,1 - (s / a));
	}
	
	return 0;	
}

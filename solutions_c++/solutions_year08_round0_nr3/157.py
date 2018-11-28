#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

const double inf = 1e30;
const double eps = 1e-14;
const double PI = 3.1415926535897932;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

double f,R,t,r,g;

inline double arcvl(double x)
{
	return x>R ? inf : sqrt(R*R-x*x);
}

inline double archl(double y)
{
	return y>R ? inf : sqrt(R*R-y*y);
}

inline bool incircle(double x,double y)
{
	return x*x+y*y < R*R-eps;
}

inline bool cover(double c,double a,double b)
{
	return c>=a && c<=b;
}

double area(double x, double y)
{
	if (incircle(x+g,y+g)) return g*g;
	
	double y1 = arcvl(x);
	double y2 = arcvl(x+g);
	double x1 = archl(y);
	double x2 = archl(y+g);
	
	double theta,s1,s2,s3,s4,s5;
	if (cover(y1,y,y+g) && cover(x1,x,x+g))
	{
		theta = atan2(y1,x)-atan2(y,x1);
		s1 = 0.5*theta*R*R;
		s2 = 0.5*(y1-y)*x;
		s3 = 0.5*(x1-x)*y;
		return s1-s2-s3;
	}
	if (cover(x2,x,x+g) && cover(y2,y,y+g))
	{
		theta = atan2(y+g,x2)-atan2(y2,x+g);
		s1 = 0.5*theta*R*R;
		s2 = 0.5*(x2-x)*(y+g);
		s3 = 0.5*(y2-y)*(x+g);
		s4 = 0.5*x*g;
		s5 = 0.5*y*g;
		return s1+s2+s3-s4-s5;
	}
	if (cover(y1,y,y+g) && cover(y2,y,y+g))
	{
		theta = atan2(y1,x)-atan2(y2,x+g);
		s1 = 0.5*theta*R*R;
		s2 = 0.5*(y2-y)*(x+g);
		s3 = 0.5*(y1-y)*x;
		s4 = 0.5*g*y;
		return s1+s2-s3-s4;
	}
	if (cover(x2,x,x+g) && cover(x1,x,x+g))
	{
		theta = atan2(y+g,x2)-atan2(y,x1);
		s1 = 0.5*theta*R*R;
		s2 = 0.5*(x2-x)*(y+g);
		s3 = 0.5*x*g;
		s4 = 0.5*(x1-x)*y;
		return s1+s2-s3-s4;
	}
}

void solve()
{
	fout << fixed << setprecision(6);
	fin >> f >> R >> t >> r >> g;
	double A = PI*R*R;
	if (f*2 >= g)
	{
		fout << 1.0 << endl;
		return;
	}
	R -= (t+f);
	g -= 2*f;
	r += f;
	
	double B = 0;
	for (double x = r; x <= R; x += g+r+r)
	    for (double y = r; incircle(x,y); y += g+r+r)
	        B += area(x,y);
	B *= 4;
	fout << 1-B/A << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i=1; i<=tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}

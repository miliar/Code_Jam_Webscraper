#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

const double pi = acos(0.0) * 2.0;

inline double sqr(double x) { return x * x; }


double get_area(double pos, double r, double R, double c)
{
	double ret = 0.0;
	if (pos >= R)
		return 0.0;
	
	r = min(r, R - pos);

	double theta = asin(pos / R);
	double temp = theta * R * R * 0.5 + 
		(R * pos * cos(theta) * 0.5);
	pos += r;
	
	double theta2 = asin(pos / R);
	double temp2 = theta2 * R * R * 0.5 + 
		(R * pos * cos(theta2) * 0.5);

	return temp2 - temp;
}

double get_area3(double pos, double pos2, double r, double R, double g, double c)
{
	double t1 = acos(pos / R);
	double t2 = acos((pos + g) / R);
	double a1 = R * sin(t1);
	double a2 = R * sin(t2);
	
	if (a1 < pos2) return 0.0;

	if (a2 >= pos2 + r)
		return g * r;
	double t3 = asin(pos2 / R);
	
	if (pos + g > R * cos(t3))
		g = R * cos(t3) - pos;

	if (pos2 + r > a1)
		r = a1 - pos2;
		
	double theta = asin(pos / R);
	double temp = theta * R * R * 0.5 + 
		(R * pos * cos(theta) * 0.5);

	double pp = pos + g;
	double theta2 = asin(pp / R);
	double temp2 = theta2 * R * R * 0.5 + 
		(R * pp * cos(theta2) * 0.5);
	
	double t4 = asin((pos2 + r) / R);
	
	double g2 = g;
	if (pos + g2 > R * cos(t4))
		g2 = R * cos(t4) - pos;

	double pp2 = pos + g2;
	double theta3 = asin(pp2 / R);
	double temp3 = theta3 * R * R * 0.5 + 
		(R * pp2 * cos(theta3) * 0.5);

	double temp4 = temp3 - temp - (pos2 + r) * g2;
		

	double ret = temp2 - temp - pos2 * g - temp4;
	return ret;
}

double get_area2(double pos, double r, double R, double g, double c)
{
	double pos2 = 0;
	double ret = 0.0;
	
	ret = get_area3(pos, pos2, r, R, g, c);
	pos2 = r + g;
	while(pos2 < R) {
		ret += get_area3(pos, pos2, r*2, R, g, c);
		pos2 += r*2 + g;
	}

	return ret;
}

double solve()
{
	double f, R, t, r, g;
	scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);

	r += f;
	t += f;
	g -= f * 2.0;
	double quarter_circle = pi * sqr(R) / 4.0;

	if (g <= 0) 
		return 1.0;
	
	double area;

	R -= t;
	double q_circle2 = pi * sqr(R) / 4.0;
	area = quarter_circle - q_circle2;

	double pos = 0;
	while(pos < R) {
		area += get_area(pos, r, R, q_circle2);
		pos += r;
		area += get_area2(pos, r, R, g, q_circle2);
		pos += g;
		area += get_area(pos, r, R, q_circle2);
		pos += r;
	}

	return area / quarter_circle;
}


int main(void)
{
	int test;
	int cnt = 0;
 	scanf("%d", &test);

	REP(i, test) {
		printf("Case #%d: %.6lf\n", ++cnt, solve());
	}

	return 0;
}


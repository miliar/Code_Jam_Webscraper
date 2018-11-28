#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long

//#define pi 3.141592654
using namespace std;
typedef vector<int> VI;
typedef vector<string>VS;

double PI = 3.141592654;
int T;


void init()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	RE("%d",&T);
}

double len(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

double f(double x, double a)
{
	return x*0.5*sqrt(a*a-x*x) + a*a*0.5*asin(x/a);
}
double get_s(double R, double r, double g)
{
	//WR("***********************************\n");
	if (g<0) return 0;
	if (R<0) return 0;
	
	double x = r, y = r;
	double ans = 0.;
	while(x < R+5)
	{
		y = r;
		while (1)
		{
			double x1 = x, y1 = y, x2 = x1, y2 = y1 + g, x3 = x1 + g, y3 = y1 + g, x4 = x1 + g, y4 = y1;
			
			y+=g+r+r;
			double x5, y5, x6, y6;
			if (x1*x1 + y1*y1 >= R*R) break;
			if (x3*x3 + y3*y3 < R*R) {ans+=g*g;continue;}
			
			if (x2*x2 + y2*y2 > R*R) //1, 2
			{
				//x5 = x1, y5 = sqrt(R*R - x1*x1);
				if (x4*x4 + y4*y4 > R*R)//2
				{
					//WR("2\n");
					y6 = y1, x6 = sqrt(R*R - y6*y6);
					double h  =  f(x6,R) - f(x1,R) - y1*(x6-x1);
					ans+=h;
				}
				else // 1
				{
					//WR("1\n");
					double h = f(x3,R) - f(x1,R) - y1*(x3-x1);
					ans+=h;
				}
			}
			else //3, 4
			{
				y5 = y2;
				x5 = sqrt(R*R - y5*y5);
				if (x4*x4 + y4*y4 > R*R)//4
				{
					//WR("4\n");
					y6 = y1;
					x6 = sqrt(R*R - y6*y6);
					double h = f(x6,R) - f(x5,R) - y1*(x6-x5) + (x5-x1)*(y2-y1);
					ans+=h;
				}
				else // 3
				{
					//WR("3\n");
					x6 = x3;
					y6 = sqrt(R*R - x6*x6);
					double h = f(x6,R) - f(x5,R) - y1*(x6-x5) + (x5-x1)*(y2-y1);
					ans+=h;
				}
			}
		}
		x+=g+r+r;
	}
	return ans*4.;
}
int main()
{
	init();
	int t;
	double f, R, d, r, g;
	double s, S;
	FOR(t,1,T)
	{
		RE("%lf %lf %lf %lf %lf",&f, &R, &d, &r, &g);
		S = PI * R * R;
		s = 0.;
		R-=(d+f);
		r+=f;
		g-=f;
		g-=f;
		s = get_s(R, r, g);
		s/=S;
		s = 1. - s;
		WR("Case #%d: %.6lf",t,s);
		if (t<T) WR("\n");
	}
	return 0;
}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<_ll> _vll;
typedef vector<string> _vs;
typedef istringstream _iss;
#define _a(v) (v).begin(),(v).end()
#define _e(x,y) (fabs((x)-(y))<1e-10)
#define _p push_back
#define _mp make_pair
#define _m(v) memset(v,0,sizeof(v));
#define _f(i,b,e) for(int i=b;i<e;i++)
#define _fl(i,n) for(int i=0;i<(n).length();i++)
#define _fs(i,n) for(int i=0;i<(n).size();i++)
#define _fe(t,i,n) for(t::iterator i=(n).begin();i!=(n).end();i++)
#define _fd(t,e) ((t).find(e)!=(t).end())
#define _s(x,y) {x+=y;y=x-y;x-=y;}
#define _st(x, y, t) {t _t_; _t_=x;x=y;y=_t_;}

#define PI 3.1415926535897932

#define FILE_INPUT

#ifdef FILE_INPUT
	#define is_ file_in
	#define os_ file_out
#else
	#define is_ cin
	#define os_ cout
#endif

#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
#endif

struct point_t
{
	double x,y;
	point_t()
	{
		x=y=0.0;
	}
	point_t(double sx, double sy)
	{
		x=sx;
		y=sy;
	}
};

struct square_t
{
	point_t left_bottom;
	point_t right_bottom;
	point_t left_top;
	point_t right_top;
};

double f, R, NR, t, r, g, d;


inline double get_distance(point_t p1, point_t p2)
{
	return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

square_t create_square(point_t left_bottom)
{
	square_t ret;
	ret.left_bottom.x	= left_bottom.x + f;
	ret.left_bottom.y	= left_bottom.y + f;
	ret.left_top.x		= left_bottom.x + f;
	ret.left_top.y		= left_bottom.y + g - f;
	ret.right_bottom.x	= left_bottom.x + g - f;
	ret.right_bottom.y	= left_bottom.y + f;
	ret.right_top.x		= left_bottom.x + g - f;
	ret.right_top.y		= left_bottom.y + g - f;
	return ret;
}

double integral(double x, double c)
{
	double d1=x*sqrt(NR*NR-x*x);
	double d2=x*x-NR*NR;
	double d3=atan2(d1, d2);
	return -0.5*d3*NR*NR - c*x + 0.5*x*sqrt(NR*NR-x*x);
}

int main()
{
#ifdef FILE_INPUT
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	int zcnt;
	double ans;
	
	is_>>zcnt;

	point_t center;

	for(int zi=1; zi<=zcnt; zi++)
	{
		double hole = 0.0;

		is_>>f>>R>>t>>r>>g;
		NR = R - t - f;
		d = r*2.0;
		if(g<=2.0*f)
		{
			ans = 1.0;
			goto print_ans;
		}

		for(int i=0; i<=R/g; i++)
		{
			for(int j=0; j<=R/g; j++)
			{
				square_t sq = create_square(point_t(j*(d+g) + r, i*(d+g) + r));
				if(get_distance(center, sq.left_bottom) >= NR)
					continue;
				double dis1, dis2;
				point_t p1, p2;
				dis1 = get_distance(center, sq.left_top);
				dis2 = get_distance(center, sq.right_bottom);
				if(get_distance(center, sq.right_top)<=NR)
				{
					hole += (g-2.0*f)*(g-2.0*f);
				}else	if(dis1<=NR && dis2<=NR)
				{
					p1.y = sq.left_top.y;
					p1.x = sqrt(NR*NR - p1.y*p1.y);
					hole += (g-2.0*f)*(p1.x - sq.left_bottom.x) + integral(sq.right_bottom.x, sq.right_bottom.y) - integral(p1.x, sq.right_bottom.y);
				}else if(dis1<=NR && dis2>=NR)
				{
					p1.y = sq.left_top.y;
					p1.x = sqrt(NR*NR - p1.y*p1.y);
					p2.y = sq.left_bottom.y;
					p2.x = sqrt(NR*NR - p2.y*p2.y);
					hole += (g-2.0*f)*(p1.x - sq.left_bottom.x) + integral(p2.x, sq.right_bottom.y) - integral(p1.x, sq.right_bottom.y);
				}else if(dis1>=NR && dis2<=NR)
				{
					p1.x = sq.left_top.x;
					p1.y = sqrt(NR*NR - p1.x*p1.x);
					p2.x = sq.right_top.x;
					p2.y = sqrt(NR*NR - p2.x*p2.x);
					hole += integral(p2.x, sq.right_bottom.y) - integral(p1.x, sq.right_bottom.y);
				}else
				{
					p2.y = sq.left_bottom.y;
					p2.x = sqrt(NR*NR - p2.y*p2.y);
					hole += integral(p2.x, sq.right_bottom.y) - integral(sq.left_bottom.x, sq.right_bottom.y);
				}
			}
		}

		if(hole>=R*R*PI/4.0)
			ans = 0.0;
		else
			ans = (R*R*PI/4.0 - hole) / (R*R*PI/4.0);

print_ans:
		os_<<"Case #"<<zi<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<ans<<endl;
	}


#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif
	return 0;
}
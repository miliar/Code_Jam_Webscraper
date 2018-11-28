#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; e<= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n, t) t *v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c, t) for(VAR(i, (c).begin() , t); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second



int main()
{
	int cases;
	cin >> cases;

	REP(cas, cases)
	{

		int flies;
		cin >> flies;
		double x=0.0, y=0.0, z=0.0, vx=0.0, vy=0.0, vz=0.0;
		int temp;

		REP(fl, flies)
		{
			cin >> temp;
			x+=temp;
			cin >> temp;
			y+=temp;
			cin >> temp;
			z+=temp;
			cin >> temp;
			vx+=temp;
			cin >> temp;
			vy+=temp;
			cin >> temp;
			vz+=temp;
		}

		x=x/flies;
		y=y/flies;
		z=z/flies;
		vx=vx/flies;
		vy=vy/flies;
		vz=vz/flies;

		long double t;
		if ((vx==0)&&(vy==0)&&(vz==0))
			t=0;
		else
			t = -((x*vx)+(y*vy)+(z*vz))/((vx*vx)+(vy*vy)+(vz*vz));

		if (t<0) t=0;

		long double x0, y0, z0;
		x0=x+t*vx;
		y0=y+t*vy;
		z0=z+t*vz;

		long double d;
		d=sqrt((x0*x0)+(y0*y0)+(z0*z0));

		cout.precision(8);
		cout << "Case #" << cas+1 << ": " << fixed << d << " " << fixed << t << endl;
	}


	return 0;
};
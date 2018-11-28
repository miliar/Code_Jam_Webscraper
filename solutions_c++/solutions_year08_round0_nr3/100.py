#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <iomanip>
#include <ctime>

using namespace std;

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef long double LD;
typedef vector <LL> VLL;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef vector <string> VS;
typedef vector <VS> VVS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(var,pocz,koniec) for(int var=(pocz);var<=(koniec);var++)
#define FORD(var,pocz,koniec) for(int var=(pocz);var>=(koniec>;var--)
#define FOREACH(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define eps 1e-14
#define PI (4*atan(1.0))

/////////////////////////////////////////////////////////////////////////////////
bool onCircle(LD x, LD y, LD R)
{
	LD dis = x*x + y*y - R*R;
	return (dis<eps && dis > -1*eps);
}

bool outside(LD x, LD y, LD R)
{
	LD dis = x*x + y*y -R*R;
	return dis > eps;
}

LD arc(LD len, LD R)
{
	LD height = sqrt( R*R - len*len/4.0);
	LD triangle = len * height /2.0;
	LD shan = asin(len/R/2.0)*R*R;
	return shan-triangle;
}

int main()
{
	int ncases;
	cin >> ncases;
	int index = 0;
	cout << fixed << setprecision(6);
	while(index < ncases)
	{
		index++;
		cout << "Case #" << index << ": ";
		//cout << PI << " " << arc(0.4748, 0.65) << endl;
		/////////////////////////////////

		long double f, R, t, r, g;

		cin >> f >> R >> t >> r >> g;

		LD total_area = R * R * PI;
		R = R-t-f;
		r += f;
		g = g-2*f;

		if (R <= eps or g <= eps or r>=R-eps )
		{
			cout  << 1.0 << endl;
			continue;
		}

		vector <LD> vx;
		vector <LD> vy;

		LD x=0;
		vx.PB(x);
		x = r;
		vx.PB(x);
		while(true)
		{
			x += g;
			if(x>R-eps)
				break;
			vx.PB(x);
			x += 2*r;
			if(x>R-eps)
				break;
			vx.PB(x);
		}
		// vx.PB(R);
		vy = vx;

		LD area = 0.0;

		int n=vx.size();
		for(int i=1; i<n; i=i+2)
		{
			
			for(int j=1; j<n; j=j+2)
			{
				if( outside( vx[i], vy[j], R ))
					break;

				LD x1 = vx[i];
				LD x2 = vx[i]+g;
				LD y1 = vy[j];
				LD y2 = vy[j]+g;

				bool s1 = outside(x2, y1, R);
				bool s2 = outside(x1, y2, R);
				bool s3 = outside(x2, y2, R);

				if( s3 == false )
				{
					area += (x2-x1) * (y2-y1);
				}
				else if (s1==true and s2==false)
				{
					LD z1 = sqrt( R*R - y1*y1);
					LD z2 = sqrt( R*R - y2*y2);
					
					area += (z1-x1+z2-x1)*g/2.0;

					area += arc( sqrt( (z2-z1)*(z2-z1) + g*g ), R);
				}
				else if (s1==false and s2==true)
				{
					LD z1 = sqrt( R*R - x1*x1);
					LD z2 = sqrt( R*R - x2*x2);
					
					area += (z1-y1+z2-y1)*g/2.0;

					area += arc( sqrt( (z2-z1)*(z2-z1) + g*g ), R);
				}
				else if(s1==false and s2==false) 
				{
					LD z1 = sqrt( R*R - x2*x2);
					LD z2 = sqrt( R*R - y2*y2);
					
					area += g*g - (x2-z2)*(y2-z1)/2.0;

					area += arc( sqrt( (x2-z2)*(x2-z2) + (y2-z1)*(y2-z1) ), R);
				}
				else
				{
					LD z1 = sqrt( R*R - x1*x1);
					LD z2 = sqrt( R*R - y1*y1);
					
					area += (z1-y1)*(z2-x1)/2.0;

					area += arc( sqrt( (z1-y1)*(z1-y1) + (z2-x1)*(z2-x1) ), R);

				}
			}
		}
		cout <<  1.0 - (area*4.0)/total_area << endl;
	}
	return 0;
}

#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <set>
#include <map>
#include <iomanip>
#include <math.h>

using namespace std;

ifstream myin("B-large.in");		
ofstream myout("2.out");

inline double _max(double a, double b)
{
	return (a>b?a:b);
}
int main()
{
	int T, N;
	myin >> T;
	for(int i=1; i<=T; ++i)
	{
		double x=0, y=0, z=0, vx=0, vy=0, vz=0, dmin , tmin;
		myin >> N;
		for(int j=0; j<N; ++j)
		{
			double ax, ay, az, avx, avy, avz;
			myin >> ax >> ay >> az >> avx >> avy >> avz;
			x += ax;	y += ay;	z += az;
			vx += avx;	vy += avy;	vz += avz;
		}
		x /= N;	y /= N;	z /= N;
		vx /= N;	vy /= N;	vz /= N;
		double a, b, c; // d(t) = at^2 + bt + c
		a = vx*vx + vy*vy + vz*vz;
		b = 2*(vx*x + vy*y + vz*z);
		c = x*x + y*y + z*z;
		if(a < 0.0000001)
		{
			tmin = 0;
			dmin = sqrt(c);
		}
		else
		{
			tmin = -b / (2*a);
			if(tmin < 0)
			{
				tmin = 0;
				dmin = sqrt(c);
			}
			else
			{
				dmin = sqrt((_max(0, 4*a*c-b*b) ) / (4*a));
			}
		}
		
		myout << "Case #" << i << ": " << fixed << setprecision(8) << dmin << " " << tmin << endl; //Case #X: dmin tmin
	}
	return 0;
}
#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <sstream>
#include <cstdio>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// I uses 1.40.0

#include <boost/foreach.hpp>

#define foreach         BOOST_FOREACH
#define reverse_foreach BOOST_REVERSE_FOREACH

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;
using namespace boost;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		ULL result = 0;

		int num;
		cin >> num;
		double x=0,y=0,z=0,vx=0,vy=0,vz=0;
		int xx,yy,zz,vxx,vyy,vzz;
		int svx=0,svy=0,svz=0;
		for(int i=0;i<num;++i) {
			cin >> xx >> yy >> zz >> vxx >> vyy >> vzz;
			x+=xx; y+=yy; z+=zz; vx+=vxx; vy+=vyy; vz+=vzz;
			svx+=vxx; svy+=vyy; svz+=vzz;
		}
		x/=num; y/=num;z/=num;vx/=num;vy/=num;vz/=num;

		double v2 = vx*vx+vy*vy+vz*vz;
		double a2 = x*x+y*y+z*z;
		double av = x*vx+y*vy+z*vz;

		if(!svx && !svy && !svz) {
			printf("Case #%d: %0.08f %0.08f\n", nn+1, sqrt(a2), 0.0);
		} else if(av <= 0) {
			if(a2 -av*av/v2 < 0) {
				printf("Case #%d: %0.08f %0.08f\n", nn+1, 0.0, fabs(-av/v2));
			} else {
				printf("Case #%d: %0.08f %0.08f\n", nn+1, sqrt(a2-av*av/v2), fabs(-av/v2));
			}
		} else {
			printf("Case #%d: %0.08f %0.08f\n", nn+1, sqrt(a2), 0.0);
		}
	}
	
	return 0;
}

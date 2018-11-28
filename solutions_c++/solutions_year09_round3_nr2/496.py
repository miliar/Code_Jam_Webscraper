#include<algorithm>
#include<cassert>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<iterator>
#include<limits>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
using namespace std;

typedef unsigned long ulong;
typedef unsigned int uint;

#define REP2(var,start,limit) for(int var=(start);var<(limit);++var)
#define REP(i,n) REP2(i,0,n)
#define ITER(x,it) for(typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define RANGE(x) (x).begin(),(x).end()
template<typename T> int SZ(const T& c) { return (int)c.size(); }
template<typename T> T infinity() { return numeric_limits<T>::max(); }


int main()
{
	int T;
	cin >> T;
	for(int c=0;c<T;++c)
	{
		int N;
		cin >> N;
		double px=0.0,py=0.0,pz=0.0;
		double vx=0.0,vy=0.0,vz=0.0;
		REP(i,N)
		{
			int x,y,z,ivx,ivy,ivz;
			cin>>x>>y>>z>>ivx>>ivy>>ivz;
	/*		double dx,dy,dz,dvx,dvy,dvz;
			dx=x/(double)N;
			dy=y/(double)N;
			dz=z/(double)N;
			dvx=ivx/(double)N;
			dvy=ivy/(double)N;
			dvz=ivz/(double)N;*/
			px+=x;py+=y;pz+=z;
			vx+=ivx;vy+=ivy;vz+=ivz;
		}
		px/=(double)N;
		py/=(double)N;
		pz/=(double)N;
		vx/=(double)N;
		vy/=(double)N;
		vz/=(double)N;

		//dot(-p,v)
		double dav=-px*vx + -py*vy + -pz*vz;
		double vv=vx*vx+vy*vy+vz*vz;

		double t = 0.0;
		if(vv > 0.0000001) t = dav / vv;

		if(t<=0.0)t=0.0;

		double dminx = px + t*vx;
		double dminy = py + t*vy;
		double dminz = pz + t*vz;
		double dmin = sqrt(dminx*dminx+dminy*dminy+dminz*dminz);

		cout << "Case #" << c+1 << ": " << setprecision(8)<< fixed << dmin << " "
			<< fixed<< setprecision(8) << t << endl;
	}
}
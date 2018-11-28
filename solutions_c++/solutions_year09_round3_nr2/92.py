#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cctype>
#include <cmath>
#include <numeric>
#include <sstream>
using namespace std;
typedef long long ll;

typedef vector<int> VI;
typedef vector<VI> VVI; 

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))

int N;
double x[500];
double y[500];
double z[500];
double vx[500];
double vy[500];
double vz[500];
double dist( double a, double b, double c ) {
	return sqrt( a*a + b*b + c*c );
}

double M(double t) {
	double xc = 0, yc = 0, zc = 0;
	REP(i,N) {
		xc += x[i] + vx[i] * t;
		yc += y[i] + vy[i] * t;
		zc += z[i] + vz[i] * t;
	}
	return dist(xc/N,yc/N,zc/N);
}

double ternary(){
	double lo = 0.0;
	double hi = 1e100;
	while(hi - lo > hi * 1e-9) {
		double a = (lo*2+hi)/3;
		double b = (lo+hi*2)/3;
		if(M(a)<M(b)) {
			hi = b;
		}
		else {
			lo = a;
		}
	}
	return (lo+hi)*0.5;
}

int main() {
	freopen("d:\\incomming\\B-large.in","r",stdin);
	int tn;
	cin >> tn;
	REP(cc,tn) {
		cin >> N;
		REP(i,N) cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		printf("Case #%d:", cc+1);
		double ret = 0;
		if(M(ret)>M(ternary())) ret =ternary(); else ret = 0;
		printf(" %.7lf %.7lf\n", M(ret), ret);
	}
}



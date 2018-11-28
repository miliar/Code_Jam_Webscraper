#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) cout<<*it<<' '; cout<<endl; }

const double EPS = 1e-6;
const double PI = atan(1)*4;

inline double sq(double x) { return x*x; }

double f, R, t, r, g, rad;

double func(double x) {
	double y = sqrt(sq(rad)-sq(x));
	double mod = 2*r + g;
	x = fmod(x, mod);
	if (x <= r+f || x >= r+g-f) return y;
	else {
		double d = r+f;
		double q = floor((y+d) / mod);
		double ret = q * 2*d - d;
		ret += min(2*d, y+d - q*mod);
		return ret;
	}
}
double simpson(double a, double b) {
	double h, s, prev_s;
	int n = 5000000;
	{
		h = (b-a)/(2*n);
		s = func(b) - func(a);
		for (int i = 0; i < n; i++) {
			s += 2*func(a+h*2*i);
			s += 4*func(a+h*(2*i+1));
		}
		s *= h/3;
	}
	return s;
}

int main() {
	int N; cin>>N;
	for (int testcase = 1; testcase <= N; testcase++) {
		cin>>f>>R>>t>>r>>g;
		rad = R-t-f;
		double alpha = sq(rad)/sq(R);
		double ans = 1.0 - alpha;
		//cerr<<simpson(0,rad)<<endl;
		ans += alpha * simpson(0,rad)*4/(sq(rad)*PI);
		cout.precision(6);
		cout<<"Case #"<<testcase<<": "<<fixed<<ans<<endl;
	}
	return 0;
}

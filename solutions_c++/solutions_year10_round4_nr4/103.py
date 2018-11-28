#include <iostream>
#include <complex>
#include <cmath>
#include <iomanip>
using namespace std;
typedef long double ld;
#define double ld
typedef complex<double> V;
#define x real
#define y imag

int N,M;
V P[1024];
V Q[1024];

double A(double R, double d)
{
	return R*R * acos(d/R) - d*sqrt(R*R-d*d);
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N>>M;
		for(int i=0; i<N; ++i) cin>>P[i].x()>>P[i].y();
		for(int i=0; i<M; ++i) cin>>Q[i].x()>>Q[i].y();

		cout<<"Case #"<<a<<":";
		for(int i=0; i<M; ++i) {
			V q=Q[i];
			V a=P[0], b=P[1];
			double r1 = abs(a-q), r2=abs(b-q);
			double R = r1;
			double r = r2;
			double d = abs(a-b);
			double x = (d*d - r*r + R*R) / (2*d);
			double d1 = x;
			double d2 = d-x;
			double aa = A(R,d1) + A(r,d2);
			cout<<fixed<<setprecision(10)<<" "<<aa;
		}
		cout<<'\n';
	}
}

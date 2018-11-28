#include <iostream>
#include <iomanip>
#include <complex>
using namespace std;
typedef long double ld;
typedef complex<ld> V;
#define x real
#define y imag
int W,L,U,G;

V low[1024];
V hi[1024];

V getp(V a, V b, ld x) {
	V r = a + ((x-a.x()) / (b.x()-a.x()))*(b-a);
//	cout<<"getp "<<x<<" : "<<r<<'\n';
	return r;
}
ld cross(V a, V b) {
//	cout<<"cross "<<a<<' '<<b<<'\n';
	return a.x()*b.y() - a.y()*b.x();
}

ld calcA(ld x) {
	ld A = 0;
	int i;
	for(i=1; low[i].x() < x; ++i) A += cross(low[i-1]-low[0], low[i]-low[0]);
	V ll = getp(low[i-1], low[i], x);
	int j;
	for(j=1; hi[j].x() < x; ++j) A += cross(hi[j]-low[0], hi[j-1]-low[0]);
	V hh = getp(hi[j-1], hi[j], x);

//	cout<<"ij: "<<i<<' '<<j<<" ; "<<A<<" ; "<<ll<<' '<<hh<<'\n';

	A += cross(low[i-1]-low[0], ll-low[0]);
//	cout<<"a "<<A<<'\n';
	A += cross(ll-low[0], hh-low[0]);
//	cout<<"b "<<A<<'\n';
	A += cross(hh-low[0], hi[j-1]-low[0]);

	return A/2;
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cout<<"Case #"<<a<<":\n";
		cin>>W>>L>>U>>G;
		for(int i=0; i<L; ++i) cin>>low[i].x()>>low[i].y();
		for(int i=0; i<U; ++i) cin>>hi[i].x()>>hi[i].y();

		ld A = 0;
		for(int i=2; i<L; ++i) A += cross(low[i-1]-low[0], low[i]-low[0]);
//		cout<<"a "<<A<<'\n';
		A += cross(low[L-1]-low[0], hi[U-1]-low[0]);
//		cout<<"b "<<A<<'\n';
		for(int i=U-2; i>=0; --i) A += cross(hi[i+1]-low[0], hi[i]-low[0]);
		A *= .5;
//		A = calcA(W);

		for(int i=1; i<G; ++i) {
			ld g = A*i/G;
			ld l=0,h=W;
			for(int j=0; j<100; ++j) {
				ld m = .5*(l+h);
				ld a = calcA(m);
				if (a < g) {
					l = m;
				} else {
					h = m;
				}
			}
			cout<<fixed<<setprecision(15)<<h<<'\n';
//			cout<<"res: "<<calcA(h)<<" ; "<<g<<'\n';
		}

//		cout<<A<<'\n';
	}
}

#include <iostream>
#include <cassert>
#include <tr1/random>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <complex>
using namespace std;
typedef complex<double> V;
#define x real
#define y imag

int N;
double W,L;
tr1::mt19937 rng;
double randf() {
	return rng() / (double)rng.max();
}
const int MN = 1024;

double rs[MN];

V pos[MN];
const double eps = 1e-4;

void fix(V& v) {
	if (v.x()<0) v.x()=0;
	if (v.x()>W) v.x()=W;
	if (v.y()<0) v.y()=0;
	if (v.y()>L) v.y()=L;
}

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N>>W>>L;
		for(int i=0; i<N; ++i) cin>>rs[i];
		
		for(int i=0; i<N; ++i) {
			pos[i].x() = randf()*W;
			pos[i].y() = randf()*L;
		}

		while(1) {
			bool fail=0;
			for(int i=0; i<N; ++i) {
				for(int j=0; j<i; ++j) {
					V& a = pos[j];
					V& b = pos[i];
					V dir = b-a;
					double need = rs[i]+rs[j]+eps;
					double dist = abs(dir);
					if (dist >= need) continue;
					V n = dir / dist;
					a -= n*rs[i];
					b += n*rs[j];
					fix(a);
					fix(b);
					fail=1;
				}
			}
			if (!fail) break;
		}
		for(int i=0; i<N; ++i) {
			for(int j=0; j<i; ++j) {
				assert(abs(pos[i]-pos[j]) > rs[i]+rs[j]+eps);
			}
			assert(pos[i].x()>=0);
			assert(pos[i].x()<=W);
			assert(pos[i].y()>=0);
			assert(pos[i].y()<=L);
		}
		cout<<"Case #"<<a<<":";
		for(int i=0; i<N; ++i) cout<<fixed<<setprecision(8)<<' '<<pos[i].x()<<' '<<pos[i].y();
		cout<<'\n';
	}
}

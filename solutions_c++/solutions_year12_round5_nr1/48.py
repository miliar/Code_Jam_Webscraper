// get gmp from http://gmplib.org/ ; ftp://ftp.gmplib.org/pub/gmp-5.0.5/gmp-5.0.5.tar.bz2
#include <gmpxx.h>

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

typedef mpz_class mpz;

mpz pw(int a, int b) {
	mpz r=1;
	for(int i=0; i<b; ++i) r*=a;
	return r;
}

struct S {
	int t,p,i;
	bool operator<(const S& s) const {
		mpz a = pw(p, s.t) * pw(100, t);
		mpz b = pw(s.p, t) * pw(100, s.t);
		if (a==b) return i<s.i;
		return a<b;
	}
} ss[1024];
int ls[1024], ps[1024];

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
		for(int i=0; i<n; ++i) cin>>ls[i];
		for(int i=0; i<n; ++i) cin>>ps[i];
		for(int i=0; i<n; ++i) {
			S& s = ss[i];
			s.t = ls[i];
			s.p = 100-ps[i];
			s.i = i;
		}
		sort(ss,ss+n);
		cout<<"Case #"<<a<<":";
		for(int i=0; i<n; ++i) cout<<' '<<ss[i].i;
		cout<<'\n';
	}
}

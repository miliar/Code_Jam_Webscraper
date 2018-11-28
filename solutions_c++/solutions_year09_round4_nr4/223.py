#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<numeric>
#include<iostream>
#include<sstream>
#include<complex>
#include<cmath>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";int __prv;REP(__prv,sz(X)-1) cout<<(X)[__prv]<<",";cout<<(X).back()<<"}"<<endl;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}
	
// end of pre-inserted code

typedef complex<double> vect;
const double eps = 1e-8;

#define DIM 64
vector<vect> p;
double x[DIM], y[DIM], r[DIM];

int inter(const vect &a, const vect &b, double ra, double rb, vect u[]) {
	double d = abs(a - b);
	if(ra + rb < d + eps) return 0;
	if(ra + rb > d - eps) {
		vect p = b - a;
		p = p / abs(p);
		u[0] = a + p*ra;
		return 1;
	}
	// ra + rb <= d - eps
	double cosa = (ra*ra + d*d - rb*rb) / (2 * ra * d);
	double y = cosa * ra;
	vect p = b - a;
	p = p / abs(p);
	vect m = a + p*y;
	vect n(p.imag(), -p.real());
	double h = ra*ra - y*y;
	if(h < 0) h = 0;
	h = sqrt(h);
	u[0] = m + n*h;
	u[1] = m - n*h;
	return 2;
}

int can(double R, int n) {
	if(n == 1) {
		return R > r[0];
	}
	vector<vect> a;
	REP(i, n) a.pb(p[i]);
	REP(i, n) if(r[i] < R - eps) {
		REP(j, i) if(r[j] < R - eps) {
			vect u[2];
			int c = inter(p[i], p[j], R - r[i], R - r[j], u);
			REP(k, c) a.pb(u[k]);
		}
	}
	vector<lint> mask(sz(a));
	REP(i, sz(a)) {
		lint u = 0;
		REP(j, n) if(abs(a[i] - p[j]) < R - r[j] + eps) {
			u = u + (lint(1)<<j);
		}
		mask[i] = u;
	}
	lint full = (lint(1)<<n) - 1;
	REP(i, sz(a)) REP(j, i) if((mask[i] | mask[j]) == full) return true;
	return false;
}

int main() {
	//freopen("1.txt","r",stdin);
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

	int tc;
	scanf("%d",&tc);
	REP(ttt, tc) {
		int n;
		cerr << "test " << (ttt+1) << "..." << endl;
		scanf("%d",&n);
		
		p.clear();
		REP(i, n) {
			scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);
			p.pb(vect(x[i], y[i]));
		}
		double lo = 1, hi = 2000;
		int it = 0;
		const int maxit = 60;
		while(hi - lo > eps && ++it < maxit) {
			double m = (lo + hi)/2;
			if(can(m, n)) hi = m;
			else lo = m;
		}
		printf("Case #%d: %.7lf\n",ttt+1,(lo+hi)/2);
	}

	fclose(stdout);
	return 0;
}
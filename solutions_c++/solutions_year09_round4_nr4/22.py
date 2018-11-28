#include <stdio.h>
#include <iomanip>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <complex>
#include <cassert>
#include <cstring>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define xx first
#define yy second
#define abso(a) ((a)>0?(a):(-(a)))
typedef long long int lli;
typedef long double ld;
typedef complex<ld> P;

#define EPS 1E-7

inline ld kw(ld r){return r*r;}
inline ld operator^(const P& a,const P& b){return real(a)*imag(b)-imag(a)*real(b);}//iloczyn wektorowy
inline ld operator%(const P& a,const P& b){return real(a)*real(b)+imag(a)*imag(b);}//iloczyn skalarny
inline ld wek(const P& a,const P& b,const P& c){return (b-a)^(c-a);}


inline lli sgn(lli a){if(a>0)return 1;if(a<0)return -1;return 0;}
inline bool por(P&a,P&b){if(real(a)!=real(b))return real(a)<real(b);return imag(a)<imag(b);}

inline bool segment_intersection(P& p1, P& p2, P& q1, P& q2){
	//UWAGA!! Zmienić P na całkowitoliczbowy
	lli s1=sgn(wek(p1,p2,q1)),s2=sgn(wek(p1,p2,q2)),t1=sgn(wek(q1,q2,p1)),t2=sgn(wek(q1,q2,p2));
	if(s1*s2>0||t1*t2>0)return false;
	P a;
	if(!s1&&!s2){
		if(por(p2,p1)){a=p1;p1=p2;p2=a;}
		if(por(q2,q1)){a=q1;q1=q2;q2=a;}
		if(por(p2,q1)||por(q2,p1))return false;
	}
	return true;
			
}

ld point_segment_dist(const P& a,const P& b,const P& p,bool seg=1){
	//UWAGA!! Jeśli seg = 1 to zwracana jest odległość od odcinka
	ld dis=abso((b-a)^(p-b))/abs(b-a);
	if(!seg)return dis;
	ld d1,d2;
	d1=(p-b)%(b-a);
	if(d1>=0)return abs(p-b);
	d2=(p-a)%(a-b);
	if(d2>=0)return abs(p-a);
	return dis;
}

int prosta_prosta(const P& A,const P& B,const P& C,const P& D,P& p){//-1 - proste sie pokrywaja
	if(abs((A-B)^(C-D))<EPS)//AB || CD
		return (abs(wek(A,B,C))<EPS?-1:0);
	ld a=(wek(C,D,A)),b=(A-B)^(C-D);
	p=(B*a+A*(b-a))/b;
	return 1;
}

int prosta_okrag(const P& A,const P& B,const P& C,ld r,P& p,P& q){//zwraca ilosc punktow przeciecia AB i o(C,r)
	ld d=wek(C,A,B)/abs(A-B);
	P z=(A-B)/abs(A-B);
	if(abs(d)>r+EPS) return 0;
	ld x=sqrt(max(kw(r)-kw(d),0.0l));
	p=C+z*P(x,d);
	q=C+z*P(-x,d);
	return (abs(d)<r-EPS?2:1);
}

int okrag_okrag(const P& A,ld rA,const P &B,ld rB,P& p,P& q){
	ld d=abs(B-A);
	if(d>rA+rB+EPS || d<abs(rA-rB)-EPS) return 0;
	P z=(B-A)/d;
	ld x=(d+(kw(rA)-kw(rB))/d)/2;
	if(rA<x) x=rA;
	ld y=sqrt(kw(rA)-kw(x));
	p=A+z*P(x,y);
	q=A+z*P(x,-y);
	return (d<rA+rB-EPS?2:1);
}

int T,N;
#define MAXN 107
P p[MAXN];
ld r[MAXN];

bool test(ld q){
	vector<P> v;
	REP(i,N) v.PB(p[i]);
	P a,b;
	REP(i,N) REP(j,i){
	int x=okrag_okrag(p[i],abs(r[i]-q), p[j],abs(r[j]-q),a,b);
		if(x>=1) v.PB(a);
		if(x>=2) v.PB(b);
	}
	FORE(i,v) FORE(j,v){
		bool zle=false;
		REP(k,N) if(abs(p[k]-*i) > q-r[k]+EPS && abs(p[k]-*j) > q-r[k]+EPS){zle=true; break;}
		if(!zle) return true;
	}
	return false;
}

int main(){
	cin >> T;
	FOR(cas,1,T){
		cin >> N;
		REP(i,N){
			ld x,y;
			cin >> x >> y >> r[i];
			p[i]=P(x,y);
		}
		ld a=0,b=10000;
		REP(q,100){
			ld q=(a+b)/2;
			if(test(q)) b=q;
			else a=q;
		}
		cout << "Case #" << cas << ": " << setprecision(10) << (a+b)/2 << endl;
	}
return 0;
}


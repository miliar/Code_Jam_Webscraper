#define DBG
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <list>
#include <map> 
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

int __tmp;
#define scanf __tmp = scan ## f

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,ee,bb) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define ST first
#define ND second
#define PB push_back
#define PP pop_back
#define MP make_pair

template<typename S,typename T>
pair<S,T> operator+(const pair<S, T>& lhs, const pair<S, T>& rhs) {
	return pair<S,T>(lhs.ST + rhs.ST, lhs.ND + rhs.ND);
}
template<typename S,typename T>
pair<S,T> operator-(const pair<S, T>& lhs, const pair<S, T>& rhs) {
	return pair<S,T>(lhs.ST - rhs.ST, lhs.ND - rhs.ND);
}
template<typename S,typename T, typename K>
pair<S,T> operator*(const pair<S, T>& lhs, const K& rhs) {
	return pair<S,T>(lhs.ST * rhs, lhs.ND * rhs);
}
template<typename S,typename T>
pair<S,T>& operator+=(pair<S, T>& lhs, const pair<S, T>& rhs) {
	lhs.ST += rhs.ST;
	lhs.ND += rhs.ND;
	return lhs;
}
template<typename S,typename T>
pair<S,T>& operator-=(pair<S, T>& lhs, const pair<S, T>& rhs) {
	lhs.ST -= rhs.ST;
	lhs.ND -= rhs.ND;
	return lhs;
}
template<typename S,typename T>
const char* operator~(const pair<S, T>& rhs) {
	stringstream s; 
	s << "(" << rhs.ST << "," << rhs.ND << ")";
	string* r = new string; 
	s >> *r;
	return r->c_str();
}

typedef long double real;
typedef pair<real,real> prr;

real segment_area(pair<prr,prr> s) {
	return (s.ND.ST - s.ST.ST) // width
		* // * avg
		(s.ND.ND + s.ST.ND) / 2;
}

pair<prr,prr> crop(prr from, prr to, double x) {
	prr resto;
	if(x < to.ST) {
		resto.ST = x;
		resto.ND = from.ND + (x - from.ST) * (to.ND - from.ND) / (to.ST - from.ST);
	} else resto = to;
	return MP(from,resto);
}

struct sum_prime {
	vector<prr> t;
	sum_prime(vector<prr>& t): t(t) {}
	real sum(real x) {
		real r = 0;
		REP(i,t.size() - 1) if(x > t[i].ST)
			r += segment_area(crop(t[i], t[i+1], x));
		return r;
	}
};

struct sum_two {
	sum_prime s;
	sum_two(vector<prr>& t): s(t) {}
	real sum(real a, real b) {
		return s.sum(b) - s.sum(a);
	}
};

struct sum_area {
	sum_two lo, hi;
	sum_area(vector<prr>& lo, vector<prr>& hi): lo(lo), hi(hi) {}
	real sum(real a, real b) {
		return hi.sum(a,b) - lo.sum(a,b);
	}
};

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		int w,l,u,g;
		scanf("%d%d%d%d", &w, &l, &u, &g);
		vector<prr> lo, hi;
		REP(i,l) {
			prr tmp; scanf("%Lf%Lf", &tmp.ST, &tmp.ND);
			lo.PB(tmp);
		}
		REP(i,u) {
			prr tmp; scanf("%Lf%Lf", &tmp.ST, &tmp.ND);
			hi.PB(tmp);
		}	
		printf("Case #%d:\n", zz);
		sum_area sums(lo,hi);	
		real start = 0;
		real end = w;
		REP(gg,g - 1) {
			real todo = sums.sum(0,w) / g;
			real b = start;
			real e = end;
			while(e - b > 0.00000001) {
				double s = (e + b) / 2;
				if(sums.sum(start, s) > todo) e = s;
				else b = s;
			}
			start = b;
			printf("%.9Lf\n", start);
		}
	}
	return 0;
}


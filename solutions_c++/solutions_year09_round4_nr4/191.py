#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

#define sz(q) ((int)(q).size())
#define _fill(mem,v) memset(mem,v,sizeof(mem))
#define FOR(i,q1,q2) for(int i=(q1); i<=(q2); ++i)
#define FORD(i,q1,q2) for(int i=(q1); i>=(q2); --i)
#define FOREACH(it,mp) for(typeof((mp).begin()) it=(mp).begin(); it!=(mp).end(); ++it)

#define isdig(c) ('0'<=(c) && (c)<='9')

#define inbit(i,n) ((n & (1<<i))>0?1:0)
#define bit(i) (1<<i)

#define mp make_pair
#define xx first
#define yy second

#define BINEPS (1e-13)
#define EPS (1e-13)
#define eq(v1,v2) (abs((v1)-(v2)) < 1e-10)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int N;

bool debug;

struct POINT {
	double x,y,r;
	
	POINT(double _x, double _y, double _r) {
		x = _x;
		y = _y;
		r = _r;
	}
	
	POINT() {
		x = y = r = 0;
	}
	
	void read() {
		scanf("%lf%lf%lf", &x, &y, &r);
	}
	
	double dist(const POINT &p) const {
		return sqrt((x-p.x)*(x-p.x) + (y-p.y)*(y-p.y));
	}
	
	bool covered(POINT &p, double R) {
		return (dist(p)+r <= R+EPS);
	}
	
	void setLen(double len) {
		double curlen = sqrt(x*x + y*y);
		x = x*len/curlen;
		y = y*len/curlen;
	}
	
	POINT operator+(const POINT &p) const {
		return POINT(x+p.x, y+p.y, 0);
	}
	
	POINT operator-(const POINT &p) const {
		return POINT(x-p.x, y-p.y, 0);
	}
	
	pair<POINT, POINT> getContainCenter(const POINT &p, double R) const {
		double r1 = R-r, r2 = R-p.r, dd = dist(p);
		if( dd>r1+r2 ) return make_pair(POINT(-1,-1,-1), POINT(-1,-1,-1));
		double x2 = (dd*dd - r1*r1 + r2*r2)/(2*dd);
		double h = sqrt(r2*r2 - x2*x2);
		double x1 = sqrt(r1*r1 - h*h);
		if( !eq(x1+x2, dd) )
			cerr << "x1+x2 != dd" << endl;
		
		POINT vec = p - (*this);
		vec.setLen(x1);
		POINT cent = vec + (*this);
		
		swap(vec.x, vec.y);
		vec.x = -vec.x;
		vec.setLen(h);
		
		POINT pc1 = cent+vec, pc2 = cent-vec;
		if( !eq(pc1.dist(*this), r1) ) cerr << "r1 incor" << endl;
		if( !eq(pc2.dist(p), r2) ) cerr << "r2 incor" << endl;
		
		return make_pair(pc1, pc2);
	}
	
	void print() {
		printf("%.1lf , %.1lf\n", x, y);
	}
}pl[100];

bool allCovered(double R,pair<POINT, POINT> &c1, pair<POINT, POINT> &c2) {
/*
	c1.xx.print();
	c1.yy.print();printf("\n");
	c2.xx.print();
	c2.yy.print();printf("---------------------\n");
*/
	
	
	bool ok = true;
	for(int q=0; q<N && ok; ++q)
		if( !pl[q].covered(c1.xx, R) && !pl[q].covered(c2.xx, R) )
			ok = false;
	if( ok ) return true;
	
	ok = true;
	for(int q=0; q<N && ok; ++q)
		if( !pl[q].covered(c1.xx, R) && !pl[q].covered(c2.yy, R) )
			ok = false;
	if( ok ) return true;

	ok = true;
	for(int q=0; q<N && ok; ++q)
		if( !pl[q].covered(c1.yy, R) && !pl[q].covered(c2.xx, R) )
			ok = false;
	if( ok ) return true;

	ok = true;
	for(int q=0; q<N && ok; ++q)
		if( !pl[q].covered(c1.yy, R) && !pl[q].covered(c2.yy, R) )
			ok = false;
	if( ok ) return true;
	
	return false;
}

bool canPlace2(double R, pair<POINT, POINT> &c1) {
	for(int k=0; k<N; ++k) {
		pair<POINT, POINT> c2 = make_pair(pl[k], pl[k]);
		if( allCovered(R, c1,c2) ) return true;
	}
	
	for(int k=0; k<N; ++k)
		for(int e=k+1; e<N; ++e) {
			pair<POINT, POINT> c2 = pl[k].getContainCenter(pl[e], R);
			if( c2.xx.r>=0 )
				if( allCovered(R, c1,c2) ) return true;
		}
	return false;
}

bool canPlace1(double R) {
	for(int i=0; i<N; ++i) {
		pair<POINT, POINT> c1 = make_pair(pl[i], pl[i]);
		if( canPlace2(R, c1) ) return true;
	}
	
	for(int i=0; i<N; ++i)
		for(int j=i+1; j<N; ++j) {
			pair<POINT, POINT> c1 = pl[i].getContainCenter(pl[j], R);
			if( c1.xx.r>=0 )
				if( canPlace2(R, c1) ) return true;
		}
	return false;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int it=1; it<=T; ++it) {
		scanf("%d", &N);
		for(int i=0; i<N; ++i)
			pl[i].read();
		
		//cout << allCovered(26, make_pair(POINT(120,115,0),POINT()), make_pair(POINT(125,500,0),POINT())) << endl;return 0;
		//debug = true;cout << canPlace1(51) << endl;return 0;
		
		double l1 = 1, l2 = 2000;
		while( l1 + BINEPS < l2 ) {
			double l = (l1+l2)/2;
			//cout << l << " - " << canPlace1(l) << endl;
			if( canPlace1(l) ) l2 = l;
			else l1 = l;
		}
		//debug = true;cout << canPlace1(26.164098168761047) << endl;return 0;
		double R = l2;
		printf("Case #%d: %.6lf\n", it, R);
	}
	return 0;
}

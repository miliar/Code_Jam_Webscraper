#define DBiG
// Grzegorz Guspiel
#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

const int maxn=50;
const double bseps=0.000001;
const double eps=0.000001;

struct tcircle {
	double x,y,r,rr;
};
tcircle t[maxn];
int n;
bool match[maxn];

void get_data() {
	scanf("%d", &n);
	REP(i,n) {
		int a,b,c; scanf("%d%d%d", &a, &b, &c);
		t[i].x=a;
		t[i].y=b;
		t[i].r=c;
	}
}

double howf(double x1, double y1, double x2, double y2) {
	return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}
double abs(double a) { if(a<0) a=-a; return a; }
double sq(double a) { return a*a; }

void checkbel(double x, double y, double r) {
	R("checkbel x="<<x<<" y="<<y<<" r="<<r);
	REP(i,n) if(howf(t[i].x,t[i].y,x,y)+t[i].r<=r+eps) {
		match[i]=1;
	}
}

void makematch(int c1, int c2, double r) {
	t[c1].rr=r-t[c1].r;
	t[c2].rr=r-t[c2].r;
	if(t[c1].rr<=0 || t[c2].rr<=0) return;
	double d = howf(t[c1].x,t[c1].y,t[c2].x,t[c2].y);
	if(d>t[c1].rr+t[c2].rr||d<abs(t[c1].rr-t[c2].rr)) return;
	double a = (sq(t[c1].rr)-sq(t[c2].rr)+sq(d))/(d*2);
	double h = sqrt(sq(t[c1].rr)-sq(a));
	double x2=t[c1].x+a*(t[c2].x-t[c1].x)/d;
	double y2=t[c1].y+a*(t[c2].y-t[c1].y)/d;
	double x3=x2+h*(t[c2].y-t[c1].y)/d;
	double y3=y2-h*(t[c2].x-t[c1].x)/d;
	R("x2="<<x2<<" y2="<<y2<<" d="<<d<<" a= "<<a<<" h="<<h);
	checkbel(x3,y3,r);
}

bool ok(double r) {
	REP(c1,n) FOR(c2,0,n-1) REP(c3,n) FOR(c4,0,n-1) {
		REP(i,n) match[i]=0;
		makematch(c1,c2,r);
		makematch(c3,c4,r);
		bool result=1;
		int bads=0;
		REP(i,n) if(!match[i]) { bads++; result=0;}
		R("bads = "<<bads);
		if(result) return 1;
	}
	REP(c1,n) FOR(c2,0,n-1) REP(c3,n) FOR(c4,0,n-1) {
		REP(i,n) match[i]=0;
		makematch(c1,c2,r);
		checkbel(t[c3].x,t[c3].y,r);
		bool result=1;
		int bads=0;
		REP(i,n) if(!match[i]) { bads++; result=0;}
		R("bads = "<<bads);
		if(result) return 1;
	}
	REP(c1,n) FOR(c2,0,n-1) REP(c3,n) FOR(c4,0,n-1) {
		REP(i,n) match[i]=0;
		checkbel(t[c1].x,t[c1].y,r);
		checkbel(t[c3].x,t[c3].y,r);
		bool result=1;
		int bads=0;
		REP(i,n) if(!match[i]) { bads++; result=0;}
		R("bads = "<<bads);
		if(result) return 1;
	}
	return 0;
}

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		get_data();
		double b=bseps;
		double e=10000;
		while(b+bseps<e) {
			double s=(b+e)/2;
			if(ok(s)) e=s;
			else b=s;
		}
		printf("Case #%d: %lf\n", zz, b);
	}
}

#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define SQR(x) ((x)*(x))

double IntergalCircle(double x,double r) {
	return x/2.0*sqrt(SQR(r)-SQR(x))+SQR(r)/2*asin(x/r);
}

double BelowCircle(double x1,double x2,double r) {
	if(x1<-r)x1=-r;
	if(x2>r)x2=r;
	return IntergalCircle(x2,r)-IntergalCircle(x1,r);
}
int sign(double x) {
	return x>0?1:-1;
}
double SqS(double x1,double x2,double y1,double y2,double r) {
	
	if(x1<-r)x1=-r;
	if(x2>r)x2=r;
	if(y1<-r)y1=-r;
	if(y2>r)y2=r;
	if(x1>x2||y1>y2)return 0.0;
	bool in11=(SQR(x1)+SQR(y1)<=SQR(r));
	bool in12=(SQR(x1)+SQR(y2)<=SQR(r));
	bool in21=(SQR(x2)+SQR(y1)<=SQR(r));
	bool in22=(SQR(x2)+SQR(y2)<=SQR(r));
	if(!in11&&!in12&&!in21&&!in22)return 0.0;
	double upper,lower;
	if(in12&&in22)upper=y2*(x2-x1);
	else {
		double ic1,ic2;
		ic2=sqrt(SQR(r)-SQR(y2));
		ic1=-ic2;
		ic1=max(ic1,x1);
		ic2=min(ic2,x2);
		if(ic1>ic2)upper=BelowCircle(x1,x2,r)*sign(y2);
		else upper=y2*(ic2-ic1)+BelowCircle(x1,ic1,r)*sign(y2)+BelowCircle(ic2,x2,r)*sign(y2);
	}
	if(in11&&in21)lower=y1*(x2-x1);
	else {
		double ic1,ic2;
		ic2=sqrt(SQR(r)-SQR(y1));
		ic1=-ic2;
		ic1=max(ic1,x1);
		ic2=min(ic2,x2);
		if(ic1>ic2)lower=+BelowCircle(x1,x2,r)*sign(y1);
		else lower=y1*(ic2-ic1)+BelowCircle(x1,ic1,r)*sign(y1)+BelowCircle(ic2,x2,r)*sign(y1);
	}
	return upper-lower;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int n,test;
	for(cin>>n,test=1;test<=n;++test) {
		double f, R, t, r, g;
		cin>>f>>R>>t>>r>>g;
		t+=f;
		r+=f;
		g-=2*f;
		double s1=0.0,s2=0.0;
		s2=M_PI*SQR(R);// racquet circle
		
		double xc,yc;
		s1=0;
		double bc=(10+ceil(R/(g+2*r)))*(g+2*r);
		for(xc=-bc;xc<=bc;xc+=g+2*r)
			for(yc=-bc;yc<=bc;yc+=g+2*r)
				s1+=SqS(xc+r,xc+r+g,yc+r,yc+r+g,R-t);
		printf("Case #%d: %.10lf\n",test,1.0-s1/s2);
	}
	
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 

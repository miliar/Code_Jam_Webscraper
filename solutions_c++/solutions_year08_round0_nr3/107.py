#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <cmath>
#include <cassert>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)
#define eps 1e-9

int inside(double x1,double y1,double r){
	return x1*x1 + y1*y1 <= r*r + eps;
};

double solve3(double x1,double y1,double x2,double y2,double r){
	double th1 = asin(y1/r);
	double th2 = asin(y2/r);
	return 0.5*r*r*(th1-th2-0.5*(sin(2*th1)-sin(2*th2)));
};

double solve2(double x0,double y0,double s,double R){
	if(inside(x0+s,y0+s,R))return s*s;
	if(!inside(x0,y0,R))return 0;
	double x1,y1,x2,y2;
	if(inside(x0,y0+s,R)){
		y1 = y0+s;
		x1 = sqrt(R*R-y1*y1);
		if(inside(x0+s,y0,R)){
			x2 = x0+s;
			y2 = sqrt(R*R-x2*x2);
		}
		else{
			y2 = y0;
			x2 = sqrt(R*R-y2*y2);
		}
		return (x1-x0)*s + solve3(x1,y1,x2,y2,R) - fabs(x1-x2)*y0;
	}
	x1 = x0;
	y1 = sqrt(R*R-x1*x1);
	if(inside(x0+s,y0,R)){
		x2 = x0+s;
		y2 = sqrt(R*R-x2*x2);
		return solve3(x1,y1,x2,y2,R) - fabs(x1-x2)*y0;
	}
	y2 = y0;
	x2 = sqrt(R*R-y2*y2);
	return solve3(x1,y1,x2,y2,R) - fabs(x2-x1)*y0;
};

double f,R,t,r,g;
double solve(){
	if(t+f >= R || f+f >= g)return 1;
	double Area = M_PI*R*R;
	double ret=0;int i,j;
	FOR(i,1024){
		FOR(j,1024){
			double x0 = (g+r+r)*j+r,y0 = (g+r+r)*i+r;
			ret+=solve2(x0+f,y0+f,g-f-f,R-t-f);
		}
	}
	return 1.0-(ret*4/Area);
};

int main(){
	int cas;
	cin >> cas;
	for(int it=1;it<=cas;it++){
		cin >> f >> R >> t >> r >> g;
		double ans = solve();
		char buf[128];
		sprintf(buf,"%#.6f",ans);
		cout << "Case #"<<it << ": "<<string(buf)<<endl;
	}
	return 0;
}

#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
using namespace std; 

#define REP(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i) 
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it) 
#define CLR(x) memset((x),0,sizeof((x))) 
typedef long long LL; 
typedef vector<int> VI; 
typedef vector<string> VS; 

double xmult(double x1,double y1,double x2,double y2,double x0,double y0){
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

double area_triangle(double x1,double y1,double x2,double y2,double x3,double y3){
	return fabs(xmult(x1,y1,x2,y2,x3,y3))/2;
}

LL N, M, A;

void run() {
	cin >> N >> M >> A;

	if (N * M < A) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	int x1, y1, x2, y2, x3, y3;

	vector<int> xx, yy;
	REP(i,N+1) {
		REP(j,M+1) {
			xx.push_back(i);
			yy.push_back(j);
		}
	}

	LL total = (N + 1) * (M + 1);

	REP(i,total) {
		FOR(j,i+1,total-1) {
			FOR(k,j+1,total-1) {
				x1 = xx[i], y1 = yy[i];
				x2 = xx[j], y2 = yy[j];
				x3 = xx[k], y3 = yy[k];

				LL t = (LL)(x1 - x3) * (LL)(y2 - y3) - (LL)(x2 - x3) * (LL)(y1 - y3);
				if (t < 0) t *= -1;

				if (t == A) {
					cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
					return;
				}
			}
		}
	}

	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int kase;
	cin >> kase;
	REP(k,kase) {
		cout << "Case #" << k + 1 << ": ";
		run();
	}
	return 0;
}

#include "stdafx.h"
#include <iostream>
#include <map>
#include <cmath>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int dp[1001][200];
const long double NN=1<<20;
const double M_PI = 2*atan2(1.,0.);

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		map<string,int> engines;
		cout << "Case #" << ts << ": ";
		long double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		t+=f;
		r+=f;
		g-=2*f;
		long double R1=R-t;
		if(g<=0 || t>=R) {
			cout << "1.0000000" << endl;
			continue;
		}
		long double area=0;
		long double y=r;
		const int NN=2*ceil(1000000/R1*(r+r+g));
		while(y<R1) {
			long double y2=y+g;
			long double dy=g/NN;
			long double y1=y;
			for(int n=0; n<=NN; n++) {
				long double w=sqrt(R1*R1-y1*y1);
				long double m=dy/3*(n==0||n==NN?1:2*(n%2)+2);
				if(w<w+1); else break;
				area+=g*floor(w/(r+r+g))*m;
				area+=max((long double)0.0,min(g,fmod(w,r+r+g)-r))*m;
				y1+=dy;
			}
			y+=r+r+g;
		}
		printf("%.7lf\n", (double)(1-4*area/(M_PI*R*R)));
	}
}

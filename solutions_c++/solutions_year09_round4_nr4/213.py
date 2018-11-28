#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int n;
double ans;

struct po {
	double x,y;
	po() {
		x=0; y=0;
	}
	po(double xx,double yy) {
		x=xx;
		y=yy;
	}
};

po operator- (po p,po q) {
	return po(p.x-q.x,p.y-q.y);
}

double dist(po p) {
	return sqrt(p.x*p.x+p.y*p.y);
}

struct cc {
	po p;
	double r;
};

cc c[5];

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>n;
		ans=9999999;
		cout<<fixed;
		for(int i=0;i<n;i++) {
			cin>>c[i].p.x>>c[i].p.y>>c[i].r;
		}
		if (n==1) ans=c[0].r;
		if (n==2) ans=max(c[1].r,c[0].r);
		
		for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) {
			cc a=c[i];
			cc b=c[j];
			double r=(a.r+b.r+dist(a.p-b.p))*0.5;
			for(int k=0;k<n;k++) if (c[k].r>r) r=c[k].r;
			if (r<ans) ans=r;
		}
		cout.precision(6);
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}

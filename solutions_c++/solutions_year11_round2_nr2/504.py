#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int points[1000000], p, C, D;
bool check(double t) {
	double lp=-1e20;
	for(int i=0;i<p;i++) {
		lp=max(lp+D, points[i]-t);
		if(lp-points[i]>t) return false;
	}
	return true;
}

double solve() {
	p=0;
	scanf("%d%d", &C, &D);
	for(int i=0;i<C;i++) {
		int P, V;
		scanf("%d%d", &P, &V);
		for(int j=0;j<V;j++) {
			points[p++]=P;
		}
	}
	double mn=0, mx=1e13;
	int t=0;
	while(mx-mn>1e-8) {
		double mid=(mn+mx)/2;
		if(check(mid)) {
			mx=mid;
		} else {
			mn=mid;
		}
		t++;
		if(t>=90) break;
	}
	return (mn+mx)/2;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: %.12lf\n", c, solve());
	}
}
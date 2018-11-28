#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

double sqr(double x) { return x*x; }

double dist(double a, double b) {
	return sqrt(sqr(a)+sqr(b));
}

int x[40],y[40];
double r[40];

double mini(int a, int b) {
	return (dist(x[a]-x[b], y[a]-y[b])+r[a]+r[b])/2.0;
}

int main() {
	int n,nt;
	
	scanf(" %d",&nt);
	for (int ct=1; ct<=nt; ct++) {
		scanf(" %d",&n);
		for (int i=0; i<n; i++)
			scanf(" %d %d %lf",&x[i],&y[i],&r[i]);
		
		double res;
		if (n==1) res=r[0];
		else if (n==2) res=max(r[0],r[1]);
		else res=min(max(mini(0,1),r[2]),min(max(mini(0,2),r[1]),max(mini(1,2),r[0])));
		
		printf("Case #%d: %lf\n",ct,res);
	}
	
	return 0;
}

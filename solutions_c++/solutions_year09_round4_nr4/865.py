#include <stdio.h>
#include <math.h>

int x[100];
int y[100];
int r[100];

double dis(double x, double y) {
	return sqrt(x*x+y*y);
}

double cal(int i, int j) {
	double d = dis(x[i]-x[j], y[i]-y[j]);
	if (d+r[i]<r[j]) return r[j];
	if (d+r[j]<r[i]) return r[i];
	return (d+r[i]+r[j])/2;
}

double max(double x, double y) {
	if (x>y) return x;
	return y;
}

double min(double x, double y, double z) {
	if (x<=y && x<=z) return x;
	if (y<=z && y<=x) return y;
	return z;
}

int main() {
	int TC, T;
	int i;
	double ans;
	freopen("1.txt", "r",stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d",&TC);
	for(T=1;T<=TC;T++) {
		int n;
		scanf("%d",&n);
		for(i=0;i<n;i++) {
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		}
		if (n==1) {
			ans=r[0];
		}
		else if (n==2) {
			ans=min(cal(0,1),max(r[0],r[1]),max(r[0],r[1]));
		}
		else {
			ans=min(
				max(cal(0,1),r[2]),
				max(cal(0,2),r[1]),
				max(cal(1,2),r[0]));
		}
		printf("Case #%d: %.6lf\n", T, ans);
	}
	return 0;
}
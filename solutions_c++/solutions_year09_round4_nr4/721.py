#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define eps 1e-11
#define oo 1e20
#define feq(x,y) (fabs((x)-(y))<eps)
int N;
double x[1000], y[1000], r[1000];
int main() {
	int T; scanf("%d", &T);
	for (int cas=1;cas<=T;cas++) {
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		memset(r, 0, sizeof(r));
		scanf("%d", &N);
		for (int i=0;i<N;i++) {
			scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
		}
		double mn=oo;
		if (N==1)	{ printf("Case #%d: %.6f\n", cas, r[0]); continue;}
		if (N==2)	{ printf("Case #%d: %.6f\n", cas, max(r[0],r[1])); continue;}
		for (int i=0;i<N;i++) {
			for (int j=i+1;j<N;j++) {
				double dx = x[i]-x[j];
				double dy = y[i]-y[j];
				double d = sqrt(dx*dx+dy*dy) + r[i] + r[j];
				mn = min(d, mn);
			}
		}
		printf("Case #%d: %.6f\n", cas, 0.5*mn*(1+eps));
	}
	

}

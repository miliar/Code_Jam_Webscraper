#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

int main() {
	int t;
	scanf("%d", &t);
	int g=1;
	while (t--) {
		int n;
		scanf("%d", &n);
		int x[n],y[n],r[n];
		for (int i=0;i<n;i++)
			scanf("%d%d%d",x+i,y+i,r+i);
		printf("Case #%d: ", g++);
		if (n==1) { printf("%.6f\n", (double)r[0]); continue; }
		if (n==2) { printf("%.6f\n", (double)max(r[0],r[1])); continue; }
		double ans = 1e40;
		for (int i=0;i<n;i++) {
			int a=(i+1)%3, b=(a+1)%3;
			double dx=x[a]-x[b], dy=y[a]-y[b];
			double rr=sqrt(dx*dx+dy*dy)+r[a]+r[b];
			ans = min(ans, max(rr,(double)r[i])/2);
		}
		printf("%.6f\n", ans);
	}
	return 0;
}

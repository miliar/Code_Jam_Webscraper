#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>

#define EPS 1e-9

using namespace std;

double dist_pp(double x1, double y1, double x2, double y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

int main() {
	int cases, t = 1;
	long long A, B, C, D, x0, y0, M, n, ans;
	int i, j, k;
	double dist[105][105];
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		vector <int> x(n), y(n);
		x[0] = x0, y[0] = y0;
		for (i=1; i < n; i++) {
			x[i] = (A * x[i-1] + B) % M;
			y[i] = (C * y[i-1] + D) % M;
			for (j=0; j < i; j++)
				dist[j][i] = dist[i][j] = dist_pp(x[i],y[i],x[j],y[j]);
		}
		
		ans = 0;
		for (i=0; i < n; i++) {
			for (j=i+1; j < n; j++) {
				for (k=j+1; k < n; k++)
					ans += ((x[i]+x[j]+x[k])%3 == 0 && (y[i]+y[j]+y[k])%3 == 0);
			}
		}
		
		printf("Case #%d: %lld\n",t++,ans);
	}
	
	return 0;
}

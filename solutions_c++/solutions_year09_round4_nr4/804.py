#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
#define N 1111
long ntests,x[N],y[N],r[N],n;

inline double dis(long x1, long y1, long x2, long y2) {
	return sqrt((double) (x1-x2)*(x1-x2) + (double) (y1-y2)*(y1-y2));
}

inline double max(double a, double b) {
	if (a>b) return a;
	else return b;
}

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d\n",&ntests);
	for (long _=1;_<=ntests;_++) {
	        scanf("%d\n",&n);
	        for (long i=1;i<=n;i++) scanf("%d%d%d\n",&x[i],&y[i],&r[i]);

	        double ans = 2000;
	        if (n==3) {
		ans <?= max((r[1]+r[2]+dis(x[1],y[1],x[2],y[2]))/2.0,r[3]);
		ans <?= max((r[1]+r[3]+dis(x[1],y[1],x[3],y[3]))/2.0,r[2]);
		ans <?= max((r[3]+r[2]+dis(x[3],y[3],x[2],y[2]))/2.0,r[1]);
		}
		if (n==2) {
			ans = r[1];
			ans >?= r[2];
		}
		if (n==1) ans = r[1];
                
		printf("Case #%d: %lf\n",_,ans);
	}

	return 0;
}

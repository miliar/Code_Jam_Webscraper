#include "stdio.h"
#include "algorithm"
#include "cmath"
using namespace std;
double x[41],y[41],r[41];
double Distance(double a,double b,double c,double d) {
	return sqrt((a-c)*(a-c) + (b-d)*(b-d));
}
int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int T,n;
	scanf("%d",&T);
	for(int cas = 1; cas <= T ; cas ++) {
		scanf("%d",&n);
		for(int i = 0 ; i < n ; i ++) {
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		}
		printf("Case #%d: ",cas);
		if(n == 1) {
			printf("%.10lf\n",r[0]);
		} else if(n == 2) {
			printf("%.10lf\n",max(r[0],r[1]));
		} else if(n == 3) {
			double dis = (Distance(x[0],y[0],x[1],y[1]) + r[0] + r[1])/2;
			double ans = max(dis,r[2]);

			dis = (Distance(x[0],y[0],x[2],y[2]) + r[0] + r[2])/2;
			ans = min(ans,max(dis,r[1]));

			dis = (Distance(x[2],y[2],x[1],y[1]) + r[2] + r[1])/2;
			ans = min(ans,max(dis,r[0]));

			printf("%.10lf\n",ans);
		}
	}
	return 0;
}
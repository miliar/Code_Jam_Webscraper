#include <iostream>
#include <cmath>

using namespace std;

double x[4],y[4],r[4];

double dis(double x1,double y1,double x2,double y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main(){
	freopen("D.in","r",stdin); freopen("D.out","w",stdout);
	int t1,t2 = 0;
	scanf("%d\n",&t1);
	while (t1){
		t1--; t2++;
		printf("Case #%d: ",t2);
		int n;
		scanf("%d\n",&n);
		for (int i=1; i<=n; ++i)
			scanf("%lf %lf %lf\n",&x[i],&y[i],&r[i]);
		switch (n){
		case 1:
			printf("%.6f\n",r[1]); break;
		case 2:
			if (r[1] > r[2]) printf("%.6f\n",r[1]); else printf("%.6f\n",r[2]);  break;
		case 3:
			double d1 = dis(x[1],y[1],x[2],y[2])+r[1]+r[2], d2 = dis(x[2],y[2],x[3],y[3]) +r[2]+r[3], d3 = dis(x[1],y[1],x[3],y[3])+r[1]+r[3];
			double t1 = max(d1/2,r[3]) , t2 = max(d2/2,r[1]),t3 = max(d3/2,r[2]);
			if (t1 <=t2 && t1 <=t3)
				printf("%.6f\n",t1);
			else if (t2<=t3)
				printf("%.6f\n",t2); else printf("%.6f\n",t3);
		}
	}
}

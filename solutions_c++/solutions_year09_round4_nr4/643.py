#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>

using namespace std;

double x[10], y[10], r[10];

double dist(int i, int j){
	return sqrt( (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]) );
}

int main(){
	freopen("in", "rt", stdin);
	freopen("out", "wt", stdout);
	int ntest, n;
	double ans;
	scanf("%d", &ntest);
	for (int itest=0; itest<ntest; ++itest){
		scanf("%d", &n);	
		for (int i=0; i<n; ++i)
			scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);	
		if (n==1) ans = r[0];
		else
		if (n==2) ans = max(r[0], r[1]);
		else{
			ans = max(r[0], (dist(1, 2)+r[1]+r[2])/2);
			ans = min(ans, max(r[1], (dist(0, 2)+r[0]+r[2])/2));
			ans = min(ans, max(r[2], (dist(1, 0)+r[1]+r[0])/2));		
		}		
		printf("Case #%d: %.6lf\n", itest+1, ans);
	}
	return 0;
}
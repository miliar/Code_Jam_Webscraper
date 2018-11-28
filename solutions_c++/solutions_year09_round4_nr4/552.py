#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
struct point{int x,y;}a[50];
double r[50];
double check(int i,int j){
	double dis = sqrt(1.0*(a[i].x-a[j].x)*(a[i].x-a[j].x)+(a[i].y-a[j].y)*(a[i].y-a[j].y));
//						printf("%lf %lf %lf => %lf\n",dis,r[i],r[j],(dis+r[i]+r[j]) / 2);
	return (dis+r[i]+r[j]) / 2;
}
int main(){
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
	int t_case,t,n,i;
	double r0,r1,r2;
	scanf("%d",&t_case);
	for (t = 1;t <= t_case;t++){
		scanf("%d",&n);
		for (i = 0;i < n;i++)
			scanf("%d%d%lf",&a[i].x,&a[i].y,&r[i]);
//		printf("%d\n",n);for (i = 0;i < n;i++)printf("%d %d %.f\n",a[i].x,a[i].y,r[i]);
		if (n == 1) r2 = r[0];
		else if (n == 2) r2 = r[0] > r[1]?r[0]:r[1];
		else if (n == 3){
			r0 = check(0,1);
			if (r[2] > r0) r0 = r[2];
			r1 = check(1,2);
			if (r[0] > r1) r1 = r[0];
			r2 = check(2,0);
			if (r[1] > r2) r2 = r[1];
			if (r0 < r2) r2 = r0;
			if (r1 < r2) r2 = r1;
		}
		printf("Case #%d: %.6f\n",t,r2);
	}
	fclose(stdout);
//	while (1);
}

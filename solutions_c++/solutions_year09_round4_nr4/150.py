#include<stdio.h>
#include<string.h>
#include<math.h>
#define eps 1e-6
int n;
double x[42], y[42], r[42];
double dis(double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}
void solve()
{
	double ans;
	double R;
	double tmp;
	
	if( n == 1 ){
		printf("%.6lf\n", r[0]);
		return;
	}
	else if ( n ==2 )
	{
		R = r[0];
		if( R+eps < r[1])R = r[1];
		printf("%.6lf\n", R );
		return;
	}
	
	tmp = dis(x[0],y[0],x[1],y[1]);
	tmp += r[0] + r[1];
	R = tmp/2;
	if(R+eps<r[2])R = r[2];
	ans = R;
	
	tmp = dis(x[0],y[0],x[2],y[2]);
	tmp += r[0] + r[2];
	R = tmp/2;
	if(R+eps<r[1])R = r[1];
	if(ans + eps > R )ans = R;
	
	tmp = dis(x[1],y[1],x[2],y[2]);
	tmp += r[1] + r[2];
	R = tmp/2;
	if(R+eps<r[0])R = r[0];
	if(ans + eps > R )ans = R;
	
	printf("%.6lf\n", ans );
	
}
int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D0.out","w",stdout);
	int tcase;
	scanf("%d",&tcase);
	for(int i =1; i <= tcase; i++){
		scanf("%d",&n);
		for(int j = 0; j < n; j++){
			scanf("%lf%lf%lf", &x[j],&y[j],&r[j]);
		}
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}

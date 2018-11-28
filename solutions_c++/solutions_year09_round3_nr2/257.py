#include<stdio.h>
#include<string.h>
#include<math.h>
#define eps 1e-8
int n;
double dx;
double dy;
double dz;
double spx;
double spy;
double spz;

void solve()
{
		double a0 = dx*dx + dy*dy + dz*dz; 
		double a1 = 2*dx*spx + 2*dy*spy + 2*dz*spz;
		double a2 = spx*spx + spy*spy + spz*spz;
		double kx = a1;
		double ky = 2*a2;
		if(fabs(ky) <= eps){
			double ans1 = sqrt(dx*dx + dz*dz + dy*dy) / n;
			double ans2 = 0;
			printf("%.8lf %.8lf\n",ans1,ans2);
		}
		else
		{
			double t= -kx/ky;
			if(t > 0 )
			{
				double ax = dx + t*spx;
				double ay = dy + t*spy;
				double az = dz + t*spz;
				double ans1 = sqrt(ax*ax + az*az + ay*ay) / n;
				double ans3 = sqrt(dx*dx + dz*dz + dy*dy) / n;
				double ans2 = 0;
				if(ans1 < ans3){
					printf("%.8lf %.8lf\n", ans1,t);
				}else{
				 	printf("%%.8lf %.8lf\n", ans3,ans2);
			  	}
			}else{
				double ans1 = sqrt(dx*dx + dz*dz + dy*dy) / n;
				double ans2 = 0;
				printf("%.8lf %.8lf\n",ans1,ans2);
			}		
		}
}

int main()
{
	int T;
	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
	scanf("%d",&T);
	for(int i = 1; i <= T; i++){
		scanf("%d",&n);
		dx = dy = dz  = 0;
		spx = spy = spz = 0;
		double a1, a2, a3, a4, a5, a6;
			
		for(int j = 0; j < n; j++){
			scanf("%lf %lf %lf %lf %lf %lf", &a1,&a2,&a3,&a4,&a5,&a6);
			dx += a1;
			dy += a2;
			dz += a3;
			spx += a4;
			spy += a5;
			spz += a6;
		}
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}

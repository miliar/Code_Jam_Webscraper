#include<stdio.h>
#include<string.h>
#include<math.h>
#define EPS 1e-10
double x[1000], y[1000], z[1000];
double vx[1000], vy[1000], vz[1000];
int main()
{
	freopen("B-large.in.txt", "r", stdin);
	/*freopen("B-large.out.txt", "w", stdout);*/
	int T;
	scanf("%d", &T);
	for(int kk=1; kk<=T; kk++){
		int n;
		scanf("%d", &n);
		double a=0, b=0, c=0, va=0, vb=0, vc=0;
		for(int i=0; i<n; i++){
			scanf("%lf%lf%lf%lf%lf%lf", &x[i], &y[i], &z[i], 
				&vx[i], &vy[i], &vz[i]);
			a+=x[i], b+=y[i], c+=z[i];
			va+=vx[i], vb+=vy[i], vc+=vz[i];
		}
		a/=n, b/=n, c/=n, va/=n, vb/=n, vc/=n;
		double aa=a*a+b*b+c*c, bb=2*(va*a+vb*b+vc*c), cc=va*va+vb*vb+vc*vc;
		double t;
		if(fabs(cc)<EPS) t=0;
		else t=-bb*0.5/cc;
		if(t<0) t=0;
		double dis;
		if(fabs(cc*t*t+bb*t+aa)<EPS) dis=0;
		else dis=sqrt(cc*t*t+bb*t+aa);
		printf("Case #%d: %.8lf %.8lf\n", kk, dis, t);
	}
	return 0;
}
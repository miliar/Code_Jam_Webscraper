#include <iostream>
#include <cmath>

using namespace std;

double eps=1e-10;

double x[1001],y[1001],z[1001],vx[1001],vy[1001],vz[1001];

int main()
{
	int t,i,j,ooo=1;
	freopen("h://f.in","r",stdin);
	freopen("h://ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int k;
		double x_s=0,y_s=0,z_s=0,x_t=0,y_t=0,z_t=0;
		scanf("%d",&k);
		for(i=0;i<k;i++)
			scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
		for(i=0;i<k;i++)
		{
			x_s+=x[i];y_s+=y[i];z_s+=z[i];
			x_t+=vx[i];y_t+=vy[i];z_t+=vz[i];
		}
		x_s/=k;y_s/=k;z_s/=k;
		x_t/=k;y_t/=k;z_t/=k;
		double erci=0,yici=0,changshu=0;
		erci=x_t*x_t+y_t*y_t+z_t*z_t;
		yici=x_s*x_t+y_s*y_t+z_s*z_t;
		yici*=-1;
		double ans_t;
		if(fabs(erci)<eps)
			ans_t=0;
		else ans_t=yici/erci;
		if(ans_t<-1*eps)
		{
			ans_t=0;
		}
		double ans_d=pow((x_t*ans_t+x_s)*(x_t*ans_t+x_s)+(y_t*ans_t+y_s)*(y_t*ans_t+y_s)+(z_t*ans_t+z_s)*(z_t*ans_t+z_s),0.5);
		printf("Case #%d: %.8lf %.8lf\n",ooo++,ans_d,ans_t);
	}
}

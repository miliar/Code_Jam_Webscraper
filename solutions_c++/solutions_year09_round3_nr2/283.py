#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const int N=510;
double  x[N],y[N],z[N],vx[N],vy[N],vz[N];
int n;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("bbb.out","w",stdout);
	int c,i,p;
	double t,d;
	scanf("%d",&c);
	for(p=1;p<=c;p++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
      double a1=0,b1=0,a2=0,b2=0,a3=0,b3=0;
	  for(i=0;i<n;i++)
	  {
		  a1+=x[i];
		  b1+=vx[i];
		  a2+=y[i];
		  b2+=vy[i];
		  a3+=z[i];
		  b3+=vz[i];
	  }
	  double a=b1*b1+b2*b2+b3*b3,b=2*(a1*b1+a2*b2+a3*b3),cc=a1*a1+a2*a2+a3*a3;
	//  printf("a=%f\n",a);
       if(fabs(a)<1e-6)
	   {
		   t=0;
		   d=sqrt(cc)/n;
	   }
	   else
	   {
	   t=-b/2/a;
	   if(t<0) t=0;
	   d=sqrt(a*t*t+b*t+cc)/n;
	   }
	  printf("Case #%d: %.8f %.8f\n",p,d,t);
	}
	return 0;
}



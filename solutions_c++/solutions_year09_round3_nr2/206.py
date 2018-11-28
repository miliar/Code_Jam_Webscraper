#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
#define N 505
struct points
{
	double x,y,z,vx,vy,vz;
}a[N];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("outb2.txt","w",stdout);
	int i,j,n,test=0,t;
	scanf("%d",&t);
	while(t>0)
	{
		t--;
		test++;
		double x1=0,x2=0,y1=0,z1=0,y2=0,z2=0,sum;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf",&a[i].x,&a[i].y,&a[i].z,&a[i].vx,&a[i].vy,&a[i].vz);
			x1+=a[i].x;x2+=a[i].vx;y1+=a[i].y;y2+=a[i].vy;z1+=a[i].z;z2+=a[i].vz;
		}
		x1/=(double)n;x2/=(double)n;y1/=(double)n;y2/=(double)n;z1/=(double)n;z2/=(double)n;
		printf("Case #%d: ",test);
		sum=(x1*x1+y1*y1+z1*z1);
		if(x2==0&&y2==0&&z2==0)
		{
			sum=sqrt(sum);
			printf("%lf 0.00000000\n",sum);
			continue;
		}
		double b=(x1*x2+y1*y2+z1*z2),a=(x2*x2+y2*y2+z2*z2),c=(x1*x1+y1*y1+z1*z1);
		if(b>0)
		{
			sum=sqrt(sum);
			printf("%lf 0.00000000\n",sum);
		}
		else
		{
			double sum1=(-1.0)*b/a;
			double dis=(x1+x2*sum1)*(x1+x2*sum1)+(y1+y2*sum1)*(y1+y2*sum1) +(z1+z2*sum1)*(z1+z2*sum1) ;              //a*sum1*sum1+2*b*sum1+c;
			dis=sqrt(dis);
			printf("%lf %lf\n",dis,sum1);
		}
	}
    return 0;
}





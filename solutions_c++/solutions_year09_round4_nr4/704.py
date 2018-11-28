#include <iostream>
#include <cmath>


using namespace std;

double x[3],y[3],r[3],eps=1e-9;

int main()
{
	int t;
	int i,j;
	int oo=1;
	freopen("ff.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);double lenth[3];
		for(i=0;i<n;++i)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);

		if(n==1)
		{
			printf("Case #%d: %.6lf\n",oo++,r[0]);continue;
		}
		if(n==2)
		{
			if(r[0]-r[1]<-1*eps)
			printf("Case #%d: %.6lf\n",oo++,r[1]);
			else
				printf("Case #%d: %.6lf\n",oo++,r[0]);
				continue;
		}
		if(n==3)
		{
		lenth[0]=pow((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]),0.5)+r[0]+r[1];
		lenth[0]/=2.0;
		lenth[1]=pow((x[1]-x[2])*(x[1]-x[2])+(y[1]-y[2])*(y[1]-y[2]),0.5)+r[1]+r[2];
		lenth[1]/=2.0;
		lenth[2]=pow((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]),0.5)+r[2]+r[0];
		lenth[2]/=2.0;
		if(lenth[0]-r[2]<-1*eps)
			lenth[0]=r[2];
		if(lenth[1]-r[0]<-1*eps)
			lenth[1]=r[0];
		if(lenth[2]-r[1]<-1*eps)
			lenth[2]=r[1];
		double minn=1000000000.0;
		for(i=0;i<3;++i)
		{
			if(lenth[i]-minn<-1*eps)
				minn=lenth[i];
		}
		printf("Case #%d: %.6lf\n",oo++,minn);
		continue;
		}
	}
}
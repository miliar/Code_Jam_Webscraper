#include <iostream>
#include <cmath>
using namespace std;

typedef struct  
{
	double x,y;
	double R;
}CY;

CY c[20];

double dis(CY a, CY b)
{
	double dx=a.x-b.x;
	double dy=a.y-b.y;
 	return (sqrt(dx*dx+dy*dy)+a.R+b.R)/2;
}

int main()
{
	freopen("DD.in","r",stdin);
	freopen("Ds.txt","w",stdout);
	int T;
	scanf("%d",&T);

	int b=1;

	while (T--)
	{

		int i,n;

		scanf("%d",&n);

		for (i=0;i<n;++i)
		{
			scanf("%lf%lf%lf",&c[i].x,&c[i].y,&c[i].R);
		}

		printf("Case #%d: ",b++);
		if (n==1)
		{
			printf("%lf\n",c[0].R);
		}
		else if (n==2)
		{
			printf("%lf\n",c[0].R>c[1].R?c[0].R:c[1].R);
		}
		else
		{
			double r1=c[0].R;
			double r2=dis(c[1],c[2]);

			double res=r1>r2?r1:r2;


			double tp;
			r1=c[1].R;
			r2=dis(c[0],c[2]);
			tp=r1>r2?r1:r2;

			res=res<tp?res:tp;


			r1=c[2].R;
			r2=dis(c[0],c[1]);
			tp=r1>r2?r1:r2;	
			res=res<tp?res:tp;
			printf("%lf\n",res);
		}

	}
	return 0;
}
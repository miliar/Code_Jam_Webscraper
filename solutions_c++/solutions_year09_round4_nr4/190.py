#include<stdio.h>
#include<math.h>

int n;
double x[50],y[50],r[50];

double dis(int i,int j)
{
	return sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("outB.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	int ca=1;
	for(ca=1;ca<=t;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		if(n==1)
		{
			printf("Case #%d: %lf\n",ca,r[0]);
			continue;
		}
		if(n==2)
		{
			printf("Case #%d: %lf\n",ca,r[0]>r[1]?r[0]:r[1]);
			continue;
		}
		if(n==3)
		{
			double ans=r[0]>dis(1,2)+r[1]+r[2]?r[0]:dis(1,2)+r[1]+r[2];
			double ans2=r[1]>dis(0,2)+r[0]+r[2]?r[1]:dis(0,2)+r[0]+r[2];
			double ans3=r[2]>dis(0,1)+r[0]+r[1]?r[2]:dis(0,1)+r[0]+r[1];
			if(ans>ans2)ans=ans2;if(ans>ans3)ans=ans3;
			printf("Case #%d: %lf\n",ca,ans/2);
		}
	}

	return 0;
}
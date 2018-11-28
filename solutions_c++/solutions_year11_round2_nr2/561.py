#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
double data[5000000];
double data2[5000000];
int ic,id;
double absx(double d)
{
	if(d<0)return -d;
	return d;
}
bool ok(double time)
{
	int n;
	memcpy(data2,data,sizeof(data));
	double togo=-999999999;
	for(n=0;n<ic;n++)
	{
		if(n!=0)
			togo=data2[n-1]+id;
		//printf("%d Shuold go to %lf\n",n,togo);
		if(absx(data2[n]-togo)<=time)
		{
			data2[n]=togo;
		}
		else if(data2[n]<togo)
		{
			//printf("Can't go from %lf to %lf\n",data2[n],togo);
			return false;

		}
		else
			data2[n]-=time;
		//printf("**%lf\n",data2[n]);
	}
	return true;
}
void work()
{
	int in,a,b,n,m;
	scanf("%d %d",&in,&id);
	ic=0;
	for(n=0;n<in;n++)
	{
		scanf("%d %d",&a,&b);
		for(m=0;m<b;m++)
			data[ic++]=a;
	}
	sort(data,data+ic);
	double s=0,e=(double)999999999;
	double ans=0;
	bool isset=0;
	while(e-s>=0.000000001)
	{
		double m=(s+e)/2;
		//printf("%lf %lf %lf %lf\n",s,e,m,ans);
		if(ok(m))
		{
			//printf("OK\n");
			if(!isset||m<ans)
			{
				ans=m;
				isset=true;
			}
			e=m;
		}
		else
			s=m;
	}
	printf("%.10lf\n",ans);
}
int main()
{
	int n,ix;
	scanf("%d",&ix);
	for(n=0;n<ix;n++)
	{
		printf("Case #%d: ",n+1);
		work();
	}
}

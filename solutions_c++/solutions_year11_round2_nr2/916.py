#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define F first
#define S second
#define MAX 1024
using namespace std;

int C;
double D;
double P[MAX];
int V[MAX];

bool ok(double time)
{
	double prev=-1e9;

	for(int i=0;i<C;i++)
	{
		for(int j=0;j<V[i];j++)
		{
			if(fabs(P[i]+time-prev)<D) return false;
			if(prev+D<P[i])
			{
				if(P[i]-time>prev+D)
					prev=P[i]-time;
				else
					prev+=D;
			}
			else prev+=D;
			/*
			
			if(fabs(prev-P[i])<D) // try to adjust
			{
				if(fabs(prev+D-P[i])>time) return false;
				prev+=D;
			}
			else prev=max(P[i]-time,prev+D);*/
		}
	}
	return true;
}

int main()
{
	int cases;
	
	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		scanf("%d %lf",&C,&D);

		for(int i=0;i<C;i++)
			scanf("%lf %d",&P[i],&V[i]);

		double low=0.0,high=1e9;
		for(int it=0;it<1000;it++)
		{
			double mid=(low+high)/2.0;			
			// now see if its possible to do it in time mid
			if(ok(mid)) high=mid;
			else low=mid;
		}
		printf("Case #%d: ",iD);
		printf("%.12lf\n",low);

	}

	return 0;
}


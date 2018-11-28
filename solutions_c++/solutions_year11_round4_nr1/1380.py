#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
struct cc
{
	int b,e,w;
}cd[1100];
bool cmp(cc a,cc b)
{
	return a.w<b.w;
}
int main()
{
	int t,s,r,x,i,tt,n,k;
	double ft;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&tt,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&cd[i].b,&cd[i].e,&cd[i].w);
			x-=(cd[i].e-cd[i].b);
		}
		ft=tt;
		double ans=0;
		sort(cd,cd+n,cmp);
		bool flag=true;
		double ct=((double)x)/r;
		if(ct<=ft)
		{
			ans+=ct;
			ft-=ct;
		}	
		else
		{
			flag=false;
			double rem=x-r*ft;
			ans+=(ft+rem/s);
			ft=0;
		}
		//printf("%lf %lf ",ans,ft);
		for(i=0;i<n;i++)
		{
			if(flag)
			{
				double ct=((double)(cd[i].e-cd[i].b))/(cd[i].w+r);
				if(ct<=ft)
				{
					ft-=ct;
					ans+=ct;
				}
				else
				{
					flag=false;
					double rem=(cd[i].e-cd[i].b-ft*(cd[i].w+r));
					ans+=(ft+rem/(cd[i].w+s));
					ft=0;
				}
			}
			else
				ans+=((double)(cd[i].e-cd[i].b))/(cd[i].w+s);
		//	printf("%lf ",ans);
		}
		printf("Case #%d: %.10f\n",k,ans);	
	}
	return 0;
}

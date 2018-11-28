#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<stdlib.h>
#include<vector>
#include<math.h>
using namespace std;
double ar[2010][2];
int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("ans.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		double l;
		int n,q;
		scanf("%lf%d%d",&l,&n,&q);
		for(int i=0;i<n;i++)
			scanf("%lf%lf",&ar[i][0],&ar[i][1]);
		printf("Case #%d:\n",k);
		for(int i=0;i<n;i++)
		{
			if(ar[i][1]>l)
			{
				if(i==0)
					ar[i][1]=l;
				else
				{
					double v=(ar[i][1]-ar[i-1][1])/(ar[i][0]-ar[i-1][0]);
					ar[i][0]=(l-ar[i-1][1])/v;
					ar[i][1]=l;
				}
				n=i+1;
				break;
			}
		}
		for(int i=0;i<q;i++)
		{
			double a;
			scanf("%lf",&a);
			double st=0;
			for(int i=0;i<n;i++)
			{
				double t1=sqrt(2*ar[i][1]/a);
				st=max(st,ar[i][0]-t1);
				/*
				double ti;
				if(i==0)
				{
					ti=sqrt(2.0*ar[i][1]/a+v*v/a/a)-v/a;
					if(ti>ar[i][0])
					{
						v+=a*ti;
						ans+=ti;
					}
					else
					{
						if(ar[i][0]==0)
							v=0;
						else
						{
							double t1=sqrt(max(2*(ar[i][1]-ar[i][0]*v)/a,0.0));
							if(ar[i][1]-ar[i][0]*v>=0)
							v+=a*t1;
						}
						ans+=ar[i][0];
					}
				}
				else
				{
					ti=sqrt(2.0*(ar[i][1]-ar[i-1][1])/a+v*v/a/a)-v/a;
					if(ans+ti>ar[i][0])
					{
						v+=a*ti;
						ans+=ti;
					}
					else
					{
						double t1=sqrt(max(2*(ar[i][1]-ar[i-1][1]-v*(ar[i][0]-ans))/a,0.0));
						v+=(ar[i][1]-ar[i-1][1])/(ar[i][0]-ar[i-1][0]);
						ans=ar[i][0];
					}
				}*/
			}
			printf("%.10lf\n",st+sqrt(2*l/a));
		}
	}
}
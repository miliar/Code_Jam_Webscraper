#include <stdafx.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

const double eps=1.0e-9;
const double eps2=1.0e-15;
const long maxn=1000005;

long n,test,t,d,cht,q,need,p,am;
long mas[maxn];
double now[maxn];

double abss(double x)
{
	if (x<0)
		return(-x);
	else return(x);
}

bool pos(double time)
{
	now[1]=mas[1]-time;
	bool fail=false;
	for (long i=2;i<=cht;i++)
	{
		//if (time-(d-mas[i]+mas[i-1])>=-eps2)
		//	now[i]=now[i-1]+d;
		//else now[i]=mas[i];
		/*now[i]=max(min(now[i-1]+d,mas[i]+time),mas[i]-time);
		if (d-(now[i]-now[i-1])>eps2)
		{
			fail=true;
			break;
		}*/
		/*if (time-abss(now[i-1]+d-mas[i])>eps)
			now[i]=now[i-1]+d;
		else
		{
			now[i]=max(mas[i]-time,now[i-1]+d);
			if (d-now[i]+now[i-1]>eps)
			{
				fail=true;
				break;
			}
		}*/
		if (mas[i]-now[i-1]+d>eps)
		{
			now[i]=max(now[i-1]+d,mas[i]-time);
		}
		else
		{
			now[i]=min(now[i-1]+d,mas[i]+time);
		}

		if (d-abss(now[i]-now[i-1])>eps)
		{
			fail=true;
			break;
		}
	}

	if (fail==true)
		return(false);
	return(time-abss(now[cht]-mas[cht])>=-eps);
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	scanf("%ld",&t);
	for (test=1;test<=t;test++)
	{
		scanf("%ld%ld",&n,&d);

		cht=0;
		for (q=1;q<=n;q++)
		{
			scanf("%ld%ld",&p,&am);
			for (long j=1;j<=am;j++)
			{
				cht++;
				mas[cht]=p;
			}
		}

		double limit=0.0;
		for (q=2;q<=n;q++)
			if (mas[q]-mas[q-1]<d)
				limit=max(limit,double(d-mas[q]+mas[q-1])/2);

		sort(mas+1,mas+cht+1);

		double start=limit;
		double finish=1000000000.0;
		pos(1);
		while(finish-start>eps)
		{
			double middle=(start+finish)/2;
			bool temp=pos(middle);
			if (temp==true)
				finish=middle;
			else start=middle;
		}

		//double d1=d;
		//start=max(start,d1);

		printf("Case #%ld: %0.8lf\n",test,start);
		/*(printf("%ld\n",d);
		for (q=1;q<=cht;q++)
		{
			printf("%0.9lf ",now[q]);
			if (abss(now[q]-mas[q])-start>eps3)
			{
				printf("\n!!!!!!!!!!\n");
			}
		}
		printf("\n");*/
	}
}
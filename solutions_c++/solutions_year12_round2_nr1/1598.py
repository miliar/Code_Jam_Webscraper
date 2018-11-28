#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<set>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<iostream>
#define PINF 2000000000
#define NINF -2000000000
using namespace std;
int n,m,t,chk[1005];
double a[1005],ans[1005];
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		double sum=0,sum2;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			chk[i]=0;
			scanf("%lf",&a[i]);
			sum+=a[i];
		}
		double temp = (sum*2)/n;
		int cnt=0;
		//printf("%lf %lf\n",sum,temp);
		sum2=sum;
		for(int i=0;i<n;i++)
		{
			if(temp<a[i])
			{
				ans[i]=0;
				chk[i]=1;
				sum2-=a[i];
				cnt++;
			}
		}
		temp = (sum+sum2)/(n-cnt);
		//printf("%lf %lf\n",sum,temp);
		for(int i=0;i<n;i++)
		{
			if(chk[i]==0)
				ans[i]=(((temp-a[i])*100)/sum);
		}
		printf("Case #%d:",c);
		for(int i=0;i<n;i++)
			printf(" %lf",ans[i]);
		printf("\n");
	}
    scanf(" ");
}

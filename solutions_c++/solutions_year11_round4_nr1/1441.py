#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
#define MAXN 1005
struct Node
{
	double st,ed,v;
}way[MAXN];
int cmp(Node a,Node b)
{
	return a.v<b.v;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int ct,i;
	double x,s,r,t,sum,ans,temp;
	int n;
	int tt=0;
	scanf("%d",&ct);
	while(ct--)
	{
		if(tt==30)
			tt=30;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&way[i].st,&way[i].ed,&way[i].v);
			sum+=(way[i].ed-way[i].st);
		}
		ans=0;
		sum=x-sum;
		sort(way,way+n,cmp);
		if(sum/r>=t)
		{
			ans+=t;
			ans+=(sum-r*t)/s;
			for(i=0;i<n;i++)
			{
				ans+=(way[i].ed-way[i].st)/(s+way[i].v);
			}
			printf("Case #%d: %.6lf\n",++tt,ans);
			continue;
		}
		ans+=sum/r;
		t-=ans;
		for(i=0;i<n;i++)
		{
			temp=(way[i].ed-way[i].st)/(r+way[i].v);
			if(temp<=t)
			{
				ans+=temp;
				t-=temp;
			}else
			{
				ans+=t;
				ans+=(way[i].ed-way[i].st-(r+way[i].v)*t)/(s+way[i].v);
				t=0;
			}
		}
		printf("Case #%d: %.6lf\n",++tt,ans);
	}
	return 0;
}
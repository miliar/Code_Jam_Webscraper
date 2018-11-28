#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int a[2021];
int next[2021],value[2021],cost[2021],was[2021];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int r,k,n;
	int i,j,cur;
	int sum;
	__int64 ans;
	scanf("%d",&t);
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d%d%d",&r,&k,&n);
		for (i=0; i<n; ++i)
		{
			scanf("%d",&a[i]);
			a[n+i]=a[i];
		}
		printf("Case #%d: ",tt+1);
		for (i=0; i<n; ++i)
		{
			j=i;
			sum=a[i];
			while (sum<=k && j<i+n)
			{
				j++;
				sum+=a[j];
			}
			next[i]=j%n;
			value[i]=sum-a[j];
		}
	/*	for (i=0; i<n; ++i)
			printf("%d ",value[i]);
		printf("\n");
		for (i=0; i<n; ++i)
			printf("%d ",next[i]);
	*/	ans=0;
		memset(was,0xFF,sizeof(was));
		for (i=0,cur=0; was[cur]==-1 && i<r; ++i)
		{
	//		printf("%d: cur = %d\n",i,cur);
			was[cur]=i;
			cost[cur]=ans;
			ans+=value[cur];
			cur=next[cur];  
		}
	//	printf("%d ",ans);
		if (i==r)
		{
			printf("%d\n",ans);
			continue;
		}
		r-=i;
		ans+=r/(i-was[cur])*(ans-cost[cur]);
		r%=(i-was[cur]);
		for (i=0; i<r; ++i)
		{
			ans+=value[cur];
			cur=next[cur];  
		}
		printf("%d\n",ans);
	}
	return 0;
}
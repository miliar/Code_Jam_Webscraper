#include <iostream>
#include <stdio.h>
using namespace std;
int r,k,n;
int gs[130];
int all[300];
int b_find(int s)
{
	if (n == 1)
		return 1;
	int num;
	int l = 1;
	int h = n;
	while (l <= h)
	{
		int mid = (l+h)>>1;
		num = all[s+mid-1]-all[s-1];
		if (num <= k)
			l = mid + 1;
		else
			h = mid - 1;
	}
	return l-1;
}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("pro.out","w",stdout);
	int t;
	
	int i,j;
	scanf("%d",&t);
	for (i = 1;i <= t;i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for (j = 1;j <= n;j++)
			scanf("%d",&gs[j]);
		all[0] = 0;
		gs[0] = 0;
		for (j = 1;j <= n;j++)
			all[j] = all[j-1]+gs[j];
		for (j = n+1;j <= 2*n;j++)
			all[j] =all[j-1]+gs[j-n];
	
		int now;
		int cnt;
		int num;
		cnt = 0;
		now = 1;
		for (j = 1;j <= r;j++)
		{
			num = b_find(now);
			cnt += all[now+num-1]-all[now-1];
			now = (now+num-1)%n+1;
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}
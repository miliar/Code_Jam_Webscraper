#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;
int es[15];
int times[2000];
int ans;
int price[15][2000];
void calc(int l,int r)
{
	int i,j;
	int flag = 0;
	for (i = l;i <= r;i++)
	{
		if (times[i] > 0)
		{
			flag = 1;
			break;
		}
	}
	if (flag == 1)
	{
		++ans;
		for (i = l;i <= r;i++)
			times[i]--;
		int mid = (l+r)>>1;
		calc(l,mid);
		calc(mid+1,r);
		return;
	}
	else
		return;
}
int main()
{
	int i;
	es[0] = 1;
	for (i = 1;i <= 15;i++)
		es[i] = es[i-1]*2;
	int t;
	int j,k;
	int p;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for (i = 1;i <= t;i++)
	{
		ans = 0;
		scanf("%d",&p);
		for (j = 0;j < es[p];j++)
		{
			scanf("%d",&times[j]);
			times[j] = p-times[j];
		}
		for (j = p-1;j >= 0;j--)
		{
			for (k = 0;k < es[j];k++)
				scanf("%d",&price[p-j][k]);
		}
		calc(0,es[p]-1);
		printf("Case #%d: %d\n",i,ans);
	}
}
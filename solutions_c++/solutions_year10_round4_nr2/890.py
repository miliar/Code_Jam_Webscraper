// #include <iostream>
// using namespace std;
// struct Node
// {
// 	int p,e;
// 	int used;
// 	Node()
// 	{
// 		used=0;
// 	}
// };
// Node node[10000];
// int m[2048];
// void construct(int p,int first,int second)
// {
// 	node[p].p=first;
// 	node[p].e=second;
// 	if (second==first+1)
// 	{
// 		return;
// 	}
// 	int mid=(first+second)/2;
// 	construct(p*2,first,mid);
// 	construct(p*2+1,mid+1,second);
// }
// void add(int p)
// {
// 	if (node[p].p+1>=node[p].e)
// 	{
// 		m[node[p].p]++;
// 		m[node[p].e]++;
// 		return;		
// 	}
// 	else 
// 	{
// 		add(p*2);
// 		add(p*2+1);
// 	}
// }
// void adding(int p,int num)
// {
// 	while (node[p].used!=0)
// 	{
// 		int mid=(node[p].p+node[p].e)/2;
// 		if (num<=mid)
// 		{
// 			p=p*2;
// 		}
// 		else 
// 		{
// 			p=p*2+1;
// 		}
// 	}
// 	node[p].used++;
// 	add(p);
// }
// 
// int main()
// {
// 	freopen("B-small-attempt0.in","r",stdin);
// 	freopen("B-small-attempt0.in","w",stdout);
// 	int t,i,j,k;
// 	int p,q;
// 	int price[2048];
// 	scanf("%d",&t);
// 	for (i=1;i<=t;i++)
// 	{
// 
// 		scanf("%d",&p);
// 		q=(1<<p);
// 		construct(1,1,q);
// 		for (j=0;j<q;j++)
// 		{
// 			scanf("%d",&m[j]);
// 		}
// 		for (j=0;j<q-1;j++)
// 		{
// 			scanf("%d",&price[j]);
// 		}
// 		int ans=0;
// 		for (j=0;j<q;j++)
// 		{
// 			int z=p-m[j];
// 			for (k=1;k<=z;k++)
// 			{
// 				adding(1,j);
// 				ans++;
// 			}
// 		}
// 		printf("Case #%d: %d\n",i,ans);
// 	}
// 	return 0;
// }
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
int ess[15];
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
	ess[0] = 1;
	for (i = 1;i <= 15;i++)
		ess[i] = ess[i-1]*2;
	int t;
	int j,k;
	int p;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (i = 1;i <= t;i++)
	{
		ans = 0;
		scanf("%d",&p);
		for (j = 0;j < ess[p];j++)
		{
			scanf("%d",&times[j]);
			times[j] = p-times[j];
		}
		for (j = p-1;j >= 0;j--)
		{
			for (k = 0;k < ess[j];k++)
				scanf("%d",&price[p-j][k]);
		}
		calc(0,ess[p]-1);
		printf("Case #%d: %d\n",i,ans);
	}
}
#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;
#define nNode 105
struct node
{
	int robot;
	int pi;
};
node ans[nNode];
int last[2];
int sum[2];
int onelast[2];
int Abs(int x)
{
	if(x<0) x=-x;
	return x;
}
void slove(int n)
{
	int i;
	last[0]=1;
	last[1]=1;
	sum[0]=0;
	sum[1]=0;
	onelast[0]=0;
	onelast[1]=0;
	int qian,now;
	now=ans[1].robot;
	onelast[now]=ans[1].pi;
	qian=now;
	last[now]=ans[1].pi;
	for(i=2;i<=n;i++)
	{
		now=ans[i].robot;
		if(now==qian)
		{
			onelast[now]+=(Abs(ans[i].pi-last[now])+1);
			last[now]=ans[i].pi;
			continue;
		}
		else
		{
			sum[qian]+=onelast[qian];
			onelast[now]=(Abs(ans[i].pi-last[now])+1);
			last[now]=ans[i].pi;
			if(onelast[now]<onelast[qian]+1) onelast[now]=onelast[qian]+1;
			onelast[now]=onelast[now]-onelast[qian];
			sum[now]+=onelast[qian];
			onelast[qian]=0;
			qian=now;
		}
	}
	sum[qian]+=onelast[qian];
	if(sum[0]<sum[1]) sum[0]=sum[1];
	printf("%d\n",sum[0]);
}
int main()
{
	int T,n,i,Case=1;
	char c;
	//freopen("A-large.in","r",stdin);
	//freopen("ans.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf(" %c %d",&c,&ans[i].pi);
			if(c=='O') ans[i].robot=0;
			if(c=='B') ans[i].robot=1;
		}
		printf("Case #%d: ",Case++);
		slove(n);
	}
	return 0;
}
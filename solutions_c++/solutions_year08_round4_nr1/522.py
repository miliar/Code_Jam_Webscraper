#include "stdio.h"
int n,m,g[10005],c[10005],x[10005],z[10005],yi[10005],er[10005];
int calc(int gate,int a,int b)
{
	if(gate==1)
		return a&b;
	else
		return a|b;
}
void search1(int now)
{
	if(z[now]==1)
		return;
	search1(2*now);
	search1(2*now+1);
	x[now]=calc(g[now],x[2*now],x[2*now+1]);
}
void search(int now,int gate,int r)
{
	if(gate==1)
	{
		if(yi[now*2]+yi[now*2+1]+r<yi[now])
			yi[now]=yi[now*2]+yi[now*2+1]+r;
		if(yi[now*2]+er[now*2+1]+r<er[now])
			er[now]=yi[now*2]+r+er[now*2+1];
		if(er[now*2]+yi[now*2+1]+r<er[now])
			er[now]=er[now*2]+yi[now*2+1]+r;
		if(er[now*2]+er[now*2+1]+r<er[now])
			er[now]=er[now*2]+er[now*2+1]+r;
	}
	else
	{
		if(yi[now*2]+yi[now*2+1]+r<yi[now])
			yi[now]=yi[now*2]+yi[now*2+1]+r;
		if(yi[now*2]+er[now*2+1]+r<yi[now])
			yi[now]=yi[now*2]+er[now*2+1]+r;
		if(er[now*2]+yi[now*2+1]+r<yi[now])
			yi[now]=er[now*2]+yi[now*2+1]+r;
		if(er[now*2]+er[now*2+1]+r<er[now])
			er[now]=er[now*2]+er[now*2+1]+r;
	}
}
int main()
{
	int kase,tot,i;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n/2;i++)
		{
			scanf("%d%d",&g[i],&c[i]);
			z[i]=0;
		}
		for(;i<=n;i++)
		{
			scanf("%d",&x[i]);
			z[i]=1;
		}
		search1(1);
		for(i=n;i>n/2;i--)
		{
			yi[i]=er[i]=10000000;
			if(x[i]==1)
				yi[i]=0;
			else
				er[i]=0;
		}
		for(i=n/2;i>=1;i--)
		{
			yi[i]=10000000;
			er[i]=10000000;
			if(g[i]==1)
			{
				search(i,1,0);
				if(c[i]==1)
					search(i,0,1);
			}
			else if(g[i]==0)
			{
				search(i,0,0);
				if(c[i]==1)
					search(i,1,1);
			}
		}
		if(m==1)
			i=yi[1];
		else
			i=er[1];
		printf("Case #%d: ",kase);
		if(i==10000000)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",i);
	}
	return 0;
}
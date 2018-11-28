#include<stdio.h>
int m,now[20],a[1500],ans;
int add(int x,int y)
{
	return x^y;
}
void dfs(int depth)
{
	int i,t1=0,t2=0,t=0,tmp=0;
	if(depth==m)
	{
		for(i=0,tmp=0;i<m;i++)
			if(now[i]==1)
			{
				tmp++;
				t1=add(t1,a[i]);
			}
		if(tmp==m)return;
		for(i=0;i<m;i++)
			if(now[i]==0)
				t2=add(t2,a[i]);
		if(t1==t2)
		{
			for(i=0;i<m;i++)
				if(now[i]==1)
					t+=a[i];
			if(t>ans)ans=t;
		}
		return;
	}
	now[depth]=1;
	dfs(depth+1);
	now[depth]=0;
	dfs(depth+1);
}
main()
{
	int i,j,abc,ab;
	freopen("c.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&abc);
	for(ab=0;ab<abc;ab++)
	{
		ans=-1;
		scanf("%d",&m);
		for(i=0;i<m;i++)
			scanf("%d",&a[i]);
		dfs(0);
		if(ans==-1)
			printf("Case #%d: NO\n",ab+1);
		else
			printf("Case #%d: %d\n",ab+1,ans);
	}
}

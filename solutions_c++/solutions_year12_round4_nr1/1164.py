#include <stdio.h>
#define N 10001
int di[N],ii[N];
int nv,dd;
bool flag;
bool dfs(int p,int q)
{
	if(q<0)return 0;
	if(p==0)return 1;
	for(int i=0;di[i]<=q;i++)
		if(ii[i]>=di[p]-di[i])
		{
			bool t=dfs(i,di[i]-di[p]+di[i]);
			if(t)return 1;
		}
	return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		flag=0;
		scanf("%d",&nv);
		for(i=0;i<nv;i++)
			scanf("%d%d",di+i,ii+i);
		scanf("%d",&dd);
		for(i=nv-1;i>=0&&!flag;i--)
			if(dd-di[i]<=ii[i])
				flag+=dfs(i,di[i]-dd+di[i]);
		if(flag)printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}
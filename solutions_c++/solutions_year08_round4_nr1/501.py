#include<cstdio>
const int mn=10005;
int n,v,T,a[mn],c[mn],f[mn][2],inn;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%d",&n,&v);
		inn=(n-1)/2;
		for(int i=1;i<=inn;i++)
			scanf("%d%d",a+i,c+i),f[i][0]=f[i][1]=mn;
		for(int i=inn+1;i<=n;i++)
			scanf("%d",a+i),f[i][a[i]]=0,f[i][!a[i]]=mn;

		for(int i=inn;i>=1;i--)
		{
			int lc=i*2,rc=i*2+1;
			if(a[i])
			{
				f[i][0]<?=f[lc][0]+f[rc][0];
				f[i][0]<?=f[lc][1]+f[rc][0];
				f[i][0]<?=f[lc][0]+f[rc][1];
				f[i][1]<?=f[lc][1]+f[rc][1];
				if(c[i])
				{
					f[i][1]<?=f[lc][0]+f[rc][1]+1;
					f[i][1]<?=f[lc][1]+f[rc][0]+1;
				}
			}
			else
			{
				f[i][0]<?=f[lc][0]+f[rc][0];
				f[i][1]<?=f[lc][0]+f[rc][1];
				f[i][1]<?=f[lc][1]+f[rc][0];
				f[i][1]<?=f[lc][1]+f[rc][1];
				if(c[i])
				{
					f[i][0]<?=f[lc][0]+f[rc][1]+1;
					f[i][0]<?=f[lc][1]+f[rc][0]+1;
				}
			}
		}
		printf("Case #%d: ",tn);
		if(f[1][v]<mn)printf("%d\n",f[1][v]);
		else puts("IMPOSSIBLE");
	}
	return 0;
}

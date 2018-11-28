#include <cstdio>
#include <cstring>
int i,j,k,s,t,n,m;
int a[2005][2005];
int b[2005];
int c[2005];
int d[2005];
int ans[2005];
int T,I;
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		scanf("%d%d",&n,&m);
		memset(c,0,sizeof c);
		for (i=1;i<=m;++i)
		{
			scanf("%d",&k);
			b[i]=0;
			for (j=1;j<=k;++j)
			{
				scanf("%d%d",&s,&t);
				if (t==0) a[i][++b[i]]=s;
				else c[i]=s;
			}
			d[i]=b[i];
		}
		memset(ans,0,sizeof ans);
		bool f=1;
		while (f)
		{
			f=0;
			for (i=1;i<=m;++i)
			{
				if (d[i]==0 && c[i]!=0 && ans[c[i]]==0)
				{
					ans[c[i]]=1;
					f=1;
				}
			}
			for (i=1;i<=m;++i)
				if (c[i]!=0 && ans[c[i]]==1)
					d[i]=0;
			for (i=1;i<=m;++i)
			for (j=1;j<=b[i];++j)
			if (a[i][j]!=0 && ans[a[i][j]]==1){
				--d[i];
				a[i][j]=-a[i][j];
			}
		}
		bool pan=1;
		for (i=1;i<=m;++i)
		if (c[i]==0)
		{
			bool f=0;
			for (j=1;j<=b[i];++j)
			{
				if (a[i][j]>=0) f=1;
			}
			if (!f) {pan=0;break;}
		}
		printf("Case #%d: ",I);
		if (pan)
		{
			for (i=1;i<n;++i)
				printf("%d ",ans[i]);
			printf("%d\n",ans[n]);
		}
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
			
				
					


#include <cstdio>
#include <cstring>
int i,j,k,s,t,n,m;

int a[200][200];
int I;
int opt[20][3000];
int T,ans;
char st[20];
main()
{
	scanf("%d",&T);
	while (T--)
	{
		ans=0;
		scanf("%d%d\n",&n,&m);
		for (i=0;i<n;++i)
		{
			gets(st);
			for (j=0;j<m;++j)
				if (st[j]=='.') a[i][j]=0;
				else a[i][j]=1;
		}
		memset(opt,0,sizeof opt);
		for (i=0;i<(1<<m);++i)
		{
			bool f=1;
			for (j=0;j<m;++j)
			{
				if (a[0][j]==1 && (i&(1<<j))>0){
					f=0;
					break;
				}
				if (j>0 && (i&(1<<j))>0 && (i&(1<<j-1))>0)
				{
					f=0;
					break;
				}
			}
			if (f){
				opt[0][i]=0;
				for (j=0;j<m;++j)
					if ( (i&(1<<j))>0) ++opt[0][i];
				if (opt[0][i]>ans) ans=opt[0][i];
				//printf("%d %d\n",i,opt[0][i]);
			}
			
		}
		for (i=1;i<n;++i)
		for (j=0;j<(1<<m);++j)
		for (k=0;k<(1<<m);++k)
		{
			bool f=1;
			for (t=0;t<m;++t)
			{
				if (t>0 && (k&(1<<t))>0 && ( (k&(1<<t-1))>0 || (j&(1<<t-1))>0))
				{
					f=0;
					break;
				}
				if (t<m-1 && (k&(1<<t))>0 && (j&(1<<t+1))>0)
				{
					f=0;
					break;
				}
				if (a[i][t]==1 && (k&(1<<t))>0){
					f=0;
					break;
				}
			}
			s=0;
			for (t=0;t<m;++t)
				if ((k&(1<<t))>0)++s;
			if (f && opt[i-1][j]+s>opt[i][k]) opt[i][k]=opt[i-1][j]+s;
			//printf("%d %d %d %d\n",j,k,opt[i-1][j],opt[i][k]);
			if (opt[i][k]>ans) ans=opt[i][k];
		}
		printf("Case #%d: %d\n",++I,ans);
	}
	return 0;
}

					

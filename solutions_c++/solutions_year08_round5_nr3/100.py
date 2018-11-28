#include<stdio.h>
#include<memory>
int z[10][1<<10];
int g[1<<10];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int c,o,n,m,i,j,s,t,v[10];
	int ans;
	char str[16];
	g[0]=0;
	for(i=1;i<(1<<10);i++)
		g[i]=g[i>>1]+(i&1);
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",str);
			v[i]=0;
			for(j=0;j<m;j++)
				if(str[j]=='x')
					v[i]|=1<<j;
		}
		memset(z,0,sizeof(z));
		for(i=0;i<n;i++)
			for(s=0;s<(1<<m);s++)
				if(!(s&v[i])&&!(s&(s<<1))&&!(s&(s>>1)))
					if(!i)
					{
						if(g[s]>z[i][s])
							z[i][s]=g[s];
					}
					else
						for(t=0;t<(1<<m);t++)
							if(!(t&(t<<1))&&!(t&(t>>1)))
								if(!(s&(t<<1))&&!(s&(t>>1)))
									if(z[i-1][t]+g[s]>z[i][s])
										z[i][s]=z[i-1][t]+g[s];
		ans=0;
		for(s=0;s<(1<<m);s++)
			if(z[n-1][s]>ans)
				ans=z[n-1][s];
		printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}


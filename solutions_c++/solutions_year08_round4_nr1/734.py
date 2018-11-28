#include<cstdio>
#include<cstring>
int t,k,i,j,n,a[10001][2],c[10001],g[10001],v;
void And(int k,int c)
{
	int i,j,x;
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
			if(a[2*k][i]!=-1 && a[2*k+1][j]!=-1)
			{
				x=i&&j;
				if(a[k][x]==-1 || a[k][x]>a[2*k][i]+a[2*k+1][j]+c)
					a[k][x]=a[2*k][i]+a[2*k+1][j]+c;
			}
}
void Or(int k,int c)
{
	int i,j,x;
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
			if(a[2*k][i]!=-1 && a[2*k+1][j]!=-1)
			{
				x=i||j;
				if(a[k][x]==-1 || a[k][x]>a[2*k][i]+a[2*k+1][j]+c)
					a[k][x]=a[2*k][i]+a[2*k+1][j]+c;
			}
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d ",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d %d",&n,&v);
		memset(a,-1,sizeof(a));
		for(i=1;i<=(n-1)/2;i++)
			scanf("%d %d",&g[i],&c[i]);
		for(i=(n-1)/2+1;i<=n;i++)
		{
			scanf("%d",&j);
			a[i][j]=0;
		}
		for(i=(n-1)/2;i>0;i--)
			if(g[i]==1)
			{
				And(i,0);
				if(c[i]) Or(i,1);
			}
			else
			{
				Or(i,0);
				if(c[i]) And(i,1);
			}		
		printf("Case #%d: ",k);
		if(a[1][v]!=-1)
			printf("%d\n",a[1][v]);
		else
			printf("IMPOSSIBLE\n");
	}
	fclose(stdout);
	return 0;
}
#include<cstdio>
#include<cstring>
int d[101][101],c[101][101],ct,n,m;
bool check(int a,int b)
{
	if(a>=1&&a<=n&&b>=1&&b<=m)return true;
	return false;
}
int dfs(int i,int j)
{
	if(c[i][j])return c[i][j];
	int a=d[i][j],b1,b2;
	if(check(i-1,j)&&a>d[i-1][j]){a=d[i-1][j],b1=i-1;b2=j;}
	if(check(i,j-1)&&a>d[i][j-1]){a=d[i][j-1],b1=i;b2=j-1;}
	if(check(i,j+1)&&a>d[i][j+1]){a=d[i][j+1],b1=i;b2=j+1;}
	if(check(i+1,j)&&a>d[i+1][j]){a=d[i+1][j],b1=i+1;b2=j;}
	if(a==d[i][j])return c[i][j]=ct++;
	return c[i][j]=dfs(b1,b2);
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tt,t,i,j;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		ct=1;
		memset(c,0,sizeof(c));
		printf("Case #%d:\n",tt);
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&d[i][j]);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(c[i][j]==0)
				{
					dfs(i,j);
				}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<m;j++)
				printf("%c ",(char)(c[i][j]+'a'-1));
			printf("%c\n",(char)(c[i][j]+'a'-1));
		}
	}
	return 0;
}

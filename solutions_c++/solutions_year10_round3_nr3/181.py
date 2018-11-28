#include<iostream>
#include<algorithm>
char s[512][513];
int d[512][512];
int g[513];
bool check(int y,int x,int yy,int xx)
{
	int i,j;
	for(i=y;i<=yy;i++)
		for(j=x;j<xx;j++)
			if(d[i][j]==d[i][j+1]&&d[i][j+1]==-1&&d[i][j]==-1)return false;
	for(i=y;i<yy;i++)
		for(j=x;j<=xx;j++)
			if(d[i][j]==d[i+1][j]&&d[i+1][j]==-1&&d[i][j]==-1)return false;
	return true;
}
void mk(int y,int x,int yy,int xx)
{
	int i,j;
	for(i=y;i<=yy;i++)
		for(j=x;j<=xx;j++)
			d[i][j]=-1;
}
int main()
{
	int T,cs,i,j,n,k,b,t,ct,ans,bt,sum,tot,m,sz;
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		scanf("%d%d",&n,&m);
		memset(g,0,sizeof(g));
		for(i=0;i<n;i++)
		{
			scanf("%s",s[i]);
			for(j=0;j*4<m;j++)
			{
				t=s[i][j]-'0';
				d[i][j*4+3]=(t&1);
				d[i][j*4+2]=((t&2)!=0);
				d[i][j*4+1]=((t&4)!=0);
				d[i][j*4+0]=((t&8)!=0);
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				printf("%d",d[i][j]);
			printf("\n");
		}
		sz=n;
		if(sz>m)sz=m;
		for(sum=tot=0;sz>1;sz--)
		{
			for(i=0;i<=n;i++)
			{
				if(i+sz-1==n)break;
				for(j=0;j<m;j++)
				{
					if(j+sz-1==m)break;
					if(check(i,j,i+sz-1,j+sz-1))
					{
						mk(i,j,i+sz-1,j+sz-1);
						g[sz]++;
						if(g[sz]==1)tot++;
						sum+=sz*sz;
					}
				}
			}
		}
		g[1]=n*m-sum;
		if(g[1]!=0)tot++;
		printf("Case #%d: %d\n",cs,tot);
		for(i=n;i>=1;i--)
			if(g[i]!=0)printf("%d %d\n",i,g[i]);
	}
	return 0;
}

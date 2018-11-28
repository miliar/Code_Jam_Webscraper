#include<iostream>
using namespace std;
int cn,ci,m,n,i,j,x,y,cur,f1,f2;
int a[110][110];
char b[110][110];
int f[12000];
int c[12000];

int fa(int x)
{
	if (f[x]<0) return x;
	f[x]=fa(f[x]);
	return f[x];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cn);
	for (ci=1;ci<=cn;ci++)
	{
		scanf("%d %d",&m,&n);
		for (i=0;i<=m+1;i++)
		for (j=0;j<=n+1;j++) a[i][j]=20000;
		for (i=1;i<=m;i++)
		for (j=1;j<=n;j++) scanf("%d",&a[i][j]);
		for (i=1;i<=m*n;i++) 
		{
			f[i]=-1;
			c[i]=-1;
		}
		for (i=1;i<=m;i++)
		for (j=1;j<=n;j++)
		{
			x=i-1;
			y=j;
			if (a[i][j-1]<a[x][y])
			{
				x=i;
				y=j-1;
			}
			if (a[i][j+1]<a[x][y])
			{
				x=i;
				y=j+1;
			}
			if (a[i+1][j]<a[x][y])
			{
				x=i+1;
				y=j;
			}
			if (a[x][y]>=a[i][j]) continue;
			f1=fa((x-1)*n+y);
			f2=fa((i-1)*n+j);
			if (f1!=f2)
			{
				if (f[f1]<f[f2])
				{
					f[f1]+=f[f2];
					f[f2]=f1;
				}
				else
				{
					f[f2]+=f[f1];
					f[f1]=f2;
				}
			}
		}
		cur=0;
		for (i=1;i<=m;i++)
		for (j=1;j<=n;j++)
		{
			f1=fa((i-1)*n+j);
			if (c[f1]==-1)
			{
				c[f1]=cur;
				cur++;
			}
			b[i][j]='a'+c[f1];
		}
		printf("Case #%d:\n",ci);
		for (i=1;i<=m;i++)
		{
			printf("%c",b[i][1]);
			for (j=2;j<=n;j++) printf(" %c",b[i][j]);
			printf("\n");
		}
	}
	return 0;
}

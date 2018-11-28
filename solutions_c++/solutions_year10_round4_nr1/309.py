/*Elegant Diamond*/
#include<stdio.h>
#include<string.h>
int a[155][155],b[310][310];
bool check(int u,int v,int k,int n)
{
	int i,j,x,y;
	memset(b,-1,sizeof(b));
	for (i=0;i<n;i++)
		for (j=0;j<n;j++)
			b[i+u][j+v]=a[i][j];
	for (i=0;i<n;i++)
	{
		for (j=0;j<n;j++)
		{
			x=j+v;
			y=i+u;
			if (b[x][y]!=-1&&b[x][y]!=b[y][x])
				return 0;
			y=k-1-i-u;
			x=k-1-j-v;
			if (b[x][y]!=-1&&b[x][y]!=b[i+u][j+v])
				return 0;
		}
	}
	return 1;
}
int cal()
{
	int n,i,j,k,u,v,ans;
	scanf("%d",&n);
	for (i=0;i<n;i++)
		for (j=0;j<=i;j++)
			scanf("%d",&a[i-j][j]);
	for (i=n-2;i>=0;i--)
		for (j=0;j<=i;j++)
			scanf("%d",&a[n-1-j][n-i-1+j]);
	ans=-1;
	for (k=n;ans==-1;k++)
	{
		for (u=0;u+n<=k&&ans==-1;u++)
		{
			v=0;
			if (check(u,v,k,n))
			{
				ans=k;
				break;
			}
			if (k!=n)
			{
				v=k-n;
				if (check(u,v,k,n))
				{
					ans=k;
					break;
				}
			}
		}
		for (v=1;v+n<=k&&ans==-1;v++)
		{
			if (check(0,v,k,n))
			{
				ans=k;
				break;
			}
			if (k!=n)
			{
				u=k-n;
				if (check(u,v,k,n))
				{
					ans=k;
					break;
				}
			}
		}
	}
	return ans*ans-n*n;
}
int main()
{
	int t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
		printf("Case #%d: %d\n",tt,cal());
	return 0;
}

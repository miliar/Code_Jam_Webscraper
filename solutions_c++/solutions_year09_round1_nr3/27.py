#include<iostream>
using namespace std;
double c[50][50];
double a[50];
int i,ci,cn,n,m,j;
double x,y,z;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	c[0][0]=1.0;
	for (i=1;i<=40;i++)
	{
		c[i][0]=c[i][i]=1.0;
		for (j=1;j<i;j++) c[i][j]=c[i-1][j-1]+c[i-1][j];
	}
	scanf("%d",&cn);
	for (ci=1;ci<=cn;ci++)
	{
		scanf("%d %d",&n,&m);
		a[n]=0;
		for (i=n-1;i>=0;i--)
		{
			y=1.0;
			x=1.0;
			for (j=0;j<=m && i+j<=n;j++)
			{
				if (m-j>i || j>n-i) z=0;
				else z=c[i][m-j]*c[n-i][j]/c[n][m];
				if (j==0) x-=z;
				else y+=z*a[i+j];
			}
			a[i]=y/x;
		}
		printf("Case #%d: %.7lf\n",ci,a[0]);
	}
	return 0;
}

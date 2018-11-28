#include<stdio.h>
#include<string.h>
bool a[105][105];
bool check()
{
	int i,j;
	for (i=1;i<=100;i++)
		for (j=1;j<=100;j++)
			if (a[i][j])
				return 0;
	return 1;
}
int cal()
{
	int n,i,j,k,x1,x2,y1,y2;
	memset(a,0,sizeof(a));
	scanf("%d",&n);
	for (k=0;k<n;k++)
	{
		scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
		for (i=x1;i<=x2;i++)
			for (j=y1;j<=y2;j++)
				a[i][j]=1;
	}
	for (k=0;;k++)
	{
		if (check())
			break;
		for (i=100;i>=1;i--)
		{
			for (j=100;j>=1;j--)
			{
				if (a[i-1][j]==0&&a[i][j-1]==0)
					a[i][j]=0;
				if (a[i-1][j]==1&&a[i][j-1]==1)
					a[i][j]=1;
			}
		}
	}
	return k;
}
int main()
{
	int t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
		printf("Case #%d: %d\n",tt,cal());
	return 0;
}

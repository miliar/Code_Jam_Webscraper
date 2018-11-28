#include<stdio.h>
#include<string.h>
int a[12][2000],b[2000];
int dfs(int l,int r)
{
	int i,temp;
	if (l==r)
	{
		return 0;
	}
	temp=dfs(l,(l+r)/2)+dfs((l+r)/2+1,r);
	for (i=l;i<=r;i++)
		if (b[i]==0)
			break;
	if (i>r)
	{
		for (i=l;i<=r;i++)
			b[i]--;
		return temp;
	}
	else
		return temp+1;
}
int cal()
{
	int n,i,j;
	scanf("%d",&n);
	for (i=0;i<(1<<n);i++)
		scanf("%d",b+i);
	for (i=0;i<n;i++)
		for (j=0;j<(1<<(n-i-1));j++)
			scanf("%d",&a[i][j]);
	return dfs(0,(1<<n)-1);
}
int main()
{
	int t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
		printf("Case #%d: %d\n",tt,cal());
	return 0;
}

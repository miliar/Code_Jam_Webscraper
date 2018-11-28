#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long int64;
int a[505][505],c[505][505],b[505];
int cal(int n,int k)
{
	int i,temp;
	if (a[n][k]!=-1)
		return a[n][k];
	if (k==1)
		return a[n][k]=1;
	if (k==n)
		return a[n][k]=1;
	a[n][k]=0;
	for (i=1;i<k;i++)
	{
		if (n-k-1>=k-i-1)
		{
			temp=((int64)cal(k,i)*c[n-k-1][k-i-1])%100003;
			a[n][k]=(a[n][k]+temp)%100003;
		}
	}
	return a[n][k];
}
void init()
{
	int i,j;
	memset(c,0,sizeof(c));
	for (i=0;i<=500;i++)
	{
		c[i][0]=c[i][i]=1;
		for (j=1;j<i;j++)
			c[i][j]=(c[i-1][j-1]+c[i-1][j])%100003;
	}
	memset(a,-1,sizeof(a));
	for (i=2;i<=500;i++)
	{
		b[i]=0;
		for (j=1;j<i;j++)
			b[i]=(b[i]+cal(i,j))%100003;
	}
	return;
}
int main()
{
	int t,tt,n;
	init();
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",tt,b[n]);
	}
	return 0;
}
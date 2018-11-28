#include <iostream>
using namespace std;

int a[111][111];


int valid(int k, int m, int p)
{
	int res = 1;
	for (int j=0;j<2*k-1;j++)
		for (int h=0;h<2*k-1;h++)
		{
			if (2*m-j>=0&&2*m-j<2*k-1)
			{
				if (a[j][h]!=a[2*m-j][h] && a[j][h]*a[2*m-j][h])
					res=0;
			}
			if (2*p-h>=0&&2*p-h<2*k-1)
			{
				if (a[j][h]!=a[j][2*p-h] && a[j][h]*a[j][2*p-h])
					res=0;
			}
		}
	if (!res)
		return -1;
	if (m<k-1)
		m=2*k-2-m;
	if (p<k-1)
		p=2*k-2-p;
	int n=m+p-k+2;
	return n*n-k*k;
}

int check(int k)
{
	int n = 100000;
	for (int j=0;j<2*k-1;j++)
	{
		for (int h=0;h<2*k-1;h++)
		{
			int z = valid(k,j,h);
			if (z>-1)
				n=min(n,z);
		}
	}
	return n;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,k;
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&k);
		int sx=k-1, sy=0;
		for (int j=0;j<k;j++)
		{
			int s=sx;
			int d=sy;
			for (int h=0;h<k;h++)
			{
				a[s][d]=1;
				s--;
				d++;
			}
			sx++;
			sy++;
		}
		for (int j=0;j<2*k-1;j++)
			for (int h=0;h<2*k-1;h++)
				if (a[j][h])
				{
					scanf("%d",a[j]+h);
					a[j][h]++;
				}
		int val = check(k);
		printf("Case #%d: %lld\n",i+1,val);
	}
	return 0;
}
#include <stdio.h>
double res[1009];

int T;
int n;
double Ver(int n, int d)
{
	double td = 1;
	for (int i=1;i<=d;i++)
	{
		td*=i;
	}
	double k=1;
	double res = 1/td;
	for (int i=1;i<=n;i++)
	{
		k*=i;
		double t = 1/td;
		t/=k;
		if (i & 1)
			res-=t;
		else
			res+=t;
	}
	return res;
}
int main()
{/*
	res[0]=0;
	res[1]=0;
	for (int i=2;i<=1000;i++)
	{
		for (int j=1;j<=i;j++)
		{
			res[i]+=Ver(i-j,j)*res[i-j];
		}
		res[i]+=1;
		res[i]/=(1-Ver(i,1));
	}*/
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		scanf("%d",&n);
		int S=0;
		for (int i=0;i<n;i++)
		{
			int t;
			scanf("%d",&t);
			if (t == i+1)
				S++;
		}
		printf("Case #%d: %.6lf\n",test,(double)(n-S));
	}
	return 0;
}
#include <stdafx.h>
#include <stdio.h>

const long maxn=105;
long wp[maxn][3];
double owp[maxn];
double oowp[maxn];
long n,t,q,k,test;
long a[maxn][maxn];
char c;

void calc_wp()
{
	for (long choice=1;choice<=n;choice++)
	{
		long sum=0;
		long cht=0;
		for (q=1;q<=n;q++)
			if (a[choice][q]!=-1)
			{
				sum+=a[choice][q];
				cht++;
			}
		wp[choice][1]=sum;
		wp[choice][2]=cht;
		//wp[choice]=(double)sum/cht;
	}
}

void calc_owp()
{
	for (long choice=1;choice<=n;choice++)
	{
		double sum=0.0;
		long cht=0;
		for (q=1;q<=n;q++)
			if (a[choice][q]!=-1)
			{
				sum+=(double)(wp[q][1]-a[q][choice])/(double)(wp[q][2]-1);
				cht++;
			}
		owp[choice]=sum/cht;
	}
}

void calc_oowp()
{
	for (long choice=1;choice<=n;choice++)
	{
		double sum=0.0;
		long cht=0;
		for (q=1;q<=n;q++)
			if (a[choice][q]!=-1)
			{
				sum+=owp[q];
				cht++;
			}
		oowp[choice]=sum/cht;
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	scanf("%ld",&t);
	for (test=1;test<=t;test++)
	{
		scanf("%ld\n",&n);
		for (q=1;q<=n;q++)
		{
			for (k=1;k<=n;k++)
			{
				scanf("%c",&c);
				if (c=='1')
					a[q][k]=1;
				else if (c=='0')
					a[q][k]=0;
				else a[q][k]=-1;
			}
			scanf("\n");
		}

		calc_wp();
		calc_owp();
		calc_oowp();

		printf("Case #%ld:\n",test);
		for (long i=1;i<=n;i++)
		{
			double temp=(double)wp[i][1]/wp[i][2];
			double res=0.25*temp+0.5*owp[i]+0.25*oowp[i];
			printf("%0.10lf\n",res);
		}
	}
}
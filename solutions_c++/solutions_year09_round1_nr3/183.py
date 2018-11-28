#include <iostream>
#include <cmath>

using namespace std;

int C,K;

double gg[50][50];
double gun(int n,int k)
{
	if(n<k) return 0.0;
	if(k==0) return 1.0;
	if(gg[n][k]>=0) return gg[n][k];
	return gg[n][k]=gun(n-1,k)+gun(n-1,k-1);
}

double ff[50];
double fun(int n)
{
	if(n==C) return 0.0;
	if(ff[n]>=0) return ff[n];
	int i;
	bool ok=false;
	double ret=0,s=1;
	for(i=n+1;i<=C;i++)
	{
		if(i<=n+K&&i>=K)
		{
			ok=true;
			double r=gun(n,n+K-i)*gun(C-n,i-n)/gun(C,K);
			s-=r;
			ret+=(fun(i)+1)*r;
		}
	}
	if(!ok) return 0;
	double x=s;
	return ff[n]=(ret+s)/(1-s);
	/*
	int i;
	bool ok=false;
	double ret=0;
	double s=1;
	if(ff[n]>=0) return ff[n];
	for(i=0;i<n;i++)
	{
		if(i>0&&i<K) continue;
		if(i+K>=n&&n>=K)
		{
			ok=true;
			double r=gun(i,i+K-n)*gun(C-i,n-i)/gun(C,K);
			ret+=(fun(i)+1.0)*r;
			s-=r;
		}
	}
	if(!ok) return 0;
	return ff[n]=(ret+s)/(1-s);*/
}

int main()
{
	memset(gg,0xff,sizeof(gg));
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d%d",&C,&K);
		memset(ff,0xff,sizeof(ff));
		double ret=fun(0);
		printf("Case #%d: %.7f\n",cse,ret);
	}
	return 0;
}

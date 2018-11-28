/*
 TASK: D. GoroSort
 LANG: C++
 by pasin30055
*/
#include <iostream>
#include <cstdio>
#include <algorithm>

#define MAX_N 1005
#define INF 1000000000

using namespace std;

int n;
int i,j,k;
int t,iii;
int cnt;
int p[MAX_N];
int val[MAX_N];
double der[MAX_N];
double fac[MAX_N];
double mic[MAX_N];
double sum;

void precomp()
{
	fac[0]=1.0;
	for(i=1;i<MAX_N;i++)
	{
		fac[i]=i*fac[i-1];
	}
	for(i=1;i<MAX_N;i++)
	{
		for(j=0;j<=i;j++)
		{
			if(j%2==0)
				der[i]+=(fac[i]/fac[j]);
			else
				der[i]-=(fac[i]/fac[j]);
		}
	}
	mic[0]=0.0;
	for(i=1;i<MAX_N;i++)
	{
		mic[i]=INF;
		mic[i]*=INF;
		for(j=0;j<1;j++)
		{
			//FIX J ELEMENT
			j=0;
			sum=0;
			for(k=0;k<i-j;k++)
			{
				sum+=((fac[i-j]/(fac[i-j-k]*fac[k]))*(der[k]/fac[i-j])*mic[k+j]);
			}
			sum+=1.0;
			sum/=(1-(der[i-j]/fac[i-j]));
			//if(i==2)
			//	printf("%d %lf %lf %lf\n",j,sum,der[i-j],fac[i-j]);
			if(sum<mic[i])
				mic[i]=sum;
		}
	}
	return ;
}

int main()
{
	freopen("D-large.in.txt","r",stdin);
	freopen("D-large-out.txt","w",stdout);
	precomp();
	scanf("%d",&t);
	for(iii=0;iii<t;iii++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&val[i]);
			p[i]=val[i];
		}
		sort(p,p+n);
		cnt=0;
		for(i=0;i<n;i++)
		{
			val[i]=lower_bound(p,p+n,val[i])-p;
			if(val[i]==i)
				cnt++;
		}
		printf("Case #%d: %.6lf\n",iii+1,(float)(n-cnt));
	}
	return 0;
}
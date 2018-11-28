#include <iostream>
#include <stdio.h>

using namespace std;

double binom[1001][1001];
double fac[1001];
double dearr[1001];
double dp[1001];

int main()
{
	/*for(int n=1;n<=1000;n++)
	{
		binom[n][0]=binom[n][n]=1;
		
		for(int k=1;k<n;k++)
		{
			binom[n][k]=binom[n-1][k-1]+binom[n-1][k];
		}
	}
	
	fac[1]=1;
	
	for(int n=2;n<=1000;n++)
	{
		fac[n]=n*fac[n-1];
	}
	
	dearr[0]=0;
	dearr[1]=0;
	dearr[2]=1;
	
	for(int n=3;n<=1000;n++)
	{
		dearr[n]=(n-1)*(dearr[n-1]+dearr[n-2]);
	}
	
	dp[0]=1;
	dp[1]=0;

	for(int n=2;n<=100;n++)
	{
		
		dp[n]=0;
		
		// let all free
		for(int i=1;i<=n;i++)
		{
			dp[n]+=binom[n][i]*dearr[n-i]*dp[n-i];
		}
		
		dp[n]=dp[n]/fac[n];
		dp[n]+=1;
		dp[n]=dp[n]/(1-dearr[n]/fac[n]);
		
	//	cout<<" N : "<<n<<" VAL : "<<dp[n]<<endl;
	}*/
	
	int T;
	
	scanf("%d",&T);
	
	for(int t=0;t<T;t++)
	{
		int N;
		scanf("%d",&N);
		
		int res =0;
		
		for(int n=0;n<N;n++)
		{
			int a;
			scanf("%d",&a);
			
			if(a!=n+1)
			{
				res++;
			}
		}
		
		printf("Case #%d: %.6lf\n",t+1,(double)res);
	}
	
	
	
	
	
}
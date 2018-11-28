#include<iostream>
#include<cstring>
#define MOD 100003
using namespace std;
main()
{
	int i,j,n,test,arr[501][501],dp[501][501];
	for(i=0;i<=500;i++)
	{
		
		arr[0][i]=arr[i][0]=arr[i][i]=1;
		
	}
	for(i=1;i<=500;i++)
	{
		arr[i][i]=1;
		for(j=1;j<i;j++)
		{
			arr[i][j]=arr[i-1][j] + arr[i-1][j-1];
			arr[i][j]=arr[i][j]%MOD;
		}
	}
//	cout<<arr[2][1];
	memset(&dp,0,sizeof(dp));
	dp[2][1]=dp[2][0]=1;
	int k;
	for(i=3;i<=500;i++)
	{
		//dp[i][1]=1;
		for(j=i-1;j>=1;j--)
		{
			if(j==1)
			{dp[i][j]=1;continue;}
			dp[i][j]=0;
			for(k=max(1,2*j-i);k<j;k++)
			{
				

				dp[i][j]+=dp[j][k]*arr[i-j-1][j-k-1];
				dp[i][j]=dp[i][j]%MOD;
	//			if(i==6)
	//			cout<<i<<" "<<j<<" "<<k<<" "<<i-j-1<<" "<<j-k-1<<" "<<dp[i][j]<<endl;
			}
		}
		//cout<<i<<endl;
		dp[i][0]=0;
		for(j=1;j<=i-1;j++)
		{
			dp[i][0]+=dp[i][j];
			dp[i][0]=dp[i][0]%MOD;
		}
		//dp[i][0]++;
	}
	cin>>test;
	for(i=1;i<=test;i++)
	{
		cin>>n;
		cout<<"Case #"<<i<<": "<<dp[n][0]<<endl;
	}
}
			
	
	
	

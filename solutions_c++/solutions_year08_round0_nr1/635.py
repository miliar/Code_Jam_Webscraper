#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	const int inf=1000000000;
	int zu;
	cin>>zu;
	int g=1;
	string s;
	while(zu--)
	{
		int m,n;
		cin>>m;
		getline(cin,s);
		map<string,int>mp;
		for(int i=1;i<=m;i++)
		{
			getline(cin,s);
			mp[s]=i;
			//cout<<s<<endl;
		}
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<g++<<": "<<0<<endl;
			continue;
		}
		getline(cin,s);
		vector<int>a(n);
		for(int i=0;i<n;i++)
		{
			getline(cin,s);
			a[i]=mp[s];
		}
		vector<vector<int> >dp(n,vector<int>(m+1,inf));
		for(int i=1;i<=m;i++)
		{
			if(a[0]==i)
				dp[0][i]=inf;
			else
				dp[0][i]=0;
		}
		for(int i=1;i<n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				if(a[i]==j)
				{
					dp[i][j]=inf;
					continue;
				}
				for(int k=1;k<=m;k++)
				{
					if(j==k)
						dp[i][j]=min(dp[i][j],dp[i-1][j]);
					else
						dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
				}
			}
		}
		int d=inf;
		for(int i=1;i<=m;i++)
			d=min(d,dp[n-1][i]);
		cout<<"Case #"<<g++<<": "<<d<<endl;
	}
}
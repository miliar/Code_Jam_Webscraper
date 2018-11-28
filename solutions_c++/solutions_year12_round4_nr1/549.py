#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int dp[11000];
int d[11000];
int l[11000];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int re,i,j,k,n,x,L;
	cin>>re;
	int cases=1;
	while(re--)
	{
		
		memset(dp,0,sizeof(dp));
		
		cin>>n;
		for(i=1;i<=n;i++)
		cin>>d[i]>>l[i];
		cin>>L;
		dp[1]=d[1];
		
		bool ff=false;
		for(i=1;i<n;i++)
		{
			for(j=i+1;j<=n;j++)
			{
				
				x=d[j]-d[i];
			//	cout<<j<<" "<<x<<endl;
				if(x>dp[i])
				continue;
				x=min(x,l[j]);
				dp[j]=max(dp[j],x);
			}
		}
		
	
		
		for(i=1;i<=n;i++)
		{
			if(d[i]+dp[i]>=L)
			ff=true;
		}
		cout<<"Case #"<<cases++<<": ";
		if(ff)
		cout<<"YES"<<endl;
		else cout<<"NO"<<endl; 
		
		
	}
	
	
	return 0;
	
}
 
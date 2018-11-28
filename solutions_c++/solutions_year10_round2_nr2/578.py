#include <iostream>
using namespace std;
int main()
{
	
	freopen("out.txt","w",stdout);
	int n,k,b,t,i;
	int x[100];
	int v[100];
	bool can[100];
	int sum[100];
	int cnt=0;
	int ca,temp,ans;
	cin>>ca;
	while(ca--)
	{
		cin>>n>>k>>b>>t;
		for(i=1;i<=n;i++)
			cin>>x[i];
		for(i=1;i<=n;i++)
			cin>>v[i];
		for(i=1;i<=n;i++)
		{
			if(v[i]*t>=(b-x[i]))
				can[i]=1;
			else
				can[i]=0;
		}
		sum[n+1]=0;
		for(i=n;i>=1;i--)
		{
			if(can[i]==0)
				sum[i]=sum[i+1]+1;
			else
				sum[i]=sum[i+1];
		}
		temp=0;
		ans=0;
		for(i=n;i>=1;i--)
		{
			if(temp<k)
			{
				if(can[i])
				{
					temp++;
					ans+=sum[i];
				}

			}
			else
				break;
		}
		if(temp<k)
		{
			printf("Case #%d: IMPOSSIBLE\n",++cnt);
		}
		else
		{
			printf("Case #%d: %d\n",++cnt,ans);
		}
	}
	return 0;
}

			

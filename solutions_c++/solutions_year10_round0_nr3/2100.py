#include <iostream>
#include <queue>
using namespace std;
long long g[10000];
int main()
{
	long long r,k,n;
	int tt;
	cin>>tt;
	for (int i=1;i<=tt;++i)
	{
		printf("Case #%d: ",i);
		cin>>r>>k>>n;
		queue <long long> q1,q2;
		for (int i=1;i<=n;++i)
		{
			cin>>g[i];
			q1.push(g[i]);
		}
		long long t=0;
		long long ans=0;
		while (1)
		{
			long long sum=0;
			while (1)
			{
				if (q1.empty())
				{
					ans+=sum;
					t++;
					while (!q2.empty())
					{
						long long f=q2.front();
						q2.pop();
						q1.push(f);
					}
					break;
				}
				long long f=q1.front();
				if (sum+f<=k)
				{
					sum+=f;
					q1.pop();
					q2.push(f);
				}
				else
				{
					ans+=sum;
					t++;
					while (!q2.empty())
					{
						long long f=q2.front();
						q2.pop();
						q1.push(f);
					}
					break;
				}				
			}
			if (t==r)
			{
				break;
			}
		}
		cout<<ans<<endl;		
	}
	return 0;
}
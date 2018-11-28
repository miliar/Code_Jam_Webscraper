#include<iostream>
#include<queue>
using namespace std;

int main()
{
	long long t,c=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%lld",&t);
	while(t--)
	{
		long long r,i,j,k,n,g[1005];
		long long ans=0;
		queue<long long> q;
		scanf("%lld%lld%lld",&r,&k,&n);
		for(i=1;i<=n;i++)
		{
			scanf("%lld",g+i);
			q.push(g[i]);
		}
		while(r)
		{
			long long t;
			long long s=0;
			j=1;
			while(j<=n&&s+q.front()<=k)
			{
				
				t=q.front();
				s+=t;
				q.pop();
				q.push(t);
				j++;
			}
			ans+=s;
			//printf("%lld\n",ans);
			r--;
		}
		printf("Case #%lld: %lld\n",c++,ans);
	}
}

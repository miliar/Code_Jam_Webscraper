#include <iostream>
#define LL long long
using namespace std;

LL T,R,k,N;
LL g[10024];
LL next[10024];
LL sum[10024];

int main()
{
	cin>>T;
    
    for(int t=1;t<=T;t++)
    {
		cin>>R>>k>>N;
		memset(g,0,sizeof(g));
		memset(next,0,sizeof(next));
		memset(sum,0,sizeof(sum));
		
		for(int i=0;i<N;i++)
		{
			cin>>g[i];
			sum[i] = g[i] + ((i>0)? sum[i-1] : 0LL);
		}
			
		for(int i=0;i<N;i++)
		{
			int ti=i;
			long long tsum = g[ti] ;
			int start=ti;
			do
			{
				ti++;
				ti%=N;
				tsum+=g[ti];				
			}
			while(tsum<=k && ti!=start);
			next[i] = ti;
		}
		
		int now = 0;
		long long ans = 0;
		for(int i=1;i<=R;i++)
		{
			int nx = next[now]-1;
			while(nx<0) nx+=N;
			
			long long tmp=0;
			if(nx>=now) tmp = sum[nx] - sum[now] + g[now];
			else tmp = sum[nx] + sum[N-1] - sum[now] + g[now];
		//	if(i%10000==0) cout<<tmp<<" ";
			ans+=tmp;
		//	cout<<"from "<<now<<" to "<<nx<<" : "<<tmp<<endl;
			now = next[now];
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
		//printf("Case #%d: %qd\n",t,ans);
	}
	
	
	
}

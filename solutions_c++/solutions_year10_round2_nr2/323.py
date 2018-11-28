#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
using namespace std;

int main()
{
	freopen("D://in.txt","r",stdin);
	freopen("D://out.txt","w",stdout);

	int t,cas,i,j,N,K,B,T,res,cnt;
	int pos[100],v[100];
	bool get[100];

	cin>>t;
	for (cas=1;cas<=t;cas++)
	{
		cin>>N>>K>>B>>T;
		res=cnt=0;
		memset(get,0,sizeof(get));
		for (i=0;i<N;i++) cin>>pos[i];
		for (i=0;i<N;i++) cin>>v[i];
		for (i=N-1;i>=0;i--)
		{
			if (v[i]*T+pos[i]>=B) get[i]=true;
		}
		for (i=N-1;i>=0;i--)
		{
			if (cnt==K) break;
			if (get[i])
			{
				for (j=i+1;j<N;j++)
				{
					if (!get[j]) res++;
				}
				cnt++;
			}
		}
		cout<<"Case #"<<cas<<": ";
		if (cnt==K) cout<<res<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
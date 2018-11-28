#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int t,T,N,S,P;

int main()
{
	cin>>T;
	while(T--)
	{
		int ans=0;
		vector<int> q;
		cin>>N>>S>>P;
		for(int i=0;i<N;i++) 
		{
			int tmp;
			scanf("%d",&tmp);
			q.push_back(tmp);
		}
		sort(q.begin(),q.end(),greater<int>());
		for(int i=0;i<q.size();i++)
		{
			if(q[i]>=P+2*max(P-1,0)) ans++;
			else if(q[i]>=P+2*max(P-2,0) and S-->0) ans++;
		}
		cout<<"Case #"<<++t<<": "<<ans<<endl;
	}
	return 0;
}

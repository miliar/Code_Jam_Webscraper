#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;


int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int T;
	cin>>T;
	int t;
	for(t = 1 ;t <= T; ++t)
	{
		cout<<"Case #"<<t<<": ";
		int n;
		cin>>n;
		int i;
		vector<pair<int,int> > vine;
		for(i=0;i<n;++i)
		{
			int d,len;
			cin>>d>>len;
			vine.push_back(make_pair(d,len));
		}
		int D;
		cin>>D;
		sort(vine.begin(),vine.end());
		if(vine[0].first>vine[0].second)
		{
			cout<<"NO"<<endl;
			continue;
		}
		else
		{
			bool vis[1000000];
			memset(vis,0,sizeof(vis));
			
			queue<pair<int,int> > Q;//first for idx,second for far
			Q.push(make_pair(0,min(vine[0].first,vine[0].second)));
			vis[0] = true;
			bool flag=false;
			while(!Q.empty())
			{
				int idx = Q.front().first;
				int far = Q.front().second;
				if(vine[idx].first+far>=D) flag=true;
				if(flag) break;
				Q.pop();
				for(i=idx+1;i<vine.size();++i)
				{
					if(vine[idx].first+far<vine[i].first) break;
					if(!vis[i])
					{
						Q.push(make_pair(i,min(vine[i].first-vine[idx].first,vine[i].second)));
						vis[i]=true;
					}
				}
			}
			if(flag) cout<<"YES"<<endl;
			else cout<<"NO"<<endl;
		}
	}
	

	return 0;
}

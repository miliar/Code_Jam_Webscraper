#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main()
{
	freopen("a.in","r",stdin) ;
	freopen("a.out","w",stdout) ;
	int cases;
	cin>>cases;
	for(int cas=1;cas<=cases;cas++)
	{
		int P,Q;
		cin>>P>>Q;
		int c=0;
		vector<int> V;
		while(c<Q)
		{
			int k;
			cin>>k;
			V.push_back(k);
			c++;
		}
		sort(V.begin(),V.end());
		int ans=100000;
		do
		{
			vector<pair<int,int> > Range;
			Range.push_back(make_pair(1,P));
			int curans=0;
			for(int i=0;i<V.size();i++)
			{
				for(int j=0;j<Range.size();j++)
					if(V[i]>=Range[j].first && V[i]<=Range[j].second)
					{
						curans+=Range[j].second-Range[j].first;
						int t=Range[j].second;
						Range[j].second=V[i]-1;
						Range.push_back(make_pair(V[i]+1,t));
						break;
					}
			}
			ans=min(ans,curans);
			
		}while(next_permutation(V.begin(),V.end()));
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}
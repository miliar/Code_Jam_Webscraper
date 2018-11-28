//In the name of Allah
//
//
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
typedef pair<int,int> pii;
vector <pii> seq;
vector <int> list[2];
int t,n;
int p[2];
int cu[2];
int main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int cas=0;cas<t;cas++)
	{
		seq.clear();
		list[0].clear();
		list[1].clear();
		p[0]=p[1]=1;
		cu[0]=cu[1]=0;
		cin>>n;
		for (int i=0;i<n;i++)
		{
			char a;
			int b;
			cin>>a>>b;
			if (a=='O')
			{
				list[0].push_back(b);
				seq.push_back(pii(0,b));
			}
			else
			{
				list[1].push_back(b);
				seq.push_back(pii(1,b));
			}
		}
		int t=0;
		for (int i=0;i<n;i++)
		{
			t+=abs(seq[i].second-p[seq[i].first])+1;
			int v=!seq[i].first,vp=seq[i].first;
			cu[vp]++;
			if (cu[v]<list[v].size())
			{
				if (abs(seq[i].second-p[vp])+1>=abs(p[v]-list[v][cu[v]]))
					p[v]=list[v][cu[v]];
				else
				{
					int st=abs(seq[i].second-p[vp])+1;
					if (p[v]>list[v][cu[v]])
						p[v]-=st;
					else
						p[v]+=st;
				}
			}
			p[vp]=seq[i].second;
		}
		cout<<"Case #"<<cas+1<<": "<<t<<endl;
	}
	return 0;
}

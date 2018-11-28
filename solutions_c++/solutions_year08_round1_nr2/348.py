#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;


int main()
{
	int c;
	cin>>c; int cn=0;
	while(c--)
	{
		cn++;
		int n,m,t,x,y;
//		adj=vector<vector<pair<int,int> > >(m,vector<pair<int,int> >());
		cin>>n>>m;
		vector<vector<pair<int,int> > > adj(m);		
		for(int i=0;i<m;i++)
		{
			cin>>t;
			for(int k=0;k<t;k++){
				cin>>x>>y; x--;
				adj[i].push_back(make_pair(x,y));
			}
		}
//		cout<<n<<' '<<m<<' '<<adj.size()<<endl;
		int bmalted=1000000; int conf=0;
		for(int mask=0;mask<(1<<n);mask++)
		{
			bool possible=true;
			for(int i=0;i<m;i++)
			{
				bool sat=false;
				for(int j=0;j<sz(adj[i]);j++)
				{
					int flav=adj[i][j].first, malt=adj[i][j].second;
					int on=false;
					if(mask&(1<<flav)) on=true;
					if(malt && on) sat=true;
					if(!malt && !on) sat=true;
				}
				if(!sat) possible=false;
			}
			if(!possible) continue;
			int bitc=__builtin_popcount(mask);
			if(bitc<bmalted)
			{
				bmalted=bitc; conf=mask;

			}
		}
		cout<<"Case #"<<cn<<": ";
		if(bmalted>=1000000)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		for(int i=0;i<n;i++)
		{
			if(i) cout<<' ';
			
			if(conf&(1<<i)) cout<<'1';
			else cout<<'0';
		}
		cout<<endl;

	}

	return 0;
}

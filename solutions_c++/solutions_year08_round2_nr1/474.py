#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <numeric>

using namespace std;

#define v vector <int>
#define vs vector <string>
#define vv vector< v >
#define forz(i,n) for(int i=0;i<n;i++)
#define fl(i,s,n) for(int i=s;i<n;i++)
#define lh(i) int(i.length())
#define sz(i) (int)(i.size())
#define pb(a) push_back(a)
#define all(a) a.begin(),a.end()
#define mp make_pair

int main()
{
	int t;
	cin>>t;
	int ot=0;
	while(t--)
	{
		long long n,a,b,c,d,x1,y1,m;
		cin>>n>>a>>b>>c>>d>>x1>>y1>>m;
		vector <pair <long long,long long> >pp;
//		map< pair<int,int>, int>mm;
		pp.pb(mp(x1,y1));
//		mm[pp[0]]=1;
		forz(i,n-1)
		{
			x1=(a*x1+b)%m;
			y1=(c*y1+d)%m;
			pp.pb(mp(x1,y1));
//			mm[pp[i+1]]=1;
		}
		int ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				for(int k=j+1;k<n;k++)
				{
					long long c1;
					long long c2;
					if((pp[i].first+pp[j].first+pp[k].first) %3==0)c1=(pp[i].first+pp[j].first+pp[k].first) /3;else continue;
					if((pp[i].second+pp[j].second+pp[k].second)%3==0)c2=(pp[i].second+pp[j].second+pp[k].second)/3;else continue;
					//if(mm[mp(c1,c2)]==1)
					ans++;			
				}	
			}
		}
	cout<<"Case #"<<++ot<<": "<<ans<<endl;
	}
	return 0;
}
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
using namespace std;

int main()
{
	int n,t,na,nb,rr=0;
	cin>>n;
	while(n--)
	{
		cin>>t;
		cin>>na>>nb;
		string t1,t2;
		int a,b,c,d;
		vector <pair < pair<int,int> ,int> >pp;
		forz(i,na)
		{	
			cin>>t1>>t2;
			sscanf(t1.c_str(),"%d:%d",&a,&b);
			sscanf(t2.c_str(),"%d:%d",&c,&d);
			pp.pb(mp(mp(a*60+b,c*60+d),1));		
		}
		forz(i,nb)
		{	
			cin>>t1>>t2;
			sscanf(t1.c_str(),"%d:%d",&a,&b);
			sscanf(t2.c_str(),"%d:%d",&c,&d);
			pp.pb(mp(mp(a*60+b,c*60+d),2));		
		}
		sort(all(pp));
		v h1;
		v h2;	
		int cnt1=0,cnt2=0;
		forz(i,sz(pp))
		{
			int flg=0;
			if(pp[i].second==1)
			{
				forz(i1,sz(h1))if(h1[i1]<=pp[i].first.first){flg=1;h2.pb(pp[i].first.second+t);h1.erase(i1+h1.begin());break;}
				if(flg==1)
				{
				}
				else
				{
					cnt1++;
					h2.pb(pp[i].first.second+t);
				}
			}
			else 
			{
				forz(i1,sz(h2))if(h2[i1]<=pp[i].first.first){flg=1;h1.pb(pp[i].first.second+t);h2.erase(i1+h2.begin());break;}
				if(flg==1)
				{
				}
				else
				{
					cnt2++;
					h1.pb(pp[i].first.second+t);
				}	
			}
		}
		cout<<"Case #"<<++rr<<": "<<cnt1<<" "<<cnt2<<endl;
	}
return 0;
}




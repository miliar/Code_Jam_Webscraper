#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <list>
using namespace std;
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int
int t,n;
map< char, set<char> > opp;
map< pair< char, char > , char > com;
vector<char> ans;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	rp(num,t)
	{
		int c;
		cin>>c;
		com.clear();
		rp(i,c)
		{
			char a,b,d;
			cin>>a>>b>>d;
			com[mp(a,b)]=d;
			com[mp(b,a)]=d;
		}
		cin>>c;
		opp.clear();
		rp(i,c)
		{
			char a,b;
			cin>>a>>b;
			opp[a].insert(b);
			opp[b].insert(a);
		}
		cin>>c;
		ans.clear();
		rp(i,c)
		{
			char a;
			cin>>a;
			if (L(ans)>0 && com.find(mp(ans.back(),a))!=com.end())
			{
				char b=ans.back();
				ans.pop_back();
				ans.pb(com[mp(b,a)]);
			}
			else
			{
				bool fnd=0;
				rp(i,L(ans))
					if (opp[a].find(ans[i])!=opp[a].end())
					{
						ans.clear();
						fnd=1;
						break;
					}
				if (!fnd)
					ans.pb(a);
			}
		}
		cout<<"Case #"<<num+1<<": [";
		rp(i,L(ans))
		{
			if (i)
				cout<<", ";
			cout<<ans[i];
		}
		cout<<"]\n";
	}
}
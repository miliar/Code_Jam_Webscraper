#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std; 

#define PB push_back 
#define MP make_pair 

#define rep(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,l,h) for(int i=(l);i<=(h);++i) 
#define FORD(i,h,l) for(int i=(h);i>=(l);--i) 
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef long long int64; 
typedef pair<int,int> pii; 

int c,d,n;
map < pair<char,char>, char> comp;
set < pair<char,char> > opp;
string str;


int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T; cin>>T;
	FOR(Case,1,T)
	{
		comp.clear();
		opp.clear();
		cin>>c;
		rep(i,c)
		{
			string s; cin>>s; comp[MP(s[0],s[1])]=s[2]; comp[MP(s[1],s[0])]=s[2];
		}
		cin>>d;
		rep(i,d)
		{
			string s; cin>>s; opp.insert(MP(s[0],s[1])); opp.insert(MP(s[1],s[0]));
		}
		cin>>n>>str;
		vector <char> ans;
		rep(i,n)
		{
			if(ans.empty()) { ans.PB(str[i]); continue;}
			ans.PB(str[i]);
			while(ans.size() > 1)
			{
				char a=ans.back(), b=ans[ans.size()-2];
				if(comp.find(MP(a, b)) != comp.end())
				{
					ans.pop_back(); ans.pop_back(); ans.PB(comp[MP(a,b)]);
				}
				else break;
			}
			rep(i,ans.size()) rep(j,ans.size()) if(i!=j)
			{
				if(opp.find(MP(ans[i],ans[j])) != opp.end())
				{
					ans.clear(); break;
				}
			}
		}
		cout<<"Case #"<<Case<<": [";
		rep(i,ans.size())
		{
			if(i) cout<<", ";
			cout<<ans[i];
		}
		cout<<']'<<endl;
	}
}
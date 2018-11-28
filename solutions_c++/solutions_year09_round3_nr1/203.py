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
#include<cstring>
#include<locale>
#include<utility>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;
lli get(vector<int> now,int base)
{
    lli res=0;
    for(int i=0;i<now.size();i++) res=res*base+now[i];
    return res;
}
int main()
{
    int t, cn=0;
    cin>>t;
    while(t--)
    {
	cn++;
	string num;
	cin>>num;
	set<char> diff(all(num));
	int base=diff.size();
	if(base<2) base++;
	set<int> used;
	vector<int> now;
	map<char,int> mp;
	
	for(int i=0;i<num.size();i++)
	{
	    if(mp.count(num[i]))
	    {
		now.push_back(mp[num[i]]);
		continue;
	    }

	    if(i==0)
	    {
		now.push_back(1);
		used.insert(1);
		mp[num[i]]=1;	
	    }
	    else
	    {
		for(int d=0;d<base;d++) if(!used.count(d))
		{
		    now.push_back(d);
		    used.insert(d);
		    mp[num[i]]=d;
		    break;
		}
	    }
	    
	}
//	cerr<<base<<endl;
//	for(int i=0;i<now.size();i++) cerr<<now[i]<<' '; cerr<<endl;
	lli res=get(now,base);
	cout<<"Case #"<<cn<<": "<<res<<endl;
    }
}

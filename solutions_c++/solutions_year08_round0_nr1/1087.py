#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define sz(X) ((int)(X.size()))
#define ln(X) ((int)(X.length()))
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define rrep(i,s,n) for(int i=n-1; i>=s; i--)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define err 1E-15

using namespace std;

int main()
{
    int n;
    cin>>n;
	for(int runs = 1; runs <= n; runs++)
	{
		int nse;
		cin>>nse;
		string temp;
		getline(cin,temp);
		vector<string> s;
		for(int i = 0; i < nse; i++)
		{	
			getline(cin,temp,'\n');
			//cout<<temp<<endl;
			s.pb(temp);
		}
		int nq;
		cin>>nq;
		//cout<<nq<<endl;
		getline(cin,temp);
		vector<string> q;
		for(int i = 0; i < nq; i++)
		{
			getline(cin,temp,'\n');
			//cout<<temp<<endl;
			q.pb(temp);
		}
		int ans = 0;
		int prev = 0;
		//rep(i,0,sz(s))cout<<s[i]<<endl;
		//rep(i,0,sz(q)) cout<<q[i]<<endl;
		//return 0;
		vector<int> hits(nse);
		while(true)
		{
			for(int i = 0; i < sz(s); i++)
				hits[i] = find(q.begin() + prev, q.end(), s[i]) - q.begin();
			//for(int i = 0; i < nse; i++) cout<<hits[i]<<" "; cout<<endl;
			int cand = max_element(hits.begin(), hits.end()) - hits.begin();
			//cout<<cand<<"........"<<endl;
			if(hits[cand] == sz(q)) break;
			ans++;
			prev = hits[cand];
		}
		cout<<"Case #"<<runs<<": "<<ans<<endl;
		
		
	}
	return 0;
}
	
	
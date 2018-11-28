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

int len(string s)
{
	int ret = 1;
	rep(i,0,sz(s) - 1)
	{
		if(s[i] != s[i + 1])
			ret++;
	}
	return ret;
}
string encode(string s, int k, vector<int> &p)
{
	string ret;
	for(int i = 0; i < sz(s); i += k)
	{
		string t;
		rep(j,0,k)
			t += s[i + p[j] - 1];
		ret += t;
	}
	return ret;
}
int main()
{
	//cout<<len("abcd")<<len("aaaa")<<len("aaad"); 
	freopen("DSin.txt","r",stdin) ;
	freopen("DSout.txt","w",stdout) ;
	int runs;
	cin>>runs;
	rep(cnt,1,runs+1)
	{
		int k; string s;
		cin>>k>>s;
		int ans = 123456789;
		vector<int> p;
		rep(i,0,k) p.pb(i + 1);
		do
		{
			//cout<<encode(s,k,p)<<endl;
			ans = min(ans,len(encode(s,k,p)));
		}
		while(next_permutation(all(p)));
		
		cout<<"Case #"<<cnt<<": "<<ans<<endl;
	}
	return 0;
}

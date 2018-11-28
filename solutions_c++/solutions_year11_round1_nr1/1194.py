#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e12,EPS=1e-9;

int main()
{
	int CS; cin>>CS;
	rep(cs,CS)
	{
		ll n; int pd,pg; cin>>n>>pd>>pg;
		string ans;
		if(pg==100){
			if(pd==100)ans="Possible";
			else ans="Broken";
		}
		else if(pg==0){
			if(pd==0)ans="Possible";
			else ans="Broken";
		}
		else{
			int g=__gcd(pd,100);
			pd/=100;
			
			if(100/g<=n)ans="Possible";
			else ans="Broken";
		}
		cout<<"Case #"<<cs+1<<": "<<ans<<endl;
	}
	
	return 0;
}

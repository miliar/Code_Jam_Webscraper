#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

bool combine(char e,vs& coms,string& res)
{
	if(res.size()==0)
		return false;
	rep(i,coms.size()){
		string& c=coms[i];
		char& rlast=res[res.size()-1];
		if(e==c[0] && rlast==c[1] || e==c[1] && rlast==c[0]){
			rlast=c[2];
			return true;
		}
	}
	return false;
}

bool oppose(char e,vs& opps,string& res)
{
	rep(i,opps.size()){
		string& o=opps[i];
		if(e==o[0] && find(allof(res),o[1])!=res.end() || e==o[1] && find(allof(res),o[0])!=res.end()){
			res.clear();
			return true;
		}
	}
	return false;
}

void solve()
{
	int c; cin>>c;
	vs coms(c);
	rep(i,c) cin>>coms[i];
	int d; cin>>d;
	vs opps(d);
	rep(i,d) cin>>opps[i];
	
	int n; cin>>n;
	string res;
	rep(i,n){
		char e; cin>>e;
		if(combine(e,coms,res))
			continue;
		if(oppose(e,opps,res))
			continue;
		res+=e;
	}
	
	cout<<"[";
	rep(i,res.size())
		cout<<res[i]<<(i==res.size()-1?"":", ");
	cout<<"]"<<endl;
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}

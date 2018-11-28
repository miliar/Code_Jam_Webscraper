#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1e9
#define pb push_back

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double D;
typedef long long LL;

int main() {
	int yo=1,k=0;
	string test,ip,ans;
	for(int _=GI;_--;) {
		test.clear();
		ip.clear();
		ans.clear();
		cin>>test;
		ip=test;
		next_permutation(test.begin(),test.end());
		ans=test;
		if(test<=ip) {
			test.pb('0');
			sort(test.begin(),test.end());
			REP (i,test.sz) {
				if(test[i]!='0') {k=i; break;}
			}
			ans="";
			ans.pb(test[k]);
			REP (i,test.sz) {
				if(i!=k) ans.pb(test[i]);
			}
		}
		cout<<"Case #"<<yo<<": "<<ans<<endl;
		yo++;
	}
	return 0;
}


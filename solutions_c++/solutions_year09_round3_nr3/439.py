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
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

int P,Q;
VI test,ip;

int go() {
	int cnt=0,p;
	REP (i,ip.sz) {
		p=ip[i];
		test[p]=0;
		FOR (i,p+1,test.sz) {
			if(test[i]==0) break;
			cnt++;
		}
		for (int i=p-1;i>=0;i--) {
			if(test[i]==0) break;
			cnt++;
		}
	}
	return cnt;
}

int main() {
	int t,ans,yo=0;
	for(int _=GI;_--;) {
		P=GI;
		Q=GI;
		ip.clear();
		test.clear();
		test.rz(P,1);
		REP (i,Q) {
			t=GI;
			ip.pb(t-1);
		}
		ans=1e9;
		do{
			test.clear();
			test.rz(P,1);
			ans=min(ans,go());
		}while(next_permutation(ip.begin(), ip.end()));
		printf("Case #%d: %d\n",++yo,ans);
	}
	return 0;
}


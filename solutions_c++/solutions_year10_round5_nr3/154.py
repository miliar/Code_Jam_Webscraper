using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(LL i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 35001
#define GI ({LL _; scanf("%Ld", &_);_;})
#define LINF (1LL<<60)
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;


int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		int n = GI;
		vector < pair<int,int> > v;
		REP(i,n) {
			int a = GI, b= GI;
			v.pb(mkp(a,b));
		}
		int ans=0;
		while(1) {
			int pos = -1, mx = 0;
			REP(i,v.sz) {
				if(mx <= v[i].second && v[i].second >= 2) mx = v[i].second, pos = i;
			}
			if(pos == -1) break;
			int f1 = 0, f2 = 0, prev = v[pos].first-1, next = v[pos].first+1;
			REP(j,v.sz) if(v[j].first == prev) f1 = 1, v[j].second++;
			else if(v[j].first == next) f2 = 1, v[j].second++;

			v[pos].second -= 2;

			if(!f1) v.pb(mkp(prev, 1));
			if(!f2) v.pb(mkp(next,1));
			ans++;
		//	REP(i,v.sz) cout << v[i].first<<","<<v[i].second <<" "; cout << endl;
		}

			printf("Case #%d: ", kase);
			cout << ans << endl;

	}
}

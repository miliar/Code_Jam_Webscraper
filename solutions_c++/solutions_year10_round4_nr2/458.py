#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iterator>
#include <numeric>
#include <complex>
using namespace std;

#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define REPD(i,n) for (int i = n-1; i >= 0; --i)
#define FOR(i,p,k) for (int i = p; i < (int)(k); ++i)
#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> ostream& operator<<(ostream& os, const vector<T>& v) { REP(i,v.size()) os<<'['<<v[i]<<']'; return os; }
#define DEBUG(x) cerr<<#x":"<<(x)<<endl;

const int INF = 100000 * 1<<10 + 1;
int memo[1<<10][10];
int a[1<<10];
int cost[1<<10];
int p, P;

int buy(int val, int l, int r, int missed) {
	//DEBUG(val); DEBUG(missed);
	if (val >= P) {
		FOR (i,l,r) if (a[i] < missed) return INF;
		return 0;
	}
	int& ret = memo[val][missed];
	if (ret != -1) return ret;
	ret = INF;
	FOR (i,l,r) if (a[i] < missed) return ret;
	int m = (l+r)/2;
	ret = min(buy(val*2,l,m,missed) + buy(val*2+1,m,r,missed) + cost[val],
			buy(val*2,l,m,missed+1) + buy(val*2+1,m,r,missed+1));
	return ret;
}

int main() {
	int T; cin>>T;
	for (int cnum = 1; cnum <= T; cnum++) {
		memset(memo,-1,sizeof(memo));
		cin>>p;
		P = 1<<p;
		REP(i,P) cin>>a[i];
		REP(i,p) {
			int tmp = 1<<(p-1-i);
			REP(j,tmp) {
				cin>>cost[tmp+j];
			}
		}
		//REP(i,P) cout<<a[i]<<" "; cout<<endl;
		//REP(i,P) cout<<cost[i]<<" "; cout<<endl;
		cout<<"Case #"<<cnum<<": "<<buy(1,0,P,0)<<endl;
	}
	return 0;
}
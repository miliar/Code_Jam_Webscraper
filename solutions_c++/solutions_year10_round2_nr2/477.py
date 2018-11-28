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
#define FOR(i,p,k) for (int i = p; i <= (int)(k); ++i)
#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> ostream& operator<<(ostream& os, const vector<T>& v) { REP(i,v.size()) os<<'['<<v[i]<<']'; return os; }
#define DEBUG(x) cerr<<#x":"<<(x)<<endl;

int main() {
	int T; cin>>T;
	for (int casenum = 1; casenum <= T; casenum++) {
		int n, k, b, t; cin>>n>>k>>b>>t;
		vector<int> x(n), v(n);
		REP(i,n) cin>>x[i];
		REP(i,n) cin>>v[i];
		int ans = 0, cnt = 0, obs = 0;
		REPD(p,n) {
			if (b-x[p] <= t*v[p]) { cnt++; ans+=obs; }
			else obs++;
			if (cnt == k) break;
		}
		cout<<"Case #"<<casenum<<": ";
		if (cnt == k) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

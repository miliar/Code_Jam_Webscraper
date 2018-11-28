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
		int n, m; cin>>n>>m;
		set<string> memo;
		memo.insert("");
		REP(i,n) {
			string tmp; cin>>tmp;
			tmp+="/";
			REP(j,tmp.size()) {
				if (tmp[j] == '/')
					memo.insert(tmp.substr(0,j));
			}
		}
		int ans = 0;
		REP(i,m) {
			string tmp; cin>>tmp;
			tmp+="/";
			REP(j,tmp.size()) {
				if (tmp[j] == '/') {
					bool result = memo.insert(tmp.substr(0,j)).second;
					if (result) ans++;
				}
			}
		}
		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}
	return 0;
}

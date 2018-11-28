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
#define ALL(x) x.begin(), x.end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) cerr<<*it<<' '; cerr<<endl; }

typedef vector<int> array;

int main() {
	int TC; cin>>TC;
	for (int tc = 1; tc <= TC; tc++) {
		int n; cin>>n;
		char tmp;
		array last(n,0);
		REP(y,n) REP(x,n) {
			cin>>tmp;
			if (tmp=='1') last[y] = x;
		}
		vector<array> cur(1,last), next;
		set<array> memo;
		for (int step = 0; !cur.empty(); step++) {
			REP(i,cur.size()) {
				array& now = cur[i];
				if (memo.count(now)) continue;
				memo.insert(now);
				bool ok = true;
				REP(x,n) {
					if (now[x] > x) {
						ok = false;
						break;
					}
				}
				if (ok) {
					cout<<"Case #"<<tc<<": "<<step<<endl;
					goto NEXT;
				}
				FOR(x,1,n) {
					swap(now[x-1],now[x]);
					next.push_back(now);
					swap(now[x-1],now[x]);
				}
			}	
			cur.swap(next);
			next.clear();
		}
		assert(false);
NEXT:;
	}
	return 0;
}

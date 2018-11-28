#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define INF 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef pair<int, int> PII;
typedef long long i64; 

int main() {
	freopen("c-large.in", "rt", stdin);
	int t,r,k,n;
	cin >> t;
	REP(step,t){
		cin >> r >> k >> n;
		vector<int> a;
		int gi;
		REP(i,n) cin >> gi, a.pb(gi);
		vector<int> b(a.sz, -1);
		vector<i64> m;
		int cur = 0;
		int iter = 0;
		while (b[cur]==-1 && r>0) {
			--r;
			b[cur] = iter;
			++iter;
			i64 cash = 0;
			int tc = cur;
			while (cash+a[cur] <= k) {
			       	cash+=a[cur], cur=(cur+1)%n;
				if (cur==tc) break;
			}
			m.pb(cash);
			if (m.sz>1) m[m.sz-1] += m[m.sz-2];
		}
		int st = b[cur];
		i64 cCash = m[m.sz-1]; if (st > 0) cCash -= m[st-1];
		i64 cl = m.sz-st;
		i64 res = m[m.sz-1];
		res += (r/cl)*cCash;
		if (r%cl > 0) {
			res += m[st+r%cl-1];
		       	if (st > 0) res -= m[st-1];
		}

		cout << "Case #" << (step+1) << ": " << res << endl;
	}
}

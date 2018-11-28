#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

ll tnum;

ll d[(int)1e6];
ll tt[(int)1e6];

int main() {
	cin >> tnum;
	REP(ti,tnum) {
		ll L, t, N, C;
		cin >> L >> t >> N >> C;
		REP(i,C)
			cin >> d[i];
		for (ll i = C; i < N; ++i)
			d[i] = d[i%C];
		ll k = N;
		tt[0] = 2*d[0];
		if (tt[0] > t)
			k = 0;
		for (ll i = 1; i < N; ++i) {
			tt[i] = tt[i-1] + 2*d[i];
			if (tt[i] > t)
				k = min(k, i);
		}
		ll ans = 0;
		for (ll i = 0; i < k; ++i)
			ans += 2*d[i];
		if (k == N) {
			printf("Case #%d: %lld\n", 1LL+ti, ans);
			continue;
		}
		if (k == 0) {
			ans += t;
			d[k] -= t/2;
		} else {
			ans += (t-tt[k-1]);
			d[k] -= (t-tt[k-1])/2;
		}
		sort(d+k, d+N, greater<ll>());
		for (ll i = k; i < N; ++i) {
			if (L) {
				ans += d[i];
				--L;
			} else
				ans += 2*d[i];
		}
		printf("Case #%lld: %lld\n", 1LL+ti, ans);

	}
	return 0;
}
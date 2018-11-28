/*
 * C.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
const long double PI = (2.0 * acos(0.0));

ll cum[2002];
ll ind[1001];
ll ind2[1001];
ll tt[1001];
bool vis[1001];

int main() {
#ifndef ONLINE_JUDGE
	//freopen("1.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	freopen("1.txt", "wt", stdout);
#endif
	ll N;
	cin >> N;
	rep(K,N) {
		ll r, k, n, x;
		//scanf("%d%d%d", &r, &k, &n);
		cin >> r >> k >> n;
		cum[0] = 0;
		rep(i,n)
			cin >> x, cum[i + 1] = cum[i] + x, cum[i + n + 1] = x;
		for (ll i = n + 1; i - n - 1 < n; ++i)
			cum[i] += cum[i - 1];
		ll j;
		rep(i,n) {
			for (j = i + 1; j - i - 1 < n && cum[j] - cum[i] <= k; ++j)
				;
			ind[i] = j - 2;
		}
		ll cnt = 0, t = 1;
		tt[0] = 0;
		mem(vis,0);
		ll kk = 0;
		while (!(vis[kk])) {
			cnt += cum[ind[kk] + 1] - cum[kk];
			vis[kk] = 1;
			ind2[kk] = t;
			kk = (ind[kk] + 1) % n;
			tt[t++] = cnt;
		}
		if (r + 1 <= t)
			//printf("Case #%d: %d\n", K + 1, tt[r]);
			cout << "Case #" << K + 1 << ": " << tt[r] << "\n";
		else {
			ll a = tt[t - 1];
			r -= (t - 1);
			ll tt1 = tt[ind2[kk] - 1], tt2 = tt[t - 1];
			ll t1 = ind2[kk] - 1, t2 = t - 1;
			ll c = r / (t2 - t1), m = r % (t2 - t1);
			/*printf("Case #%d: %d\n", K + 1, a + (tt2 - tt1) * c + tt[m + t1]
			 - tt[t1]);*/
			cout << "Case #" << K + 1 << ": " << a + (tt2 - tt1) * c + tt[m
					+ t1] - tt[t1] << "\n";
		}
	}

	return 0;
}

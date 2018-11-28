#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

ll a[40], b[40];

ll pot(ll a, int b) {
	ll res = 1;
	while (b--) {
		res *= a;
		res %= 1000;
	}
	return res;
}

ll comb(ll n, ll k) {
	ll res = 1;
	for (ll i = 1; i <= k; i++) {
		res = res*(n-k+i)/i;
	}
	return res%1000;
}

int main() {
	int C;
	cin >> C;
	REP(c, C) {
		int x;
		cin >> x;
		ll res = 0;
		for (int k = 0; k <= x; k += 2) {
			ll cal = 2*pot(5, k/2)*pot(3, x-k);
			cal *= comb(x, k);
			cal %= 1000;
			res = (res+cal)%1000;
		}
		res--; res %= 1000;
		cout << "Case #" << c+1 << ": " << setfill('0') << setw(3) << res << endl;
	}
	return 0;
}

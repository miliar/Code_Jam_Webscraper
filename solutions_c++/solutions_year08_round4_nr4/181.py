#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()

bool _free[111];
int a[111];
int k;
string s;
int ans;

void check() {
	int pos;
	string ss = s;
	
	REP(i, ss.size()) {
		if (i % k == 0) pos = i;
		ss[i] = s[pos + a[i % k]];
	}
	int res = 1;
	FOR(i, 1, ss.size() - 1) if (ss[i] != ss[i- 1]) {
		res++;
	}
//	cout << ss << " " << res << endl;
	ans <?= res;
}

void duyet(int i) {
	if (i == k) {
		check();
		return;
	}
	REP(j, k) if (_free[j]) {
		_free[j] = false;
		a[i] = j;
		duyet(i + 1);
		_free[j] = true;
	}
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		cin >> k;
		cin >> s;
		ans = s.size();
		memset(_free, true, sizeof(_free));
		duyet(0);
		cout << ans << endl;
	}
	return 0;
};


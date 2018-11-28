#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

typedef long long LL;
typedef vector<LL> vi;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

vi a;


LL sum(int q, int n) {
	int N = sz(a);

	if( q+n-1 < N ) {
		if(q == 0)
			return a[n-1];
		else
			return a[q+n-1] - a[q-1];
	} else {
		return sum(q,N-q) + sum(0,n-(N-q));
	}
}

bool ok(int q, int n, LL k) {
	int N = sz(a);

	if( n == N ) {
		return a.back() <= k;
	} else {
		return sum(q,n) <= k;
	}
}

LL next_ride(int& q, int k) {
	int N = sz(a);

	if(ok(q, N, k))
		return (LL)a.back();

	int lo = 1, hi = N;
	while( hi-lo > 1 ) {
		int mid = (lo+hi)/2;

		if( ok(q, mid, k) )
			lo = mid;
		else
			hi = mid;
	}

	LL eu = sum(q,lo);

	q += lo;
	q %= N;

	return eu;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T; cin >> T;
	for(int t = 1; t<=T; ++t) {

		int R, k, N;
		cin >> R >> k >> N;

		a.clear(); a.resize(N);
		for(int i = 0; i < N; ++i) {
			int g; cin >> g;
			a[i] = i ? a[i-1]+g : g;
		}

		LL euros = 0;
		int q = 0;

		for(int i = 0; i < R; ++i) {
			euros += next_ride(q, k);
		}

		cout << "Case #" << t << ": " << euros << "\n";
	}

	return 0;
}

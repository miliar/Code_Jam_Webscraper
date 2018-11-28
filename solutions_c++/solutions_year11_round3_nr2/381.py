//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cassert>
using namespace std;

typedef vector<long long> vi;
typedef pair<long long, int> pli;
typedef long long ll;

int main() {
	int tc;
	cin >> tc;
	for (int cn = 1; cn <= tc; ++cn) {
		ll l, t, n, c;
		cin >> l >> t >> n >> c;
		vi a(c);
		for (int i = 0; i < c; ++i)
			cin >> a[i];
		vi dists(n);
		ll tt = t * 2;
		long long sum = 0;
		vector<pli> tos;
		for (int i = 0; i < n; ++i) {
			dists[i] = a[i % c] * 4;
			sum += dists[i];
			ll diff = min(tt, dists[i]);
			tt -= diff;
			dists[i] -= diff;
			tos.push_back(pli(dists[i], tt));
		}
		//cout << l << " " << t << " " << n << " " << c << endl;
		//cout << "sumbef " << sum << endl;
		sort(tos.rbegin(), tos.rend());
		for (int i = 0; i < l && i < tos.size(); ++i) {
			sum -= tos[i].first / 2;
		}
		assert(sum % 2 == 0);
		cout << "Case #" << cn << ": " << sum / 2 << endl;
	}
	return 0;
}

#include <algorithm>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<ld> pt;

template<class T>
T gcd(T a, T b) {
	T t;
	while (b) {
		t = b;
		b = a%b;
		a = t;
	}
	return a;
}

int main() {
	int num_tests; cin >> num_tests;
	for (int test = 1; test <= num_tests; ++test) {
		// get inputs
		int c; ld d; cin >> c >> d;
		vector<ld> pos;
		for (int i = 0; i < c; ++i) {
			ld p; int v; cin >> p >> v;
			for (int j = 0; j < v; ++j) {
				pos.push_back(p);
			}
		}
		sort(pos.begin(), pos.end());
		// binary search on time
		ld tol = 1e-8;
		ld h = 1e13;
		ld l = 0;
		while (h - l >= tol) {
			ld m = (l + h)/2;

			// see if this is possible
			bool possib = true;
			ld boundary = pos[0] - m - 1;
			for (int i = 0; i < (int) pos.size(); ++i) {
				if (boundary < pos[i]) {
					boundary = max(boundary, pos[i] - m) + d;
				} else if (boundary > pos[i]) {
					if (boundary - pos[i] < m) {
						boundary = boundary + d;
					} else {
						possib = false;
						break;
					}
				} else {
					boundary = boundary + d;
				}
			}

			// do binary search logic
			if (possib) {
				h = m;
			} else {
				l = m;
			}
		}
		cout << "Case #" << test << ": " << ((l + h)/2) << endl;
	}
}


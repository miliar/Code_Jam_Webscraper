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
		int n; cin >> n;
		string matrix[n];
		ld total[n], wp[n], owp[n], oowp[n];
		for (int i = 0; i < n; ++i) {
			cin >> matrix[i];
			total[i] = 0.0;
			for (int j = 0; j < n; ++j) {
				if (matrix[i][j] != '.')
					total[i] += 1;
			}
		}
		// wp
		for (int i = 0; i < n; ++i) {
			assert((int) matrix[i].length() == n);
			int wins = 0;
			for (int j = 0; j < n; ++j) {
				if (matrix[i][j] == '.')
					continue;
				if (matrix[i][j] == '1')
					++wins;
			}
			wp[i] = ld(wins)/total[i];
		}
		// owp
		for (int i = 0; i < n; ++i) {
			ld curr = 0.0;
			for (int j = 0; j < n; ++j) {
				if (matrix[i][j] != '.') {
					curr += (wp[j]*total[j] - ((matrix[i][j] == '0') ? 1 : 0))/(total[j] - 1.0);
				}
			}
			owp[i] = curr/total[i];
		}
		// oowp
		for (int i = 0; i < n; ++i) {
			ld curr = 0.0;
			for (int j = 0; j < n; ++j) {
				if (matrix[i][j] != '.') {
					curr += owp[j];
				}
			}
			oowp[i] = curr/total[i];
		}
		// output answer
		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < n; ++i) {
			cout << ld(0.25)*wp[i] + ld(0.50)*owp[i] + ld(0.25)*oowp[i] << endl;
		}
	}
}


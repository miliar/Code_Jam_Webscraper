#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cassert>

#define vv vector
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define in cin
#define out cout
#pragma warning(disable: 4996)

using namespace std;

int ans;
vv<int> a;

void go(int pos = 0, int sean_sum = 0, int sean_count = 0, int sean_xor_sum = 0, int patrick_xor_sum = 0) {
	if (pos == a.size()) {
		if (sean_xor_sum == patrick_xor_sum && sean_count != a.size()) {
			ans = max(ans, sean_sum);
		}
	} else {
		go(pos + 1, sean_sum + a[pos], sean_count + 1, sean_xor_sum ^ a[pos], patrick_xor_sum);
		go(pos + 1, sean_sum, sean_count, sean_xor_sum, patrick_xor_sum ^ a[pos]);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testcases;
	in >> testcases;

	for (int test = 0; test < testcases; ++test) {
		int n; in >> n;
		a.assign(n, 0);
		for (int i = 0; i < n; ++i) {
			in >> a[i];
		}

		ans = 0;
		go();

		out << "Case #" << test + 1 << ": ";
		if (ans == 0)
			out << "NO";
		else
			out << ans;
		out << endl;
	}

	return 0;
}
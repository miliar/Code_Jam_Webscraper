#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[100];

bool CouldBe(int sum, int border, int &s) {
	bool can = false;
	for (int i = 0; i <= 10; ++i) {
		for (int j = i; j <= i + 2; ++j) {
			for (int k = i; k <= j; ++k) {
				if (i + j + k != sum) {
					continue;
				}
				int delta = j - i;
				if (delta <= 1) {
					if (j >= border) {
						return true;
					}
				} else {
					if (s && j >= border) {
						can = true;
					}
				}
			}
		}
	}

	if (can) {
		--s;
	}
	return can;
}

int solve(int n, int s, int p) {
	int ans = 0;
	sort(a, a + n);
	for (int i = n - 1; i >= 0; --i) {
		ans += CouldBe(a[i], p, s);
	}
	return ans;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		int n, s, p;
		cin >> n >> s >> p;
		for (int j = 0; j < n; ++j) {
			cin >> a[j];
		}
		cout << solve(n, s, p) << endl;
	}
	return 0;
}
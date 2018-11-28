#include <iostream>
#include <cstdio>

using namespace std;

const int N = 1e4 + 10;
int d[N], len[N], n, D, dp[N];

void sol (int test_number) {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> d[i] >> len[i];
	}	
	for (int i = 0; i < n; ++i) {
		dp[i] = 0;
	}

	cin >> D;

	dp[0] = d[0];
	bool can = false;
	for (int i = 0, j = 0; i < n; ++i) {
		if (d[i] + dp[i] >= D) {
			can = true;
		}
		if (j <= i) {
			j = i + 1;
		}
		for (; j < n && d[j] - d[i] <= dp[i]; ++j) {
			dp[j] = min(len[j], d[j] - d[i]);
		}
	}
	cout << "Case #" << test_number + 1 << ": " << (can ? "YES" : "NO") << endl;
}

int main () {
//	freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tests_count;
	cin >> tests_count;
	for (int i = 0; i < tests_count; ++i) {
		sol(i);
	}
	return 0;
}
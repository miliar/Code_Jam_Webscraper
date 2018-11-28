#include <algorithm>
#include <cassert>
#include <complex>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
typedef complex<double> pt;

int D, I, M, N;
int a[256];

int cache[512][512][2];
int dp(int before, int index, int du) {
	// base case
	if (index == N)
		return 0;
	int ret = cache[before][index][du];
	// seen before
	if (ret != -1)
		return ret;
	// recursive call
	// delete
	ret = min(dp(before, index + 1, 0), dp(before, index + 1, 1)) + D;
	// change
	for (int i = max(0, before - M); i <= min(255, before + M); i++) {
		ret = min(ret, dp(i, index + 1, 0) + abs(a[index] - i));
		ret = min(ret, dp(i, index + 1, 1) + abs(a[index] - i));
	}
	// insert
	int low = (du == 0) ? max(0, before - M) : before;
	int high = (du == 1) ? min(255, before + M) : before;
	for (int i = low; i <= high; i++) {
		if (i != before)
			ret = min(ret, dp(i, index, du) + I);
	}
//cout << before << ", " << index << ", " << du << ", N = " << N << endl;
	return cache[before][index][du] = ret;
}

int main() {
	int num_tests; cin >> num_tests;
	for (int test = 1; test <= num_tests; test++) {
		// clean up
		memset(cache, -1, sizeof(cache));
		// get input
		cin >> D >> I >> M >> N;
		for (int i = 0; i < N; i++)
			cin >> a[i];
		// output answer
		int ans = min(dp(a[0], 0, 0), dp(a[0], 0, 1));
		for (int i = 0; i <= 255; i++) {
			ans = min(ans, dp(i, 0, 0));
			ans = min(ans, dp(i, 0, 1));
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
}


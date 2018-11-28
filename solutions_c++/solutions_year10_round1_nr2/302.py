#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int data[128];
int D, I, M, N;

int cc[128][300];
int dp(int at, int val) {
	if(at == N) return 0;
	int& ret = cc[at][val];
	if(ret >= 0) return ret;
	if(abs(val - data[at]) <= M) return (ret = dp(at+1, data[at]));
	// delete
	ret = dp(at+1, val) + D;
	// insert
	if(val > data[at]) { // reduce by M, val - M >= 0
		ret = min(ret, dp(at, val-M) + I);
	} else { // increase by M, val + M <= 255
		ret = min(ret, dp(at, val+M) + I);
	}
	// modify
	for(int n = max(0, val - M); n <= min(255, val + M); ++n) {
		ret = min(ret, dp(at+1, n) + abs(n - data[at]));
	}
	return ret;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> D >> I >> M >> N;
		for(int i = 0; i < N; ++i) cin >> data[i];
		for(int i = 0; i <= N; ++i)
			for(int v = 0; v <= 300; ++v)
				cc[i][v] = -1;
		int ans = dp(1, data[0]);
		// skip i
		for(int i = 0; i < N; ++i) {
			// modify the first number
			// ans = min(ans, dp(i+1, data[i]) + i * D);
			for(int n = 0; n <= 255; ++n) {
				ans = min(ans, dp(i+1, n) + i * D + abs(n - data[i]));
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}


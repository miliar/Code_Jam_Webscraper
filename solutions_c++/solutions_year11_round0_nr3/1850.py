#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

long long add(long long A, long long B) {
	// add them using "wrong" binary
	long long C = 0;
	int p = 0;
	while (A > 0 || B > 0) {
		if (((A&1) + (B&1)) & 1) {
			C |= (1 << p);
		}
		p++;
		A >>= 1; B >>= 1;
	}
	return C;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int N; cin >> N;
		long long tot = 0;
		long long totR = 0;
		int smallest = 1 << 30;
		for (int i = 0; i < N; i++) {
			int val; cin >> val;
			tot = add(tot, val);
			totR += val;
			smallest = min(smallest, val);
		}
		cout << "Case #" << t+1 << ": ";
		if (tot == 0) {
			cout << totR - smallest << "\n";
		} else {
			cout << "NO\n";
		}
	}
	return 0;
}
#include <iostream>

using namespace std;

#define N 101

int n, p;
int t[N];

int notsurprise(int t) {
	for (int v1 = p; v1 <= 10; v1++) {
		if (v1 > t) break;
		for (int v2 = v1; v2 >= 0; v2--) {
			if (v1 - v2 > 1) break;
			for (int v3 = v2; v3 >= 0; v3--) {
				if (v1 - v3 > 1) break;
				if (v1 + v2 + v3 == t) return 1;
			}
		}		
	}
	return 0;
}

int surprise(int t) {
	for (int v1 = p; v1 <= 10; v1++) {
		if (v1 > t) break;
		for (int v2 = v1; v2 >= 0; v2--) {
			if (v1 - v2 > 2) break;
			for (int v3 = v2; v3 >= 0; v3--) {
				if (v1 - v3 > 2) break;
				if (v1 + v2 + v3 == t) return 1;
			}
		}		
	}
	return 0;
}

int solve(int i, int s) {
	if (i >= n) return 0;

	if (s == 0) { //no surprises
		return notsurprise(t[i]) + solve(i + 1, s);
	} else if (n - i < s) {
		return surprise(t[i]) + solve(i + 1, s - 1);
	} else {
		return max(notsurprise(t[i]) + solve(i + 1, s), surprise(t[i]) + solve(i + 1, s - 1));
	}
}

int main() {
	int ntc; cin >> ntc;
	for (int tc = 1; tc <= ntc; tc++) {
		int s;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i++) cin >> t[i];
		cout << "Case #" << tc << ": " << solve(0, s) << endl;
	}

	return 0;
}

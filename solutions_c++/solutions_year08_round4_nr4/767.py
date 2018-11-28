#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

typedef vector<int> vi;

int apply(string &S, vi &p, int k) {
	char d = 0;
	int sl = S.length(), rl = 0;
	for (int i = 0; i < sl; i += k) {
		for (int j = 0; j < k; j++) {
			char c = S[i + p[j]];
			if (c != d) {
				rl += 1;
				d = c;
			}
		}
	}
	return rl;
}

void solve(void) {
	int k; string S;
	cin >> k >> S;
	int m = S.length() + 1;
	vi p; for (int i = 0; i < k; i++) p.push_back(i);
	do {
		int rs = apply(S, p, k);
		if (rs < m) m = rs;
	} while (next_permutation(p.begin(), p.end()));
	cout << m;
}

int main(void) {
	int nc; cin >> nc;
	for (int ic = 1; ic <= nc; ic++) {
		cout << "Case #" << ic << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

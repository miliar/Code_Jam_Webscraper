#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int case_nr, T;

	cin >> T;

	for (case_nr=1; case_nr<=T; case_nr++) {
		cout << "Case #" << case_nr << ": ";

		int N;
		long long L, H;
		cin >> N >> L >> H;
		vector<long long> f(N);

		for (int i=0; i<N; i++) {
			cin >> f[i];
		}

		bool found = false;
		for (long long val=L; val<=H; val++) {
			bool ok = true;
			for (int i=0; i<N; i++) {
				if (val % f[i] != 0 && f[i] % val != 0) {
					ok = false;
					break;
				}
			}

			if (ok) {
				cout << val << "\n";
				found = true;
				break;
			}
		}

		if (!found)
			cout << "NO\n";
	}
}

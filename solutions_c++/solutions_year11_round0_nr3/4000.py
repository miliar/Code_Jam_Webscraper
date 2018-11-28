#include <algorithm>
#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <cmath>

using namespace std;


void doit() {
	int N;
	cin >> N;

	unsigned long candy[N];

	for (int i = 0; i < N; i++) {
		cin >> candy[i];
	}

	unsigned long long maxs = 0;

	//cout <<(1UL <<N);

	for (unsigned long i = 1; i < (1UL << N) -1; i++) {
		unsigned long s = 0;
		unsigned long long sreal = 0;
		unsigned long p = 0;
		for (int j = 0; j < N; j++) {
			if ((i & (1 << j)) == 0) { // assign to sean
				s ^= candy[j];
				sreal += candy[j];
			} else {
				p ^= candy[j];
			}
			//cout << s << p << '\n';
		}
		if (s==p) {
			maxs = max(maxs, sreal);
		}
	}

	if (maxs != 0) {
		cout << maxs << '\n';
	} else {
		cout << "NO\n";
	}
}

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cout << "Case #" << i + 1 << ": ";
		doit();
	}

	return 0;
}

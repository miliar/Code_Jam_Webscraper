#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int> vi;

int main(void) {
	int N; cin >> N;
	for (int x = 1; x <= N; x++) {
		int P, K, L; cin >> P >> K >> L;
		vi F(L);
		for (int l = 0; l < L; l++) {
			cin >> F[l];
		}
		sort(F.begin(), F.end());
		int T = 0, i = L - 1;
		for (int p = 1; p <= P && i >= 0; p++) {
			for (int k = 0; k < K && i >= 0; k++) {
				T += F[i] * p;
				i--;
			}
		}
		cout << "Case #" << x << ": ";
		if (i >= 0) {
			cout << "Impossible";
		} else {
			cout << T;
		}
		cout << endl;	
	}
	return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	long long case_nr, N, P, K, L;
	vector <long long> freqs;

	cin >> N;

	for (case_nr=1; case_nr<=N; case_nr++) {
		cin >> P >> K >> L;

		freqs.resize(L);

		for (long long i=0; i<L; i++)
			cin >> freqs[i];

		sort(freqs.rbegin(), freqs.rend());

		long long ret=0;
		for (long long i=0; i<L; i++) {
			ret+=freqs[i]*(i/K+1);
		}

		assert(P*K>=L);

		cout << "Case #" << case_nr << ": " << ret << endl;
	}
}

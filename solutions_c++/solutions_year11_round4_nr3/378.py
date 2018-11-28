#include <iostream>
#include <vector>
using namespace std;

bool composite[1000001];
vector<long long> primes;

int main() {
	for (int i = 2; i <= 1000000; i++) {
		if (composite[i]) continue;
		for (int j = 2*i; j <= 1000000; j += i) composite[j] = true;
		primes.push_back(i);
	}
	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int spread = 1;
		
		long long N;
		cin >> N;
		for (vector<long long>::iterator i = primes.begin(); i != primes.end() && (*i)*(*i) <= N; i++) {
			long long cur = (*i);
			int logg = 0;
			while (cur <= N) {
				cur *= (*i);
				logg++;
			}
			spread += logg-1;
		}
		cout << "Case #" << t+1 << ": " << (N == 1 ? 0 : spread) << '\n';
	}
	return 0;
}

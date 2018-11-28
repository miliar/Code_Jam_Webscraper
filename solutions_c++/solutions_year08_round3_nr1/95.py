#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	for(int nacho = 1; nacho <= N; nacho++) {
		int P, K, L;
		cin >> P >> K >> L;
		vector<long long> cant(L);
		for(int i = 0; i < L; i++)
			cin >> cant[i];
		sort(cant.rbegin(), cant.rend());

		if(L > P*K) {
			cout << "Case #" << nacho << ": Impossible" << endl;
			continue;
		}
		
		long long sol = 0;
		for(int i = 0; i*K < L; i++)
			for(int j = i*K; j < min(i*K+K, L); j++)
				sol += cant[j]*(i+1);
		
		cout << "Case #" << nacho << ": " << sol << endl;
	}
	
	return 0;
}

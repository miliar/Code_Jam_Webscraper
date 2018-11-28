
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T, N;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> N;
		vector<int> P(N);
		for(int i = 0; i < N; i++) cin >> P[i];
		for(int i = N-1; i >= 0; i--) if(P[i] == i+1) N--;
		cout << "Case #" << t << ": " << N << endl;
	}
}


#include <iostream>
#include <vector>
using namespace std;


int solve(vector<int> C) {
	int S = 0, S2 = 0, min = 1000000000;
	for(int i = 0; i < C.size(); i++) {
		S ^= C[i];
		S2 += C[i];
		if(C[i] < min) min = C[i];
	}
	if(S) return -1;
	return S2 - min;
}

int main() {
	int T, N;

	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> N;
		vector<int> C(N);
		
		for(int i = 0; i < N; i++) cin >> C[i];
		int r = solve(C);
		cout << "Case #" << t << ": ";
		if(r < 0) cout << "NO"; else cout << r;
		cout << endl;

	}


}

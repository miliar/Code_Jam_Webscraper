#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		int N, K; // switches, snaps
		cin >> N >> K;
		vector<bool> switches(N, false);
		for(int j = 0; j < K; j++) {
			int k = 0;			
			do{
				switches[k] = !switches[k];
				k++;
			} while(k < N && !switches[k-1]);
		}

		bool state = true;
		for(int l = 0; l < N; l++) {
			if(state &= switches[l]);
			else break;
		}

		cout << "Case #" << i << ": " << (state ? "ON" : "OFF") << endl;
	}
	return 0;
}
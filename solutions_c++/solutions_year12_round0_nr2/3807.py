#include<iostream>
#include<string>

using namespace std;

int main() {
	int K;
	cin >> K >> ws;
	for (int k = 1; k <= K; k++) {
		cout << "Case #" << k << ": ";

		int N, S, P, number = 0;
		cin >> N >> S >> P;
		for (int i = 0; i < N; i++) {
			int t;
			cin >> t;
			t -= P;
			if (t < 0) continue;
			if (2*P-2 <= t) number++; //this one can have a high enough score
			else if (S  &&  2*P-4 <= t) {S--; number++; } //this one can have a high enouch score if it's suprising
		}

		cout << number << endl;

	}

}

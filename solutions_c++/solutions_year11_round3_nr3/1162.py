#include <iostream>
using namespace std;

int main() {
	int numTests;
	cin >> numTests;

	for (int t = 1; t <= numTests; t++) {
		int numPlayers;
		int low;
		int high;

		cin >> numPlayers >> low >> high;

		int* freqs = new int[numPlayers];
		for (int i = 0; i < numPlayers; i++) {
			cin >> freqs[i];
		}

		int freq;
		bool isHarmonic = true;
		for (freq = low; freq <= high; freq++) {
			isHarmonic = true;
			for (int i = 0; i < numPlayers; i++) {
				if ((freq % freqs[i] != 0) && (freqs[i] % freq != 0)) {
					isHarmonic = false;
					break;
				}
			}

			if (isHarmonic) {
				break;
			}
		}

		printf("Case #%d: ", t);
		if (isHarmonic) {
			printf("%d\n", freq);
		}
		else {
			printf("NO\n");
		}
	}
}

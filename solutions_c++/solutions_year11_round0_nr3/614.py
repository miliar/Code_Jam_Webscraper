#include <iostream>

using namespace std;

int main() {
	int ncasos;
	int N, x;
	cin >> ncasos;
	for (int caso = 1; caso <= ncasos; caso++) {
		cin >> N;
		int total = 0, minim = 999999999, bitxor = 0;
		for (int i = 0; i < N; i++) {
			cin >> x;
			total += x;
			if (x < minim) minim = x;
			bitxor = bitxor xor x;
		}
		cout << "Case #" << caso << ": ";
		if (bitxor) {
			cout << "NO";
		} else {
			cout << total-minim;
		}
		cout << endl;
	}
	return 0;
}

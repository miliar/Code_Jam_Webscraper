#include <iostream>

using namespace std;

int main() {
	int ncasos, N;
	int x, mispl;
	cin >> ncasos;
	for (int caso = 1; caso <= ncasos; caso++) {
		cin >> N;
		mispl = 0;
		for (int i = 1; i <= N; i++) {
			cin >> x;
			if (x != i) mispl++;
		}
		cout << "Case #" << caso << ": " << mispl << endl;
	}
	return 0;
}

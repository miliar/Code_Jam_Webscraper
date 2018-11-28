#include <iostream>
#include <string>

using namespace std;

string R[500];
int P[500];
int nexto[500], nextb[500];

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> R[i] >> P[i];
		}
		nexto[N] = nextb[N] = 1;
		for (int i = N-1; i >= 0; i--) {
			nexto[i] = nexto[i+1];
			nextb[i] = nextb[i+1];
			if (R[i] == "O") {
				nexto[i] = P[i];
			} else {
				nextb[i] = P[i];
			}
		}
		int poso = 1, posb = 1, time = 0, i = 0;
		while (i < N) {
			if (R[i] == "O") {
				if (poso == P[i]) {
					i++;
				} else if (poso < P[i]) {
					poso++;
				} else if (poso > P[i]) {
					poso--;
				}
				if (posb < nextb[i]) {
					posb++;
				} else if (posb > nextb[i]) {
					posb--;
				}
			} else {
				if (posb == P[i]) {
					i++;
				} else if (posb < P[i]) {
					posb++;
				} else if (posb > P[i]) {
					posb--;
				}
				if (poso < nexto[i]) {
					poso++;
				} else if (poso > nexto[i]) {
					poso--;
				}
			}
			time++;
		}
		cout << "Case #" << t+1 << ": " << time << endl;
	}
	return 0;
}

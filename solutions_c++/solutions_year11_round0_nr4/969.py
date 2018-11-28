#include <iostream>

using namespace std;

double P[1002][1002];
double cum[1002][1002];
double E[1002];

int main() {
	for (int n = 0; n <= 1000; n++) {
		for (int k = 0; k <= 1000; k++) {
			if (k > n) P[n][k] = 0;
			else if (n == 0) P[n][k] = 1;
			else {
				P[n][k] = 0;
				if (k > 0) P[n][k] += P[n-1][k-1] / n;
				if (n >= 2) P[n][k] += cum[n-2][k] / n;
			}

			cum[n][k] = ((n == 0) ? 0 : cum[n - 1][k]) + P[n][k];
		}
	}

	E[0] = 0;
	for (int k = 1; k <= 1000; k++) {
		E[k] = 1;
		for (int i = 1; i <= k; i++) {
			E[k] += P[k][i] * E[k - i];
		}
		E[k] /= (1 - P[k][0]);
	}

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		int counter = 0;
		for (int i = 0 ; i < N; i++) {
			int c;
			cin >> c;
			if (c != i + 1) counter++;
		}
		cout << "Case #" << t << ": " << E[counter] << endl;
	}

	return 0;
}

#include <iostream>

using namespace std;

int main() {

	int T, N, i, j;
	int PO, PB, TO, TB, TM;
	int P;
	char R;

	cin >> T;
	for (i = 1; i <= T; i++) {
		cin >> N;
		PO = PB = 1;
		TO = TB = 0;
		for (j = 0; j < N; j++) {
			cin >> R >> P;
			if (R == 'O') {
				TM = TO + abs(PO - P) + 1;
				if (TM <= TB) TO = TB + 1; else TO = TM;
				PO = P;
			} else {
				TM = TB + abs(PB - P) + 1;
				if (TM <= TO) TB = TO + 1; else TB = TM;
				PB = P;
			}
		}
		cout << "Case #" << i << ": " << max(TB, TO) << endl;
	}
	return 0;
}


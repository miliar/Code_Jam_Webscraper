#include <iostream>
using namespace std;

int vinePos[10000];
int vineSlack[10000];

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		int curVine;
		int maxDist = 0;
		bool bad = false;
		for (int i = 0; i < N; i++) {
			cin >> vinePos[i];
			cin >> vineSlack[i];
			if (i == 0) {
				vineSlack[0] = vinePos[0];
				curVine = 0;
				if (vinePos[i] + vineSlack[i] > maxDist) {
					maxDist = vinePos[i] + vineSlack[i];
				}
				continue;
			}
			while (curVine < i && vineSlack[curVine] < vinePos[i] - vinePos[curVine]) {
				curVine++;
			}
			if (curVine == i) {
				bad = true;
			}
			if (vinePos[i] - vinePos[curVine] < vineSlack[i]) {
				vineSlack[i] = vinePos[i] - vinePos[curVine];
			}
			if (vinePos[i] + vineSlack[i] > maxDist) {
				maxDist = vinePos[i] + vineSlack[i];
			}
		}
		int D;
		cin >> D;
		if (!bad && D <= maxDist) {
			cout << "Case #" << t << ": YES\n";
		} else {
			cout << "Case #" << t << ": NO\n";
		}
	}
	return 0;
}

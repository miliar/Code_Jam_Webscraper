#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int T, N, B;
	char R;
	int cA, cB;
	int pA, pB;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i+1 << ": ";
		cin >> N;
		cA = cB = 0;
		pA = pB = 1;
		bool entra = true;
		int ultMov = 0;
		char ultMovC = '0';
		while(N--) {
			cin >> R >> B;
			if(entra) {
				ultMovC = R == 'O' ? 'B' : 'O';
				entra = false;
			}
			if(R == 'O') {
				if(ultMovC == 'B') {
					if(abs(pA-B) < ultMov) {
						cA += ultMov + 1;
						ultMov = 1;
					} else {
						cA += abs(pA-B) + 1;
						ultMov = abs(pA-B)-ultMov+1;
					}
					
				} else {
					cA += abs(pA-B) + 1;
					ultMov += abs(pA-B) + 1;
				}
				pA = B;
				ultMovC = 'O';
			} else {
				if(ultMovC == 'O') {
					if(abs(pB-B) < ultMov) {
						cB += ultMov + 1;
						ultMov = 1;
					} else {
						cB += abs(pB-B) + 1;
						ultMov = abs(pB-B)-ultMov+1;
					}
				} else {
					cB += abs(pB-B) + 1;
					ultMov += abs(pB-B) + 1;
				}
				pB = B;
				ultMovC = 'B';
			}
		}
		cout << max(cA, cB) << endl;
	}
	return 0;
}

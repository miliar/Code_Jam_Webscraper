#include <iostream>
using namespace std;

int L, D, N;

char words[10000][20];

int main() {
	cin >> L >> D >> N;
	for (int i = 0; i < D; i++) cin >> words[i];
	for (int i = 0; i < N; i++) {
		char pattern[1000];
		cin >> pattern;
		int pos = 0;
		bool charUsed[256];
		bool alive[10000];
		for (int j = 0; j < D; j++) alive[j] = true;
		for (int j = 0; j < L; j++) {
			for (int k = 0; k < 256; k++) charUsed[k] = false;
			if (pattern[pos] == '(') {
				pos++;
				while (pattern[pos] != ')') {
					charUsed[pattern[pos]] = true;
					pos++;
				}
			}
			else charUsed[pattern[pos]] = true;
			pos++;
			for (int k = 0; k < D; k++) if (!charUsed[words[k][j]]) alive[k] = false;
		}
		int num = 0;
		for (int j = 0; j < D; j++) if (alive[j]) num++;
		cout << "Case #" << (i+1) << ": " << num << endl;
	}
}

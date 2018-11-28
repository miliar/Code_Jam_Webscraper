/**
 * magicka.cpp
 *
 * @date May 7, 2011
 * @author Arpan
 **/

#include <iostream>
#include <vector>

//#define DEBUG

using namespace std;

char combos[36][3];
char oppos[28][2];

bool isCombo(char *seq, int& n, char elem, int C) {
	for(int c = 0; c < C; c++) {
		if( (elem == combos[c][0] && seq[n-1] == combos[c][1])
		 || (elem == combos[c][1] && seq[n-1] == combos[c][0])) {
			seq[n-1] = combos[c][2];
			return true;
		}
	}
	return false;
}

bool isOppo(char *seq, int& n, char elem, int D) {
	bool clearFlag = false;
	for(int d = 0; d < D && !clearFlag; d++) {
		bool flag = false;
		char op;
		if(elem == oppos[d][0]) {
			flag = true;
			op = oppos[d][1];
		}
		else if(elem == oppos[d][1]) {
			flag = true;
			op = oppos[d][0];
		}

		if(flag) {
			// check if op is present in current seq
			for(int i = 0; i < n; i++) {
				if(seq[i] == op) {
					clearFlag = true;
					break;
				}
			}
		}
	}

	if(clearFlag) {
		n = 0;
		return true;
	}
	else {
		seq[n] = elem;
		n++;
		return false;
	}
}

void printSeq(char *seq, int n) {
	cout << "[";
	if(n > 0) {
		for(int i = 0; i < (n-1); i++) {
			cout << seq[i] << ", ";
		}
		cout << seq[n-1];
	}
	cout << "]" << endl;
}

int main(int argc, char* argv[]) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int C, D, N;

		cin >> C;
		for(int c = 0; c < C; c++) {
			cin >> combos[c][0] >> combos[c][1] >> combos[c][2];
		}

		cin >> D;
		for(int d = 0; d < D; d++) {
			cin >> oppos[d][0] >> oppos[d][1];
		}

		cin >> N;
#ifdef DEBUG
		cout << N << ':' << endl;
#endif
		char seq[N+1], elem;
		int n = 0;
		for(int i = 0; i < N; i++) {
			cin >> elem;
#ifdef DEBUG
			cout << elem;
#endif
			if(n > 0) {
				// check combos
				if(isCombo(seq, n, elem, C)) {
#ifdef DEBUG
					cout << " [combo]";
#endif
				}
				// check oppos
				else if(isOppo(seq, n, elem, D)) {
#ifdef DEBUG
					cout << " [oppo]";
#endif
				}
			}
			else {
				// get started
				seq[0] = elem;
				n = 1;
			}
#ifdef DEBUG
			cout << " seq(" << n << "): ";
			printSeq(seq, n);
#endif
		}
		seq[n] = '\0';

		cout << "Case #" << t << ": ";
		printSeq(seq, n);
	}
}

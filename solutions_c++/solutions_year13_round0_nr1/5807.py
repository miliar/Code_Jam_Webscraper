#include <iostream>
#include <stdlib.h>
#include <float.h>
#include <math.h>

using namespace std;
#define X 1
#define O 2
#define T 3
#define DOT 4

bool test(char state[4][4], char c) {
	for (int j = 0; j < 4; ++j) {
		int count = 0;
		for (int t = 0; t < 4; ++t) {
			if (state[t][j] == c || state[t][j] == 'T')
				count++;
		}
		if (count == 4)
			return true;
	}
	for (int j = 0; j < 4; ++j) {
		int count = 0;
		for (int t = 0; t < 4; ++t) {
			if (state[j][t] == c || state[j][t] == 'T')
				count++;
		}
		if (count == 4)
			return true;
	}
	int count = 0;
	for (int i = 0; i < 4; ++i) {
		if (state[i][i] == c || state[i][i] == 'T')
			count++;
	}
	if (count == 4)
		return true;
	count = 0;
	for (int i = 0; i < 4; ++i) {
		if (state[3 - i][i] == c || state[3 - i][i] == 'T')
			count++;
	}
	if (count == 4)
		return true;
}

bool full(char state[4][4]) {
	for (int j = 0; j < 4; ++j) {
		for (int t = 0; t < 4; ++t) {
			if (state[t][j] == '.')
				return false;
		}
	}
	return true;
}

int main(int argc, char **argv) {
	int testCount = 0;
	char state[4][4];
	cin >> testCount;
	char dummy;
//	cin >> dummy;
//	cout << dummy;
	for (int i = 0; i < testCount; ++i) {
		for (int j = 0; j < 4; ++j) {
			for (int t = 0; t < 4; ++t) {
				cin >> state[j][t];
//				cout << state[j][t];
			}
//			cout << endl;
//			cin >> dummy;
		}
		bool p1 = test(state, 'X');
		bool p2 = test(state, 'O');
		bool f = full(state);
		if (p1)
			cout << "Case #" << (i + 1) << ": X won" << endl;
		else if (p2)
			cout << "Case #" << (i + 1) << ": O won" << endl;
		else if (f)
			cout << "Case #" << (i + 1) << ": Draw" << endl;
		else
			cout << "Case #" << (i + 1) << ": Game has not completed" << endl;
	}
}

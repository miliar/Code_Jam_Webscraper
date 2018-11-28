#include <iostream>

#define DIM 16

using namespace std;

int solutions[] = {
	0x000F,
	0x00F0,
	0x0F00,
	0xF000,
	0x1111,
	0x2222,
	0x4444,
	0x8888,
	0x1248,
	0x8421
};

string calculate(char* state) {
	int i, x = 0, o = 0, v;
	bool eog = true;
	for (i = 0; i < DIM; ++i) {
		v = (1 << i);
		switch (state[i]) {
			case 'X':
				x |= v;
				break;
			case 'O':
				o |= v;
				break;
			case 'T':
				x |= v;
				o |= v;
				break;
			case '.':
				eog = false;
				break;
		}
	}

	for (i = 0; i < 10; ++i) {
		if ((x & solutions[i]) == solutions[i]) {
			return "X won";
		}
		if ((o & solutions[i]) == solutions[i]) {
			return "O won";
		}
	}
	if (eog) {
		return "Draw";
	}
	return "Game has not completed";
}

int main() {
	int t, i, j;
	char state[DIM];

	cin >> t;

	for (i = 1;  i <= t; ++i) {
		for (j = 0; j < DIM; ++j) {
			cin >> state[j];
		}
		cout << "Case #" << i << ": " << calculate(state) << endl;
	}
}

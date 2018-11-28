#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int i;
	int j;
	char arr[10][10];
	char b[150];
	int f;
	int t;
	int k;

	cin >> t;
	k = 1;

	while (k <= t) {
	f = 3;
	for (i = 0; i < 4; i++) {
		cin >> arr[i];
		getchar ();
	}

	getchar ();

	for (i = 0; i < 4; i++) {
		b['O'] = 0;
		b['X'] = 0;
		b['T'] = 0;
		b['.'] = 0;

		for (j = 0; j < 4; j++) {
			b[arr[i][j]]++;
		}

		if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
			f = 0;
			break;
		} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
			f = 1;
			break;
		} else if (b['.'] > 0) {
			f = 2;
		}
	}

	if (f > 1) {
	for (i = 0; i < 4; i++) {
                b['O'] = 0;
                b['X'] = 0;
                b['T'] = 0;
                b['.'] = 0;

                for (j = 0; j < 4; j++) {
                        b[arr[j][i]]++;
                }

                if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
			f = 0;
			break;
		} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
			f = 1;
			break;
		} else if (b['.'] > 0) {
			f = 2;
		}
        }
	}

	if (f > 1) {
                b['O'] = 0;
                b['X'] = 0;
                b['T'] = 0;
                b['.'] = 0;

                for (j = 0; j < 4; j++) {
                        b[arr[j][j]]++;
                }

                if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
			f = 0;
		} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
			f = 1;
		} else if (b['.'] > 0) {
			f = 2;
		}
        }

	if (f > 1) {
                b['O'] = 0;
                b['X'] = 0;
                b['T'] = 0;
                b['.'] = 0;

                for (j = 0; j < 4; j++) {
                        b[arr[j][3 - j]]++;
                }

                if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
			f = 0;
		} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
			f = 1;
		} else if (b['.'] > 0) {
			f = 2;
		}
        }

	if (f == 0) {
		cout << "Case #" << k << ": O won\n";
	} else if (f == 1) {
		cout << "Case #" << k << ": X won\n";
	} else if (f == 2) {
		cout << "Case #" << k << ": Game has not completed\n";
	} else {
		cout << "Case #" << k << ": Draw\n";
	}

	k++;
	}

	return 0;
}

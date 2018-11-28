#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool check(const vector<string>& a, char c) {
	for (int i = 0; i < 4; ++i) {
		bool found = true;
		for (int j = 0; j < 4; ++j) {
			if (a[i][j] != c && a[i][j] != 'T') {
				found = false;
			}
		}
		if (found) {
			return true;
		}
	}

	for (int i = 0; i < 4; ++i) {
		bool found = true;
		for (int j = 0; j < 4; ++j) {
			if (a[j][i] != c && a[j][i] != 'T') {
				found = false;
			}
		}
		if (found) {
			return true;
		}
	}

	bool found = true;
	for (int i = 0; i < 4; ++i) {
		if (a[i][i] != c && a[i][i] != 'T') {
			found = false;
		}
	}

	if (found) {
		return true;
	}

	found = true;
	for (int i = 0; i < 4; ++i) {
		if (a[i][3 - i] != c && a[i][3 - i] != 'T') {
			found = false;
		}
	}
	if (found) {
		return true;
	}

	return false;

}


int main() {
	int n_tests;
	cin >> n_tests;

	for (int test = 0; test < n_tests; ++test) {
		vector<string> a(4);
		for (int i = 0; i < 4; ++i) {
			cin >> a[i];
		}

		bool has_empty = false;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (a[i][j] == '.') {
					has_empty = true;
				}
			}
		}

		cout << "Case #" << test + 1 << ": ";
		if (check(a, 'X')) {
			cout << "X won" << endl;
		} else if (check(a, 'O')) {
			cout << "O won" << endl;
		} else if (has_empty) {
			cout << "Game has not completed" << endl;
		} else {
			cout << "Draw" << endl;
		}

		{
			string t;
			getline(cin, t);
		}
	}

	return 0;
}

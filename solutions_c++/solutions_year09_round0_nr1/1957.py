#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	fstream fn;
	ofstream fn2;
	int L, D, N;
	vector<string> words;
	vector<bool> fit;
	vector<string> patt;
	string n;
	char row[1000];

	fn.open ("input.txt");
		fn >> L >> D >> N;
		for (int i = 0; i < D; ++i) {
			fn >> row; words.push_back(row);
		}
		for (int i = 0; i < N; ++i) {
			fn >> row; patt.push_back(row);
			cout << row << endl;
		}
	fn.close();

	fn2.open ("C:\output.txt");
	for (int test = 0; test < N; ++test) {
		fn2 << "Case #" << (test + 1) << ": ";
		fit.resize(0);
		for (int i = 0; i < D; ++i) fit.push_back(true);
		int x = 0, y;
		/*do {
			x = patt[test].find("(", x);
			if (x != string::npos) {
				y = patt[test].find(")", x);
				cout << patt[test].substr(x + 1, y - x - 1).c_str() << endl;
				x = y + 1;
			}
		} while (x != -1);(*/
		int c = 0;
		for (int i = 0; i < patt[test].size(); ++i) {
			if (patt[test][i] == '(') {
				// till ')'
				int cl;
				cl = patt[test].find(")", i);
				n = patt[test].substr(i+1, cl - i - 1);
				for (int j = 0; j < D; ++j) {
					if (n.find(words[j][c]) == -1) {
						fit[j] = false;
					}
				}
				i = cl;
			} else {
				for (int j = 0; j < D; ++j) {
					if (words[j][c] != patt[test][i]) {
						fit[j] = false;
					}
				}
			}
			c++;
		}

		c = 0;
		for (int j = 0; j < D; ++j) {
			if (fit[j]) c++;
		}
		cout << c;
		fn2 << c << endl;
	}
	fn2.close();

	system("pause");
	return 0;
}
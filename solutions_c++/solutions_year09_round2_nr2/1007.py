#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	fstream fn;
	ofstream fn2;
	int T;
	fn.open ("input.txt");
	fn2.open ("C:\output.txt");
	fn >> T;
	for (int test = 0; test < T; ++test) {
		char n[25];
		int c;
		fn >> n;
		c = strlen(n);
		cout << "n[]: ";
		for (int i = 0; i < c; ++i) cout << n[i];
		cout << endl;
		fn2 << "Case #" << (test + 1) << ": ";
		cout << "Case #" << (test + 1) << ": ";
		// Lex perm
		if (next_permutation (n, n+c)) {
			for (int i = 0; i < c; ++i) {
				fn2 << n[i];
				cout << n[i];
			}
		} else {
			sort(n, n+c);
			int f;
			for (int i = 0; i < c; ++i) {
				if (n[i] != '0') {f = i; break;}
			}
			fn2 << n[f] << "0";
			cout << n[f] << "0";
			for (int i = 0; i < c; ++i) {
				if (i != f) {
					fn2 << n[i];
					cout << n[i];
				}
			}
		}
		fn2 << endl;
		cout << endl;
	}
	fn.close();
	fn2.close();
	system("pause");
	return 0;
}
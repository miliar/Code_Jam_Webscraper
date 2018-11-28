#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <map>
#include <set>
#include <string>

using namespace std;

char pic[50][52];
int r, c;

bool repl(int i, int j, char c) {
	if (i >= r || j >= c || pic[i][j] != '#') return true;
	pic[i][j] = c;
	return false;
}

int main(void) {
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;
	for (int tcase = 0; tcase < t; tcase++) {

		in >> r >> c;
		for (int i = 0; i < r; i++) {
			in >> pic[i];
		}

		bool fail = false;

		for	(int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (pic[i][j] == '#') {
					fail = fail || (repl(i, j, '/') || repl(i + 1, j, '\\') || repl(i, j + 1, '\\') || repl(i + 1, j + 1, '/'));
				}
			}
		}

		out << "Case #" << (tcase + 1) << ":\n";
		if (fail) {
			out << "Impossible\n";
		} else {
			for	(int i = 0; i < r; i++) {
				out << pic[i] << "\n";
			}
		}
	}

}

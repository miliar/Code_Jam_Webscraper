#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <fstream>

using namespace std;

string s;

inline char check(char a, char b, char c, char d) {
	s[0] = a;
	s[1] = b;
	s[2] = c;
	s[3] = d;
	sort(s.begin(), s.begin() + 4);
	//cout << "s = " << s << "\n";
	if (s == "XXXX" || s == "TXXX" || s == "XTXX" || s == "XXTX" || s == "XXXT") {
		return 'X';
	}
	if (s == "OOOO" || s == "TOOO" || s == "OTOO" || s == "OOTO" || s == "OOOT") {
		return 'O';
	}
	return 'N';
}

int main() {
	ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
	int t;
	in >> t;
	s.resize(4);
	char a[4][4];
	bool f, was;
	for (int i = 0; i < t; ++i) {
		was = false;
		out << "Case #" << i + 1 << ": "; 
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				in >> a[j][k];
				//out << a[j][k] << " ";
				if (a[j][k] == '.') {
					was = true;
				}
			}
		}
		//cout << "\nRead\n";
		f = false;
		if (check(a[0][0], a[0][1], a[0][2], a[0][3]) == 'X' ||
			check(a[1][0], a[1][1], a[1][2], a[1][3]) == 'X' ||
			check(a[2][0], a[2][1], a[2][2], a[2][3]) == 'X' ||
			check(a[3][0], a[3][1], a[3][2], a[3][3]) == 'X' ||

			check(a[0][0], a[1][0], a[2][0], a[3][0]) == 'X' ||
			check(a[0][1], a[1][1], a[2][1], a[3][1]) == 'X' ||
			check(a[0][2], a[1][2], a[2][2], a[3][2]) == 'X' ||
			check(a[0][3], a[1][3], a[2][3], a[3][3]) == 'X' ||

			check(a[0][0], a[1][1], a[2][2], a[3][3]) == 'X' ||
			check(a[0][3], a[1][2], a[2][1], a[3][0]) == 'X') {
				if (i == t - 1) {
					out << "X won";
				}
				else
					out << "X won\n";
				f = true;
		} else {
			if (check(a[0][0], a[0][1], a[0][2], a[0][3]) == 'O' ||
				check(a[1][0], a[1][1], a[1][2], a[1][3]) == 'O' ||
				check(a[2][0], a[2][1], a[2][2], a[2][3]) == 'O' ||
				check(a[3][0], a[3][1], a[3][2], a[3][3]) == 'O' ||

				check(a[0][0], a[1][0], a[2][0], a[3][0]) == 'O' ||
				check(a[0][1], a[1][1], a[2][1], a[3][1]) == 'O' ||
				check(a[0][2], a[1][2], a[2][2], a[3][2]) == 'O' ||
				check(a[0][3], a[1][3], a[2][3], a[3][3]) == 'O' ||

				check(a[0][0], a[1][1], a[2][2], a[3][3]) == 'O' ||
				check(a[0][3], a[1][2], a[2][1], a[3][0]) == 'O') {
				if (i == t - 1) {
					out << "O won";
				}
				else
					out << "O won\n";
				f = true;
			}
		}
		if (!f && was) {
			if (i == t - 1) 
				out << "Game has not completed";
			else
				out << "Game has not completed\n";
		} 
		if (!f && !was) {
			if (i == t - 1)
				out << "Draw";
			else
				out << "Draw\n";
		}

	}
	//system("PAUSE");
}
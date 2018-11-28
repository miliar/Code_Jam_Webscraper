/*
 * Written by Benjamin Kittridge
 *     for Google Code Jam
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <bitset>
#include <stack>
#include <iomanip>
#include <boost/algorithm/string.hpp>

using namespace std;

bool match(char a, char b, char c, char d) {
	char m;

	if (a == '.' || b == '.' || c == '.' || d == '.')
		return false;
	if (a != 'T')
		m = a;
	else if (b != 'T')
		m = b;
	if ((a == m || a == 'T') && (b == m || b == 'T') &&
	    (c == m || c == 'T') && (d == m || d == 'T')) {
		cout << m << " won";
		return true;
	}
	return false;
}

void run() {
	char s[4][4];
	uint32_t i, j;

	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			cin >> s[i][j];
	
	for (i = 0; i < 4; i++) {
		if (match(s[0][i], s[1][i], s[2][i], s[3][i]))
			return;
		if (match(s[i][0], s[i][1], s[i][2], s[i][3]))
			return;
	}

	if (match(s[0][0], s[1][1], s[2][2], s[3][3]))
		return;
	if (match(s[3][0], s[2][1], s[1][2], s[0][3]))
		return;

	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (s[i][j] == '.') {
				cout << "Game has not completed";
				return;
			}
		}
	}

	cout << "Draw";
}

int main(int argc, char **argv) {
	uint32_t n;

	cin >> n >> ws;

	for (uint32_t c = 1; n--; c++) {
		cout << "Case #" << c << ": ";
		run();
		cout << endl;
	}
	return 0;
}


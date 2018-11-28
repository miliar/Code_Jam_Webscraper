#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
//#include <random>
#include <time.h>

using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ size

int main () {
	int pocet, i, a1, a2, a3, ii, iii, draw, j;
	string r;
	char znak, rr[3][5][5];
	cin >> pocet;
	for (i = 0; i < pocet; i++) {
		scanf("%c", &znak);
		for (ii = 0; ii < 4; ii++) {
			for (iii = 0; iii < 4; iii++) {
				scanf("%c", &znak);
				for (j = 0; j < 2; j++) {
					if (znak != 'T')
						rr[j][ii][iii] = znak;
					else if (j == 0)
						rr[j][ii][iii] = 'X';
					else
						rr[j][ii][iii] = 'O';
				}
			}
			scanf("%c", &znak);
		}
		a1 = 0;
		for (j = 0; j < 2; j++) {
			for (ii = 0; ii < 4; ii++) {
				if (rr[j][ii][0] == rr[j][ii][1] && rr[j][ii][1] == rr[j][ii][2] && rr[j][ii][1] == rr[j][ii][3] && rr[j][ii][0] != '.' && a1 == 0) {
					cout << "Case #" << i + 1 << ": " << rr[j][ii][2] << " won" << endl;
					a1 = 1;
				}
			}
			for (ii = 0; ii < 4; ii++) {
				if (rr[j][0][ii] == rr[j][1][ii] && rr[j][0][ii] == rr[j][2][ii] && rr[j][0][ii] == rr[j][3][ii] && rr[j][3][ii] != '.' && a1 == 0) {
					cout << "Case #" << i + 1 << ": " << rr[j][0][ii] << " won" << endl;
					a1 = 1;
				}
			}
			if (rr[j][0][0] == rr[j][1][1] && rr[j][0][0] == rr[j][2][2] && rr[j][0][0] == rr[j][3][3] && rr[j][3][3] != '.' && a1 == 0) {
				cout << "Case #" << i + 1 << ": " << rr[j][0][0] << " won" << endl;
				a1 = 1;
			}
			if (rr[j][0][3] == rr[j][1][2] && rr[j][0][3] == rr[j][2][1] && rr[j][0][3] == rr[j][3][0] && rr[j][3][0] != '.' && a1 == 0) {
				cout << "Case #" << i + 1 << ": " << rr[j][0][3] << " won" << endl;
				a1 = 1;
			}
		}
		draw = 1;
		for (ii = 0; ii < 4; ii++) {
			for (iii = 0; iii < 4; iii++) {
				if (rr[0][ii][iii] == '.') {
					draw = 0;
				}
				//cout << rr[0][ii][iii];
			}
			//cout << endl;
		}
		//cout << endl;
		if (draw == 0 && a1 == 0) {
			cout << "Case #" << i + 1 << ": Game has not completed" << endl;
			continue;
		} else if (a1 == 0)
			cout << "Case #" << i + 1 << ": Draw" << endl;
	}
	return 0;
}

#include <iostream>
#include <cstdio>
#include <sstream>

using namespace std;

int main() {
	int T; scanf("%d", &T);
	stringstream ss;
	for (int i = 0; i < T; i++) {
		ss << "Case #" << i+1 << ": ";

		char c[5][5];
		for (int j = 0; j < 4; j++) {
			scanf("%s", c[j]);
		}

		int xwon = 0, owon = 0;
		int cnt = 0;
		for (int j = 0; j < 4; j++) {
			cnt = c[0][j]+c[1][j]+c[2][j]+c[3][j];
			if (cnt == 'X'*4 || cnt == 'X'*3+'T') xwon = 1;
			cnt = c[j][0]+c[j][1]+c[j][2]+c[j][3];
			if (cnt == 'X'*4 || cnt == 'X'*3+'T') xwon = 1;

			cnt = c[0][j]+c[1][j]+c[2][j]+c[3][j];
			if (cnt == 'O'*4 || cnt == 'O'*3+'T') owon = 1;
			cnt = c[j][0]+c[j][1]+c[j][2]+c[j][3];
			if (cnt == 'O'*4 || cnt == 'O'*3+'T') owon = 1;
		}
		cnt = 0;
		for (int j = 0; j < 4; j++) cnt += c[j][j];
		if (cnt == 'X'*4 || cnt == 'X'*3+'T') xwon = 1;
		cnt = 0;
		for (int j = 0; j < 4; j++) cnt += c[3-j][j];
		if (cnt == 'X'*4 || cnt == 'X'*3+'T') xwon = 1;
		cnt = 0;
		for (int j = 0; j < 4; j++) cnt += c[j][j];
		if (cnt == 'O'*4 || cnt == 'O'*3+'T') owon = 1;
		cnt = 0;
		for (int j = 0; j < 4; j++) cnt += c[3-j][j];
		if (cnt == 'O'*4 || cnt == 'O'*3+'T') owon = 1;

		if (xwon) ss << "X won" << endl;
		if (owon) ss << "O won" << endl;
		if (xwon || owon) continue;

		int draw = 1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (c[j][k] == '.') draw = 0;
			}
		}
		if (draw) ss << "Draw" << endl;
		else ss << "Game has not completed" << endl;
	}
	cout << ss.str();
	return 0;
}

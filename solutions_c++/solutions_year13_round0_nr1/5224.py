#include <iostream>
#include <fstream>

using namespace std;

ifstream inp("input.txt");
ofstream out("output.txt");
char dat[4][4];

bool check(int r, char c, int sx, int sy, int dx, int dy) {
	//cout << "#" << sx << ", " << sy << endl;
	for (int i = 0; i < 4; i++) {
		if (dat[sx][sy] == c || dat[sx][sy] == 'T') {
			sx += dx;
			sy += dy;
		} else {
			return false;
		}
	}
	out << "Case #" << r << ": " << c << " won" << endl;
	return true;
}

bool check_draw(int r) {
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			if (dat[x][y] == '.') {
				return false;
			}
		}
	}
	out << "Case #" << r << ": Draw" << endl;
	return true;
}

int main() {
	int n;
	inp >> n;

	for (int i = 0; i < n; i++) {

		for (int x = 0; x < 4; x++) {
			for (int y = 0; y < 4; y++) {
				inp >> dat[x][y];
			}
		}

		char p;
		bool chk = false;
		for (int z = 0; z < 2; z++) {
			p = z ? 'X' : 'O';

			for (int x = 0; x < 4; x++) {
				if (!chk) {
					chk |= check(i+1, p, 0, x, 1, 0);
				}
				if (!chk) {
					chk |= check(i+1, p, x, 0, 0, 1);
				}
			}
			if (!chk) {
				chk |= check(i+1, p, 0, 0, 1, 1);
			}
			if (!chk) {
				chk |= check(i+1, p, 0, 3, 1, -1);
			}
			if (chk) {
				break;
			}
		}

		if (!chk) {
			if (check_draw(i+1)) {
				continue;
			}
			out << "Case #" << i+1 << ": Game has not completed" << endl;
		}

	}

	return 0;
}

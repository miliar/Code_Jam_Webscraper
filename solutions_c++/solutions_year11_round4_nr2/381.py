#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
using namespace std;

fstream in, out;

int t;

int r, c, d;

int grid[500][500];

int min(int x, int y) {
	if (x < y) {
		return x;
	} else {
		return y;
	}
}

bool isok(int x, int y, int test) {
	int vx = 0;
	int vy = 0;
	for (int i = x; i < x + test; i++) {
		for (int j = y; j < y + test; j++) {
			if ((i != x || j != y) && 
				(i != x || j != y + test - 1) && 
				(i != x + test - 1 || j != y) && 
				(i != x + test - 1 || j != y + test - 1)) {
				vx += grid[i][j] * (2*i - 2*x - (test - 1));
				vy += grid[i][j] * (2*j - 2*y - (test - 1));
			}
		}
	}
	if (vx == 0 && vy == 0) {
		return true;
	} else {
		return false;
	}
}

int main() {
	in.open("probb.in", fstream::in);
	out.open("probb.out", fstream::out);
 
	in >> t;

    for (int i = 0; i < t; i++) {
		in >> r >> c >> d;
		char next;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				in >> next;
				grid[j][k] = (int)(next - '0');
			}
		}

		int m = min(r, c);
		int ans = 0;
		for (int test = m; test >= 3; test--) {
			for (int x = 0; x <= r - test; x++) {
				for (int y = 0; y <= c - test; y++) {
					if (isok(x, y, test)) {
						ans = test;
						break;
					}
				}
				if (ans > 0) {
					break;
				}
			}
			if (ans > 0) {
				break;
			}
		}

		if (ans > 0) {
			out << "Case #" << i + 1 << ": " << ans << endl;
		} else {
			out << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
   
	in.close();
	out.close();

	return 0;
}

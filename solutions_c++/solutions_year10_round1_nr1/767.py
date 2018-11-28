#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main() {
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt0.in");
	//ifstream in("A.in");
	ofstream out("A.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		int N, K; bool isb = 0, isr = 0;
		in >> N >> K;
		char grid[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				in >> grid[i][j];
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = N - 1; j >= 0; j--) {
				if (grid[i][j] != '.') {
					for (int k = j + 1; k < N && grid[i][k] == '.'; k++) {
						swap(grid[i][k - 1], grid[i][k]);
					}
				}
			}
		}

		// hor
		for (int i = 0; i < N; i++) {
			for (int j = 0; j <= N - K; j++) {
				if (grid[i][j] == '.') continue;
				bool is = 1;
				for (int k = 0; k < K - 1; k++) {
					if (grid[i][k + j] != grid[i][k + j + 1]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
			if (isb && isr) {
				break;
			}
		}

		// ver
		for (int i = 0; i <= N - K; i++) {
			for (int j = 0; j < N; j++) {
				bool is = 1;
				for (int k = 0; k < K - 1; k++) {
					if (grid[k + i][j] != grid[k + 1 + i][j]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
			if (isb && isr) {
				break;
			}
		}

		// dia + +
		for (int i = 0; i <= N - K; i++) {
			for (int j = 0; j <= N - K; j++) {
				// + +
				bool is = 1;
				for (int X = 0, Y = 0; X < K - 1; X++, Y++) {
					if (grid[i + X][j + Y] != grid[i + X + 1][j + Y + 1]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
		}

		// dia + -
		for (int i = 0; i <= N - K; i++) {
			for (int j = K - 1; j < N; j++) {
				bool is = 1;
				for (int X = 0, Y = 0; X < K - 1; X++, Y--) {
					if (grid[i + X][j + Y] != grid[i + X + 1][j + Y - 1]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
		}

		// dia - +
		for (int i = K - 1; i < N; i++) {
			for (int j = 0; j < N - K; j++) {
				bool is = 1;
				for (int X = 0, Y = 0; X < K - 1; X--, Y++) {
					if (grid[i + X][j + Y] != grid[i + X - 1][j + Y + 1]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
		}

		// dia - -
		for (int i = K - 1; i < N; i++) {
			for (int j = K - 1; j < N; j++) {
				bool is = 1;
				for (int X = 0, Y = 0; X < K - 1; X--, Y--) {
					if (grid[i + X][j + Y] != grid[i + X - 1][j + Y - 1]) {
						is = 0; break;
					}
				}
				if (is) {
					if (grid[i][j] == 'B') isb = 1;
					else if (grid[i][j] == 'R') isr = 1;
				}
				if (isb && isr) {
					break;
				}
			}
			if (isb && isr) {
				break;
			}
		}

		if (isr && isb) {
			out << "Case #" << x << ": " << "Both" << endl;
		} else if (!isr && !isb) {
			out << "Case #" << x << ": " << "Neither" << endl;
		} else {
			out << "Case #" << x << ": " << (isb?"Blue":"Red") << endl;
		}
	}

	return 0;
}

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int H, W;
vector< vector<int> > m;
vector< vector<char> > b;
vector<int> dumb;
vector<char> dumb2;

void rec(int y, int x, char c) {
	// Care of the sink
	if (y > 0 && b[y - 1][x] == '7') {
		b[y - 1][x] = c - 'a' + 'A';
		rec(y-1, x, c);
	}
	if (y < H-1 && b[y + 1][x] == '^') {
		b[y + 1][x] = c - 'a' + 'A';
		rec(y+1, x, c);
	}
	if (x > 0 && b[y][x - 1] == '>') {
		b[y][x - 1] = c - 'a' + 'A';
		rec(y, x-1, c);
	}
	if (x < W-1 && b[y][x + 1] == '<') {
		b[y][x + 1] = c - 'a' + 'A';
		rec(y, x+1, c);
	}
}

int main() {
	fstream fn;
	ofstream fn2;
	int T;
	fn.open ("input.txt");
	fn2.open ("C:\output.txt");
		fn >> T;
		for (int test = 0; test < T; ++test) {
			fn >> H >> W;
			dumb.resize(W);
			dumb2.resize(W);
			m.resize(H);
			b.resize(H);
			for (int j = 0; j < H; ++j) {
				m[j] = dumb;
				b[j] = dumb2;
				for (int k = 0; k < W; ++k) {
					fn >> m[j][k];
				}
			}

			int c = 0;
			for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					int a = 10111;
					if (k > 0 && m[k - 1][j] < a) a = m[k - 1][j];
					if (k < H-1 && m[k + 1][j] < a) a = m[k + 1][j];
					if (j > 0 && m[k][j - 1] < a) a = m[k][j - 1];
					if (j < W-1 && m[k][j + 1] < a) a = m[k][j + 1];
					if (m[k][j] <= a) {
						b[k][j] = 'a' + (c++);
					} else if (k > 0 && m[k - 1][j] == a) {
						b[k][j] = '^';
					} else if (j > 0 && m[k][j - 1] == a) {
						b[k][j] = '<';
					} else if (j < W-1 && m[k][j + 1] == a) {
						b[k][j] = '>';
					} else if (k < H-1 && m[k + 1][j] == a) {
						b[k][j] = '7';
					}
				}
			}
			for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					if ('a' <= b[k][j] && b[k][j] <= 'z') rec(k, j, b[k][j]);
				}
			}
			char recode[26];
			int rc = 0;
			for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					bool f = false;
					if ('A' <= b[k][j] && b[k][j] <= 'Z') b[k][j] = b[k][j] - 'A' + 'a';
					for (int z = 0; z < rc; ++z) {
						if (recode[z] == b[k][j]) {
							f = true;
							break;
						}
					}
					if (!f) {
						recode[rc++] = b[k][j];
					}
				}
			}
			//for (int z = 0; z < rc; ++z) {cout << (char)(recode[z]-'a'+'A');} cout << endl;
			for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					for (int z = 0; z < rc; ++z) {
						if (b[k][j] == recode[z]) {b[k][j] = 'a' + z; break;}
					}
				}
			}
			/*for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					cout << b[k][j];
				}cout << endl;
			}cout << endl;*/

			fn2 << "Case #" << (test + 1) << ":" << endl;
			for (int k = 0; k < H; ++k) {
				for (int j = 0; j < W; ++j) {
					fn2 << b[k][j] << " ";
				}fn2 << endl;
			}
		}
	fn.close();
	fn2.close();
	system("pause");
	return 0;
}
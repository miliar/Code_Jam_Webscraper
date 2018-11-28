#include <iostream>

using namespace std;

int A [100][100];
char v [100][100];
int addR [4] = {-1,  0,  0, +1};
int addC [4] = { 0, -1, +1,  0};
int h, w;
char current;
char walk (int r, int c) {
	if (v [r][c] >= 'a') return v [r][c];
	int mm = -1;
	for (int i = 0; i < 4; ++i)
	if (r + addR [i] >= 0 && r + addR [i] < h &&
		c + addC [i] >= 0 && c + addC [i] < w &&
		A [r + addR [i]] [c + addC [i]] < A [r][c]) {
			if (mm < 0 || A [r + addR [mm]] [c + addC [mm]] > A [r + addR [i]] [c + addC [i]])
				mm = i;
	}
	
	if (mm == -1) {
		// sink
		v [r][c] = current;
		current++;
		return v [r][c];
	} else {
		return (v [r][c] = walk(r + addR [mm], c + addC [mm]));
	}
}
int main () {
	int X;
	cin >> X;
	for (int x = 0; x < X; ++x) {
		cin >> h >> w;
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j) {
				cin >> A [i][j];
				v [i][j] = 'a' - 1;
			}
		current = 'a';
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				walk (i, j);
		cout << "Case #" << x + 1 << ":" << endl;
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) 
				cout << (j == 0 ? "" : " ") << (char) v [i][j];
			cout << endl;
		}
	}
}


#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

int main() {

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {

		int R, C;
		cin >> R >> C;

		int tiles[50][50];
		memset(tiles, 0, sizeof(tiles));

		int blue = 0;
		int white = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				char c;
				cin >> c;
				switch (c) {
				case '.':
					white++;
					tiles[i][j] = 0;
					break;
				case '#':
					blue++;
					tiles[i][j] = 1;
					break;
				}
			}
		}

		if (blue % 4 != 0) {
			cout << "Case #" << t << ": " << endl << "Impossible" << endl;
			continue;
		}

		for (int i = 0; i < R - 1; i++) {
			for (int j = 0; j < C - 1; j++) {
				if (tiles[i][j] == 1) {
					if (tiles[i][j + 1] == 1 && tiles[i + 1][j] == 1 && tiles[i
							+ 1][j + 1] == 1) {
						tiles[i][j] = -1;
						tiles[i][j + 1] = -2;
						tiles[i + 1][j] = -3;
						tiles[i + 1][j + 1] = -4;
						blue -= 4;
					}
				}
				if (blue == 0)
					break;
			}

			if (blue == 0)
				break;
		}

		if (blue != 0) {
			cout << "Case #" << t << ": " << endl << "Impossible" << endl;
			continue;
		} else {
			cout << "Case #" << t << ":" << endl;
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					switch (tiles[i][j]) {
					case 0:
						cout << ".";
						break;
					case -1:
						cout << "/";
						break;
					case -2:
						cout << "\\";
						break;
					case -3:
						cout << "\\";
						break;
					case -4:
						cout << "/";
						break;
					}
				}
				cout << endl;
			}

		}

	}

	return 0;
}

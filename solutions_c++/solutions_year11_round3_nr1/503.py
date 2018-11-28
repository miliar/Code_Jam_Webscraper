#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

char grid[50][50];
int main() {
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int R, C;
		cin >> R >> C;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				cin >> grid[i][j];

		bool possible = true;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (grid[i][j] == '#') {
					if (i == R-1 || j == C-1)
						possible = false;
					else {
						if (grid[i+1][j] != '#' || grid[i+1][j+1] != '#' || grid[i][j+1] != '#')
							possible = false;
						else {
							grid[i][j] = '/';
							grid[i][j+1] = '\\';
							grid[i+1][j] = '\\';
							grid[i+1][j+1] = '/';
						}
					}
				}
			}
		}
		cout << "Case #" << cc << ":" << endl;
		if (possible) {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++)
					cout << grid[i][j];
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
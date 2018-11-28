#include <iostream>

using namespace std;

int main() {
	int N; cin >> N;
	for(int I=0; I<N; ++I) {
		int r, c; cin >> r >> c;
		char grid[r][c];
		for (int i=0; i<r; ++i) {
			for (int j=0; j<c; ++j) {
				char r; cin >> r;
				grid[i][j]=r;
			}
		}
		bool possible=true;
		for (int i=0; i<r; ++i) {
			for (int j=0; j<c; ++j) {
				if(grid[i][j]=='#') {
					grid[i][j]='/';
					if (j+1 < c and grid[i][j+1]=='#') grid[i][j+1]='\\'; else possible=false;
					if (i+1 < r and grid[i+1][j]=='#') grid[i+1][j]='\\'; else possible=false;
					if (j+1 < c and i+1 < r and grid[i+1][j+1]=='#') grid[i+1][j+1]='/'; else possible=false;
				}
			}
		}
		cout << "Case #" << I+1 << ":" << endl;
		if (!possible) {
			cout << "Impossible" << endl;
		} else {
			for (int i=0; i<r; ++i) {
				for (int j=0; j<c; ++j) {
					cout << grid[i][j];
				}
				cout << endl;
			}
		}
	}
}

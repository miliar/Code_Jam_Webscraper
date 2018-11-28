#include<iostream>
#include<string>

using namespace std;

const int MAXN = 55;

char picture[MAXN][MAXN];
int r, c;

void makeNewPicture() {
	char newPic[MAXN][MAXN];

	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			newPic[i][j] = 'a';
		}
	}

	// other rows
	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			if(picture[i][j] == '.') {
				newPic[i][j] = '.';
			}
			else {
				if(newPic[i][j] == 'a') {
					if(i == r-1 || j == c-1) {
						cout << "Impossible" << endl;
						return;
					}
					else if(picture[i][j+1] == '#' && picture[i+1][j] == '#' && picture[i+1][j+1] == '#') {
						newPic[i][j] = '/';
						newPic[i][j+1] = '\\';
						newPic[i+1][j] = '\\';
						newPic[i+1][j+1] = '/';
					}
					else {
						cout << "Impossible" << endl;
						return;
					}
				}
			}
		}
	}

	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			cout << newPic[i][j];
		}
		cout << endl;
	}
}

int main() {
	int T = 0;
	cin >> T;

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		r = 0;
		c = 0;
		cin >> r >> c;

		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				char x;
				cin >> x;
				picture[i][j] = x;
			}
		}

/*
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				cout << picture[i][j];
			}
			cout << endl;
		}
*/

		cout << "Case #" << caseNum << ":" << endl;

		makeNewPicture();
	}

	return 0;
}

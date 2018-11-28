#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	char A[52][52];
	for(int t=1; t<=T; t++) {
		int R, C;
		cin >> R >> C;
		for(int i=1; i<=R; i++)
			for(int j=1; j<=C; j++)
				cin >> A[i][j];
		bool ans = true;
		for(int i=1; i<=R; i++) for(int j=1; j<=C; j++) {
			if (A[i][j] == '#') {
				if (A[i+1][j] != '#' || A[i][j+1] != '#' || A[i+1][j+1] != '#') {
					i = R; ans = false;
					break;
				}
				A[i][j] = A[i+1][j+1] = '/';
				A[i+1][j] = A[i][j+1] = '\\';
			}
		}
		cout << "Case #" << t << ":" << endl;
		if (!ans) cout << "Impossible" << endl;
		else {
			for(int i=1; i<=R; i++) {
				for(int j=1; j<=C; j++)
					cout << A[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}


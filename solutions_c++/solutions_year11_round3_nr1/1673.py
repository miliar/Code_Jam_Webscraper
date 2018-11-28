#include <iostream>
#include <string>
using namespace std;
int main() {
	int T, R, C;
	string A[50];
	cin >> T;
	for (int z = 1; z <= T; ++z) {
		cin >> R >> C;
		for (int i = 0; i < R; ++i) cin >> A[i];
		bool b = true;
		for (int i = 0; b && i < R; ++i)
			for (int j = 0; b && j < C; ++j)
				if (A[i][j] == '#') {
					b = i+1 < R && j+1 < C && A[i][j+1] == '#' && A[i+1][j] == '#' && A[i+1][j+1] == '#';
					if (b) {
						A[i][j] = '/';
						A[i][j+1] = '\\';
						A[i+1][j] = '\\';
						A[i+1][j+1] = '/';
					}
				}
		cout << "Case #" << z << ":\n";
		if (b) {
			for (int i = 0; i < R; ++i)
				cout << A[i] << "\n";
		}
		else cout << "Impossible\n";
	} 
}
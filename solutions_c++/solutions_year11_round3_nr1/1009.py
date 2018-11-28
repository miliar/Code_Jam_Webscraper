#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int case_nr, T, R, C;

	cin >> T;

	for (case_nr=1; case_nr<=T; case_nr++) {
		cout << "Case #" << case_nr << ":\n";

		cin >> R >> C;

		vector<string> t(R);
		for (int i=0; i<R; i++)
			cin >> t[i];

		bool possible = true;
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if (t[i][j]=='#') {
					if (i==R-1 || j==C-1) {
						possible = false;
						break;
					}
					if (t[i+1][j]=='#' && t[i][j+1]=='#' && t[i+1][j+1]=='#') {
						t[i][j]='/';
						t[i+1][j]='\\';
						t[i][j+1]='\\';
						t[i+1][j+1]='/';
					} else {
						possible = false;
						break;
					}
				}
			}
		}

		if (possible) {
			for (int i=0; i<R; i++)
				cout << t[i] << "\n";
		} else
			cout << "Impossible\n";
	}
}

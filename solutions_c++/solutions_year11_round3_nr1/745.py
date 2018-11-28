#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	char tbl[64][64];

	for (int tn=0;tn<t;tn++) {
		int R,C;
		cin >> R >> C;
		
		for (int i=0;i<R;i++) {
			for (int j=0;j<C;j++) {
				cin >> tbl[i][j];
			}
		}

		bool f = true;

		cout.precision(10);
		cout << "Case #" << (tn+1) << ": " << endl;
		
		for (int i=0;i<R && f;i++) {
			for (int j=0;j<C ;j++) {
				if (tbl[i][j] == '#') {
					if (i>=R-1 || j>=C-1) {
						f = false;
						break;
					}
					if (tbl[i+1][j+1]!='#' || tbl[i+1][j]!='#' || tbl[i][j+1]!= '#' ) {
						f = false;
						break;
					}
					tbl[i][j] = '/';
					tbl[i+1][j+1] = '/';
					tbl[i+1][j] = '\\';
					tbl[i][j+1] = '\\';
				}
			}
		}

		if (f) {
			for (int i=0;i<R;i++) {
				for (int j=0;j<C;j++) {
					cout <<  tbl[i][j];
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}

	}

	return 0;
}

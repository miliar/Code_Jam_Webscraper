#include <iostream>
#include <fstream>

using namespace std;

int main() {
	
	int i, j, k;
	bool ok;
	int T, R, C;
	char mat[55][50];
	
	fstream fin, fout;
	fin.open("A-large-0.in", fstream::in);
	fout.open("A-large-0.out", fstream::out);
	
	fin >> T;
	
	for (i = 0; i < T; i++) {
		fin >> R >> C;
		
		for (j = 0; j < R; j++) {
			for (k = 0; k < C; k++) {
				fin >> mat[j][k];
			}
		}
		
		ok = true;
		for (j = 0; (j < R-1) && (ok == true); j++) {
			for (k = 0; k < C-1; k++) {
				if (mat[j][k] == '#') {
					mat[j][k] = '/';
					if ( mat[j][k+1] != '#') {
						ok = false;
						break;
					} else {
						mat[j][k+1] = '\\';
					}
					
					if ( mat[j+1][k] != '#') {
						ok = false;
						break;
					} else {
						mat[j+1][k] = '\\';
					}
					
					if ( mat[j+1][k+1] != '#') {
						ok = false;
						break;
					} else {
						mat[j+1][k+1] = '/';
					}
				}
			}
		}
		
		if (ok) {
			for (j = 0; j < R; j++) {
				if (mat[j][C-1] == '#') {
					ok = false;
					break;
				}
			}
		}
		
		if (ok) {
			for (j = 0; j < C; j++) {
				if (mat[R-1][j] == '#') {
					ok = false;
					break;
				}
			}
		}
		
		fout << "Case #" << i+1 << ":\n";
		
		if (!ok) {
			fout << "Impossible\n";
		} else {
			for (j = 0; j < R; j++) {
				for (k = 0; k < C; k++) {
					fout << mat[j][k];
				}
				fout << "\n";
			}
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
		
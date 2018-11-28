#include <iostream>
#include <fstream>

using namespace std;

int main() {
	
	int i, j, k;
	bool ok;
	int T, N, L, H;
	unsigned int notes[100];
	
	fstream fin, fout;
	fin.open("C-small-0.in", fstream::in);
	fout.open("C-small-0.out", fstream::out);
	
	fin >> T;
	
	for (i = 0; i < T; i++) {
		fin >> N >> L >> H;
		
		for (j = 0; j < N; j++) {
			fin >> notes[j];
		}
		
		ok = false;
		for (j = L; j <= H && !ok; j++) {
			ok = true;
			for (k = 0; k < N; k++) {
				if (j < notes[k] && (notes[k] % j != 0)) {
					ok = false;
					break;
				} else if (j > notes[k] && (j % notes[k] != 0)) {
					ok = false;
					break;
				}
			}
			if (ok) {
				fout << "Case #" << i + 1 << ": " << j << "\n";
				break;
			}	
		}
		
		if (!ok) {
			fout << "Case #" << i + 1 << ": NO\n";
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
		
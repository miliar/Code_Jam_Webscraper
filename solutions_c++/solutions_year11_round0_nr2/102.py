#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open(argv[1]);
	int T;
	f >> T;
	for (int i=0; i<T; i++) {
		int C, D, N;
		f >> C;
		string* CC = new string[C];
		for (int j=0; j<C; j++)  f >> CC[j];
		f >> D;
		string* DD = new string[D];
		for (int j=0; j<D; j++)  f >> DD[j];
		string NN;
		f >> N;
		f >> NN;
		int j = 1;
		while (j <= N-1) {
			int c = 0;
			int ci = -1;
			while (c < C) {
				if (NN[j] == CC[c][0] && NN[j-1] == CC[c][1] || NN[j-1] == CC[c][0] && NN[j] == CC[c][1]) {
					ci = c;
					break;
				}
				c++;
			}
			if (ci != -1) {
				NN[j-1] = '!';
				NN[j] = CC[c][2];
				j++;
			} else {
				int k = 0;
				int ki = -1;
				while (k <= j-1) {
					if (NN[k] == '!') k++;
					else {
						int di = -1;
						for (int z=0; z<D; z++) {
							if (NN[k] == DD[z][0] && NN[j] == DD[z][1] || NN[j] == DD[z][0] && NN[k] == DD[z][1]) {
								di = z; break;
							}
						}
						if (di != -1) { ki = k; break; }
						k++;
					}
				}
				if (ki != -1) {
					for (int kkk = 0 ; kkk<=j; kkk++) NN[kkk] = '!';
				}
				j++;
			}
		}
		delete[] CC;
		delete[] DD;	

		cout << "Case #" << i+1 << ": [";
		bool fff = false;
		for (int j=0; j<N-1; j++) 
			if (NN[j]!='!') { cout << NN[j] << ", "; fff = true; }
		if (NN[N-1] != '!') cout << NN[N-1];
		else if (fff) cout << "\b\b";
		cout << "]";
		cout << endl; 
	}
	f.close();
}

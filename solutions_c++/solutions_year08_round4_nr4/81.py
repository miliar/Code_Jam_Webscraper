#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	
	int Nx;
	cin >> Nx;
	for(int nx = 1; nx <= Nx; ++nx) {
		cout << "Case #" << nx << ": ";

		int k;
		string S;
		cin >> k;
		getline(cin, S);
		getline(cin, S);

		int Bm = 1000000;
		for(int i = 0; i != k; ++i) {
			vector<int> B(k * (1 << k), 1000000);
			B[(1 << i)*k + i] = 0;
			
			for(int p = 1; p != (1 << k) - 1; ++p) {
				for(int m = 0; m != k; ++m) {
					if(B[p*k+m] == 1000000) continue;
					for(int j = 0; j != k; ++j) {
						if(p & (1 << j)) continue;
						int p2 = p | (1 << j);
						
						// breaks from m to j
						int brs = 0;
						for(int b = 0; b != (int)S.size(); b += k) {
							if(S[b+m] != S[b+j]) ++brs;
						}
						// check for the last
						if(p2 + 1 == (1 << k)) {
							for(int b = 0; b + k < (int)S.size(); b += k) {
								if(S[b+k+i] != S[b+j]) ++brs;
							}
						}
						B[p2*k+j] = min(B[p2*k+j], brs+B[p*k+m]);
					}
				}
			}
			
			for(int j = 0; j != k; ++j) {
				Bm = min(Bm, B[((1 << k) - 1)*k + j]);
			}
		}
		
		cout << (Bm + 1);
		
		cout << endl;
	}
	
}

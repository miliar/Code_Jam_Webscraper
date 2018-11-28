#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int i = 0; i < T; ++i) {
		int N = 0;
		f >> N;
		vector<int> moves (N);
		for (int j = 0; j < N; ++j) {
			char c;
			int nm = 0;
			f >> c;
			f >> nm;			
			if (c == 'O') moves[j] = nm;
			else moves[j] = -nm;
		}
				
		//start positions
		int PosB = 1;
		int PosO = 1;
		
		//find first black
		int CurB = 0;
		while (CurB < N && moves[CurB] > 0) CurB++;
				
		//find first orange
		int CurO = 0;
		while (CurO < N && moves[CurO] < 0) CurO++;

		int res = 0;
		while (CurO < N || CurB < N) {			
			if (CurB == N && CurO == N) break;
			if (CurB == N) {
				res += abs(abs(moves[CurO]) - PosO) + 1;
				PosO = abs(moves[CurO]);
				//find next orange
				CurO++;
				while (CurO < N && moves[CurO] < 0) CurO++;
			}
			else if (CurO == N) {
				res += abs(abs(moves[CurB]) - PosB) + 1;
				PosB = abs(moves[CurB]);
				//find next black
				CurB++;
				while (CurB < N && moves[CurB] > 0) CurB++;
			}

			if (CurO < N && CurB < N) {
				int Btogo = abs(abs(moves[CurB]) - PosB);
				int Otogo = abs(abs(moves[CurO]) - PosO);
				if (CurO < CurB) {
					PosO = abs(moves[CurO]);
					res += Otogo + 1;
					if (Btogo > Otogo) {
						PosB = abs(moves[CurB]) - PosB < 0 ? PosB - (Otogo + 1) : PosB + (Otogo + 1);
					} else {
						PosB = abs(moves[CurB]);
					}
					//find next orange
					CurO++;
					while (CurO < N && moves[CurO] < 0) CurO++;
				} else {
					PosB = abs(moves[CurB]);
					res += Btogo + 1;					
					if (Btogo < Otogo) {
						PosO = abs(moves[CurO]) - PosO < 0 ? PosO - (Btogo + 1) : PosO + (Btogo + 1);
					} else {
						PosO = abs(moves[CurO]);
					}					
					//find next black
					CurB++;
					while (CurB < N && moves[CurB] > 0) CurB++;					
				}
			}
		}

		//cout << "Case #" << i+1 << ": " << res << endl;
		of << "Case #" << i+1 << ": " << res << endl;
	}
	f.close();
	of.close();
	cin.get();
}
#include <iostream>
#include <iomanip>
#include <fstream>
//#include <string>
//#include <vector>

using namespace std;

int T, N, P;
char R;

int main() {
//	char bah;

	//ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\A-small-attempt0.in");
	//ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\A-small-attempt0.out");
	//ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\A-sample.in");
	//ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\A-sample.out");
	ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\A-large.in");
	ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\A-large.out");

	fin >> T;


	for (double casenum = 1; casenum <= T; casenum++) {		


		fin >> N; //commands
		int Opos = 1;
		int Bpos = 1;
		int Obuffer = 0;
		int Bbuffer = 0;
		int Cost = 0;

		for(int i = 0; i < N; i++) {
			fin >> R;
			fin >> P;
			int tmpCost = 0;
			if (R == 'O') {
				if (Opos != P) { 
					tmpCost = abs(Opos - P) - Obuffer;
					if (tmpCost >= 0) {
						Bbuffer += tmpCost;
						Cost += tmpCost;
					}
				}
				Obuffer = 0;
				Bbuffer += 1;
				Cost += 1;
				Opos = P;
			} else if (R == 'B') {
				if (Bpos != P) { 
					tmpCost = abs(Bpos - P) - Bbuffer;
					if (tmpCost >= 0) {
						Obuffer += tmpCost;
						Cost += tmpCost;
					}
				}
				Bbuffer = 0;
				Obuffer += 1;
				Cost += 1;
				Bpos = P;
			}
		}
						
		fout << "Case #" << casenum << ": ";
		fout << Cost << endl;
	}

//cout << "WHAT" << endl; cin >> bah;
}
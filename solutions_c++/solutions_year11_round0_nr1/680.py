 
#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

int T, N, P, op, ot, bp, bt, lt, tt;
char R;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	for (int t = 1; t <= T; t ++) {
		fin >> N;
		op = bp = 1;
		ot = bt = lt = 0;
		for (int n = 0; n < N; n ++) {
			fin >> R >> P;
			if (R == 'O') {
				tt = abs (P - op) + 1;
				if (ot + tt <= lt) {
					ot = lt + 1;
				}
				else {
					ot = ot + tt;
				}
				op = P;
			}
			else {
				tt = abs (P - bp) + 1;
				if (bt + tt <= lt) {
					bt = lt + 1;
				}
				else {
					bt = bt + tt;
				}
				bp = P;
			}
			lt = max (ot, bt);
		}
		fout << "Case #" << t << ": " << lt << endl;
	}
}
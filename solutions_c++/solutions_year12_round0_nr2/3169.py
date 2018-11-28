#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T, S, p, N;
	fin >> T;
	for (int i = 1; i <= T; i++) {
		fin >> N;
		fin >> S;
		fin >> p;
		int st, ust;
		if (p >= 2) {
			st = p + (p-2) + (p-2);
			ust = p + (p-1) + (p-1);
		}
		else if (p == 1) {
			st = 1;
			ust = 1;
		}
		else {
			st = 0;
			ust = 0;
		}
		int stnum = 0;
		int nstnum = 0;
		for (int j = 0; j < N; j++) {
			int tt;
			fin >> tt;
			if (tt >= ust) {
				nstnum ++;
			}
			else if (tt >= st) {
				stnum ++;
			}
		}
		fout << "Case #" <<  i << ": ";
		if (stnum <= S) {
			fout << nstnum + stnum << endl;
		}
		else {
			fout << nstnum + S << endl;
		}
	}
	
}
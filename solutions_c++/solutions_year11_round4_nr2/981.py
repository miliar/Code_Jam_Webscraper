#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

int main() {
	ifstream in("B.in");
	ofstream out("B.out");

	int T = 0;
	in >> T;
	for (int k = 1; k <= T; k++) {
		int C, R, D, REZ = -1;
		in >> R >> C >> D;
		vector <string> V;
		for (int i = 0; i < R; i++) {
			string tmp;
			in >> tmp;
			V.push_back(tmp);
		}
		
		for (int i = min(C, R); i >= 3; i--)
			for (int y = 0; y < V.size(); y++)
				for (int x = 0; x < V[0].size(); x++) 
					if ((y + i - 1) < V.size() && (x + i - 1) < V[0].size()) {
						bool flag = true;
						vector <int> sor, oszlop;

						for (int h = 0; h < i; h++) {
							int tmpSor = 0, tmpOszlop = 0;
							for (int h2 = 0; h2 < i; h2++) {
								tmpSor += V[y+h][x+h2] - '0';
								tmpOszlop += V[y+h2][x+h] - '0';
							}
							sor.push_back(tmpSor);
							oszlop.push_back(tmpOszlop);
						}
						
						int balFelso = V[y][x] - '0';
						int jobbFelso = V[y][x+i-1] - '0';
						int balAlso = V[y+i-1][x] - '0';
						int jobbAlso = V[y+i-1][x+i-1] - '0';
						sor[0] -= balFelso + jobbFelso;
						sor[sor.size()-1] -= balAlso + jobbAlso;
						oszlop[0] -= balFelso + balAlso;
						oszlop[oszlop.size()-1] -= jobbFelso + jobbAlso;

						for (int h4 = 0; h4 < (sor.size()-1-h4); h4++) {
							if (sor[h4] != sor[sor.size()-1-h4]) {
								flag = false;
								break;
							}
							if (oszlop[h4] != oszlop[oszlop.size()-1-h4]) {
								flag = false;
								break;
							}
						}
						if (flag) {
							REZ = i;
							goto FINE;
						}
					}

FINE:
		if (REZ != -1)
			out << "Case #" << k << ": " << REZ << endl;
		else
			out << "Case #" << k << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
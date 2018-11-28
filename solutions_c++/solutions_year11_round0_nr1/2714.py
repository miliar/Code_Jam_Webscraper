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
	ifstream in("A.in");
	ofstream out("A.out");

	int T = 0;
	in >> T;
	for (int k = 1; k <= T; k++) {
		int nr;
		in >> nr;
		int poz;
		char szin;
		vector <char> V;
		vector <int> B, O;
		int actB = 1, actO = 1;
		for (int i = 0; i < nr; i++) {
			in >> szin;
			in >> poz;
			if (szin == 'B') {
				B.push_back(abs(poz - actB));
				actB = poz;
			} else {
				O.push_back(abs(poz - actO));
				actO = poz;
			}
			V.push_back(szin);
		}
		int rez = 0;
		B.push_back(0);
		O.push_back(0);
		int indB = 0, indO = 0;
		for (size_t i = 0; i < V.size(); i++) {
			if (V[i] == 'B') {
				O[indO] -= min(O[indO], B[indB]+1);
				rez += B[indB]+1;
				indB++;
			} else {
				B[indB] -= min(O[indO]+1, B[indB]);
				rez += O[indO]+1;
				indO++;
			}
		}
		out << "Case #" << k << ": " << rez << endl;
	}

	return 0;
}
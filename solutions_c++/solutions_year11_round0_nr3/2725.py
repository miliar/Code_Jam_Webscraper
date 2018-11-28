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

long long S(vector <int> a) {
	if (a.size() == 0) return 0;
	long long rez = a[0];
	for (size_t i = 1; i < a.size(); i++)
		rez = rez ^ a[i];
	return rez;
}

long long SU(vector <int> a) {
	long long rez = 0;
	for (size_t i = 0; i < a.size(); i++) rez += a[i];
	return rez;
}

int main() {
	ifstream in("C.in");
	ofstream out("C.out");

	int T = 0;
	in >> T;

	for (int k = 1; k <= T; k++) {
		int nrCandy;
		long long maxim = -1;
		in >> nrCandy;
		vector <int> C;
		for (int i = 0; i < nrCandy; i++) {
			int tmp;
			in >> tmp;
			C.push_back(tmp);
		}
		for (int i = 0; i < (1 << nrCandy); i++) {
			vector <int> egy, ketto;
			for (int j = 0; j < nrCandy; j++)
				if (i & (1 << j)) egy.push_back(C[j]);
				else ketto.push_back(C[j]);

			if (egy.size() > 0 && ketto.size() > 0) {
				long long rez1 = S(egy), rez2 = S(ketto);

				if (rez1 == rez2) maxim = max(maxim, max(SU(egy), SU(ketto)));
			}
		}
		if (maxim == -1) out << "Case #" << k << ": NO" << endl;
		else out << "Case #" << k << ": " << maxim << endl;
	}

	return 0;
}
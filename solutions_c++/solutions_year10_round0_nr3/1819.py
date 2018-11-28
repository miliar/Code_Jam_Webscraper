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
#include <utility>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

int main() {
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	int T;
	in >> T;
	for (int i = 1; i <= T; i++) {
		int hanyszorNaponta = 0, kapacitas = 0, csoportSzam = 0;
		in >> hanyszorNaponta >> kapacitas >> csoportSzam;
		cout << hanyszorNaponta << " " << kapacitas << " " << csoportSzam << endl;

		vector <int> csoportok;
		for (int j = 0; j < csoportSzam; j++) {
			int tmp = 0;
			in >> tmp;
			csoportok.push_back(tmp);
		}

		vector <int> aux;
		for (int a1 = 0; a1 < 2; a1++)
			for (size_t a2 = 0; a2 < csoportok.size(); a2++)
				aux.push_back(csoportok[a2]);

		vector < pair<int, int> > szam;
		for (int v = 0; v < csoportSzam; v++) {
			int rez = 0, h = 0;
			for (int k = v; k < v + csoportSzam; k++) {
				if ((rez + aux[k]) <= kapacitas) {
					h++;
					rez += aux[k];
				} else {
					break;
				}
			}
			szam.push_back(make_pair(rez, h));
		}
		long long REZ = 0;
		int index = 0;
		for (int p = 0; p < hanyszorNaponta; p++) {
			REZ += szam[index].first;
			index += szam[index].second;
			index %= csoportSzam;
		}
		out << "Case #" << i << ": " << REZ << endl;
	}
	return 0;
}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main() {
	//ifstream in("C-large.in");
	ifstream in("C-small-attempt0.in");
	//ifstream in("C.in");
	ofstream out("C.out");

	int N;

	in >> N;

	for (int ll = 0; ll < N; ll++) {
		int P, Q;
		in >> P >> Q;
		vector <int> pris;
		for (int i = 0; i < Q; i++) { int tmp; in >> tmp; pris.push_back(tmp); }
		sort(pris.begin(), pris.end());
		int best = 0;
		do {
			int calc = 0;
			bool prison[P]; for (int i = 0; i < P; i++) prison[i] = 0;
			for (int i = 0; i < pris.size(); i++) {
				int cell = pris[i] - 1;
				prison[cell] = 1;
				for (int j = cell - 1; j >= 0; j--) {
					if (prison[j]) break;
					calc++;
				}
				for (int j = cell + 1; j < P; j++) {
					if (prison[j]) break;
					calc++;
				}
			}
			if (best == 0) best = calc;
			best = min(calc, best);
		}while (next_permutation(pris.begin(), pris.end()));

		out << "Case #" << ll + 1 << ": " << best << endl;
	}

	return 0;
}

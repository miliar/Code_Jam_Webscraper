#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int emax (int score) {
	if (score <2) return score;
	if (score > 28) return 10;
	return score /3 + 1 - (score %3 == 0);
}

int smax (int score) {
	if (score < 2 || score > 28) return emax (score);
	return score/3 + score %3 + (score%3 == 0);
}

int main () {
	ifstream in ("blarge.in");
	ofstream out ("blarge.out");
	int g, p, s, n;
	in >> n;
	for (int b = 1; b <= n; ++b) {
		in >>g >> s >> p;
		vector <int> sc (g);
		int ret = 0;
		for (int c= 0; c!= g; ++c)
			in >> sc [c];
		if (!p) {		out <<  "Case #" << b << ": " << g << endl;; continue;}
		sort(sc.begin(), sc.end());
		for (int c= 0;c != sc.size (); ++c)
			if (emax (sc[c]) >= p)
				++ret;
		for (int c =0; c!=sc.size (); ++c)
			if (s && emax(sc[c]) < p && smax (sc[c]) >= p) {
				++ret;
				--s;
			}
		out <<  "Case #" << b << ": " << ret << endl;
	}
}

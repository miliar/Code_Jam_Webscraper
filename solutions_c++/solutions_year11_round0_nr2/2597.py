#include "stdafx.h"

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

vector <string> Oppos;
vector <char> R;
vector <int> Counter(256, 0);

bool opposite(char a) {
	for (size_t i = 0; i < Oppos.size(); i++) {
		char b = ' ';
		if (Oppos[i][0] == a) {
			b = Oppos[i][1];
		} else if (Oppos[i][1] == a) {
			b = Oppos[i][0];
		}
		if (b != ' ') {
			if (Counter[b - 'A'] > 0)
				return true;
		}
	}
	return false;
}

int main() {
	ifstream in("B.in");
	ofstream out("B.out");

	int T = 0;
	in >> T;
	cout << T << endl;
	for (int k = 0; k < T; k++) {
		cout << "Test " << k+1 << endl;
		R.clear();
		Oppos.clear();
		for (int z = 0; z < 256; z++) Counter[z] = 0;
		int nrComb = 0;
		string tmp;
		in >> nrComb;
		map <string, int> M;
		map <string, char> H;
		for (int j = 0; j < nrComb; j++) {
			in >> tmp;
			char aux = tmp[2];
			tmp.resize(2);
			sort(tmp.begin(), tmp.end());
			M[tmp]++;
			H[tmp] = aux;
			reverse(tmp.begin(), tmp.end());
			M[tmp]++;
		}
		
		int nrOppos = 0;
		in >> nrOppos;
		for (int j = 0; j < nrOppos; j++) {
			in >> tmp;
			Oppos.push_back(tmp);
		}
		int nrChar = 0;
		in >> nrChar;
		string Seq = "";
		in >> Seq;

		for (size_t i = 0; i < Seq.size(); i++) {
			if (R.size() > 0) {
				string tmp = "";
				tmp += R[R.size()-1];
				tmp += Seq[i];
				sort(tmp.begin(), tmp.end());
				if (M.count(tmp) > 0) {
					Counter[R[R.size()-1]-'A']--;
					R.resize(R.size()-1);
					Counter[H[tmp]-'A']++;
					R.push_back(H[tmp]);
				} else {
					if (opposite(Seq[i])) {
						for (int z = 0; z < 256; z++) Counter[z] = 0;
						R.clear();
					} else {
						Counter[Seq[i]-'A']++;
						R.push_back(Seq[i]);
					}
				}
			} else {
				Counter[Seq[i]-'A']++;
				R.push_back(Seq[i]);
			}
		}

		out << "Case #" << k+1 << ": [";
		for (size_t i = 0; i < R.size(); i++) {
			out << R[i];
			if (i+1 < R.size()) {
				out << ", ";
			}
		}
		out << "]" << endl;
	}

	return 0;
}

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
		int R, C;
		vector <string> V;
		in >> R >> C;
		string st;
		for (int i = 0; i < R; i++) {
			in >> st;
			V.push_back(st);
		}

		bool flag = true;

		vector <string> Rez = V;
		for (int i = 0; i < C; i++)
			for (int j = 0; j < R; j++) {
				if (Rez[j][i] == '#') {
					if (j+1 < R && Rez[j+1][i] == '#' && i+1 < C && Rez[j][i+1] == '#') {
						Rez[j][i] = '/';
						Rez[j+1][i+1] = '/';
						Rez[j+1][i] = '\\';
						Rez[j][i+1] = '\\';
					} else {
						flag = false;
						break;
					}
				}
			}

		if (flag) {
			for (int i = 0; i < C; i++)
				for (int j = 0; j < R; j++)
					if (Rez[j][i] == '#') {
						flag = false;
						break;
					}
		}

		out << "Case #" << k << ":" << endl;
		if (flag) {
			for (int i = 0; i < Rez.size(); i++)
				out << Rez[i] << endl;
		} else {
			out << "Impossible" << endl;
		}
	}

	return 0;
}
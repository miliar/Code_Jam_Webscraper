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

vector <string> felbont(string a) {
	string tmp = "";
	vector <string> rez;
	for (size_t i = 0; i < a.size(); i++) {
		if (a[i] == '/')
			if (tmp != "")
				rez.push_back(tmp);
		tmp += a[i];
	}
	rez.push_back(tmp);
	return rez;
}

int main() {
	ifstream in("A-small.in");
	ofstream out("A-small.out");
	int T = 0;
	in >> T;
	for (int v = 1; v <= T; v++) {
		int N = 0, M = 0;
		in >> N >> M;
		vector <string> megvan, kell;
		for (int i = 0; i < N; i++) {
			string tmp;
			in >> tmp;
			vector <string> X;
			X = felbont(tmp);
			for (size_t j = 0; j < X.size(); j++)
				megvan.push_back(X[j]);
		}
		for (int i = 0; i < M; i++) {
			string tmp;
			in >> tmp;
			vector <string> X;
			X = felbont(tmp);
			for (size_t j = 0; j < X.size(); j++)
				if (find(ALL(kell), X[j]) == kell.end())
					kell.push_back(X[j]);
		}
		sort(ALL(megvan));
		sort(ALL(kell));
		cout << "megvan: " << endl;
		for (size_t i = 0; i < megvan.size(); i++) cout << megvan[i] << endl;
		cout << "kell: " << endl;
		for (size_t i = 0; i < kell.size(); i++) cout << kell[i] << endl;
		int res = 0;
		for (size_t i = 0; i < kell.size(); i++)
			if (find(ALL(megvan), kell[i]) == megvan.end()) {
				cout << "ez kell: " << kell[i] << endl;
				res++;
				megvan.push_back(kell[i]);
				sort(ALL(megvan));
			}
		out << "Case #" << v << ": " << res << endl;
	}
	return 0;
}


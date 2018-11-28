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
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int C = 0;
	in >> C;
	for (int v = 1; v <= C; v++) {
		cout << v << endl;
		int N, K, B, T;
		in >> N >> K >> B >> T;
		vector <int> X, V;
		int tmp = 0;
		for (int i = 0; i < N; i++) {
			in >> tmp;
			X.push_back(tmp);
		}
		for (int i = 0; i < N; i++) {
			in >> tmp;
			V.push_back(tmp);
		}
		for (size_t i = 0; i < N; i++)
			for (size_t j = i+1; j < N; j++)
				if (X[i] > X[j]) {
					swap(X[i], X[j]);
					swap(V[i], V[j]);
				}
		vector <double> kell;
		for (size_t i = 0; i < X.size(); i++) {
			int dist = abs(B - X[i]);
			kell.push_back((double)dist / (double) V[i]);
		}
		int nemJo = 0, rez = 0, OK = 0, marVan = 0;
		for (int i = X.size()-1; i >= 0; i--) {
			if (kell[i] <= T) {
				rez += nemJo;
				marVan++;
			} else 
				nemJo++;
			if (marVan >= K)
				break;
		}
		if (marVan >= K)
			out << "Case #" << v << ": " << rez << endl;
		else
			out << "Case #" << v << ": IMPOSSIBLE" << endl;
	}
	return 0;
}


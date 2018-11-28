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
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T;
	in >> T;
	for (int i = 1; i <= T; i++) {
		int N = 0, K = 0;
		in >> N >> K;
		cout << N << " " << K << endl;
		bool rez = true;
		for (int j = 0; j < N; j++) {
			if (K % 2 != 1) {
				rez = false;
				break;
			}
			K /= 2;
		}
		if (rez)
			out << "Case #" << i << ": ON" << endl;
		else
			out << "Case #" << i << ": OFF" << endl;
	}
	return 0;
}


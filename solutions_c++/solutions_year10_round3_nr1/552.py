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

bool inters(int a1, int b1, int a2, int b2) {
	if (a1 < a2 && b1 > b2) return true;
	if (a1 > a2 && b1 < b2) return true;
	return false;
}

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T;
	in >> T;
	for (int v = 1; v <= T; v++) {
		int N;
		in >> N;
		vector <int> A, B;
		for (int i = 0; i < N; i++) {
			int a, b;
			in >> a >> b;
			A.push_back(a); B.push_back(b);
		}
		int rez = 0;
		for (size_t i = 0; i < A.size(); i++)
			for (size_t j = i+1; j < A.size(); j++)
				if (inters(A[i], B[i], A[j], B[j]))
					rez++;
		out << "Case #" << v << ": " << rez << endl;
	}
	return 0;
}


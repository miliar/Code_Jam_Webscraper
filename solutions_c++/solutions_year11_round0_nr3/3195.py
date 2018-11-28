#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <stack>
#include <queue>

using namespace std;


int main() {

	//ifstream in("C.in");
	//ofstream out("C.out");
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	//ifstream in("C-large.in");
	//ofstream out("C-large.out");

	int T; in >> T;

	for (int x = 0; x < T; x++) {
		int N; in >> N;
		vector<int> v; for (int i = 0; i < N; i++) { int t; in >> t; v.push_back(t); }
		int best = -1;
		for (int i = 0; i < (1 << N); i++) {
			vector<int> a, b;
			for (int j = 0; j < N; j++) {
				if (((1 << j) & i) != 0) a.push_back(v[j]);
				else b.push_back(v[j]);
			}
			if (a.empty() || b.empty()) continue;
			int av = a[0]; int bv = b[0];
			int sa = a[0]; int sb = b[0];
			for (int j = 1; j < a.size(); j++) av ^= a[j], sa += a[j];
			for (int j = 1; j < b.size(); j++) bv ^= b[j], sb += b[j];
			if (av == bv) {
				best = max(best, max(sa, sb));
			}
		}
		out << "Case #" << x + 1 << ": ";
		if (best == -1) out << "NO";
		else out << best;
		out << endl;
	}

	return 0;
}

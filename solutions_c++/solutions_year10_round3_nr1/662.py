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
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt0.in");
	//ifstream in("A.in");
	ofstream out("A.out");

	int T; in >> T;

	for (int x = 1; x <= T; x++) {
		int res = 0;
		int N;
		in >> N;
		vector<pair<int, int> > wires;
		for (int i = 0; i < N; i++) {
			int a, b;
			in >> a >> b;
			wires.push_back(make_pair(a, b));
		}
		for (int i = 0; i < wires.size(); i++) {
			for (int j = i + 1; j < wires.size(); j++) {
				if ((wires[i].first < wires[j].first && wires[i].second > wires[j].second) ||
					(wires[i].first > wires[j].first && wires[i].second < wires[j].second))
					res += 1;
			}
		}
		out << "Case #" << x << ": " << res << endl;
	}

	return 0;
}

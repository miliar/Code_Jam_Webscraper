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

	//ifstream in("A.in");
	//ofstream out("A.out");
	//ifstream in("A-small.in");
	//ofstream out("A-small.out");
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int T; in >> T;

	for (int i = 0; i < T; i++) {
		int n; in >> n;
		int b = 1, o = 1; int tb = 0, to = 0;
		int t = 0;
		for (int j = 0; j < n; j++) {
			char c; int u; in >> c >> u;
			if (c == 'O') {
				int s = max(abs(u - o) - to, 0) + 1; to = 0;
				tb += s;
				t += s;
				o = u;
			} else {
				int s = max(abs(u - b) - tb, 0) + 1; tb = 0;
				to += s;
				t += s;
				b = u;
			}
		}
		out << "Case #" << i + 1 << ": " << t << endl;
	}

	return 0;
}

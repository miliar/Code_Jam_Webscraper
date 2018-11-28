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

long long gcd(long long a, long long b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main() {

	//ifstream in("A.in");
	//ofstream out("A.out");
	//ifstream in("A-small-attempt2.in");
	//ofstream out("A-small.out");
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int T; in >> T;

	for (int x = 1; x <= T; x++) {
		long long N, pd, pg; in >> N >> pd >> pg;
		if ((pg == 100 && pd < 100) || (pg == 0 && pd > 0)) {
			out << "Case #" << x << ": Broken" << endl;
			continue;
		}
		if (100 / gcd(pd, 100) <= N) {
			out << "Case #" << x << ": Possible" << endl;
		} else {
			out << "Case #" << x << ": Broken" << endl;
		}
	}

	return 0;
}

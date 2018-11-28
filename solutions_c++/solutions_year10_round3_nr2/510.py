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
	//ifstream in("A-large.in");
	ifstream in("B-small-attempt0.in");
	//ifstream in("B.in");
	ofstream out("B.out");

	int dp[100]; dp[0] = 0; dp[1] = 1;
	for (int i = 2; i < 100; i++) dp[i] = dp[i / 2] + 1;
	int T;
	in >> T;
	for(int x = 1; x <= T; x++) {
		int L, P, C;
		in >> L >> P >> C;
		int res = 0;
		while (L * C < P) {
			res++; L = L * C;
		}
		out << "Case #" << x << ": " << dp[res] << endl;
	}

	return 0;
}

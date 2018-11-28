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

	int T;

	in >> T;

	for (int x = 0; x < T; x++) {
		string s;
		in >> s;
		string res = s;
		map <char, int> ass;
		ass[s[0]] = 1; res[0] = '1';
		int cur = -1;
		for (int i = 1; i < s.size(); i++) {
			if (ass[s[i]] == 0) {
				ass[s[i]] = cur;
				if (cur == -1) cur = 2; else cur++;
			}

			if (ass[s[i]] == -1) res[i] = '0'; else res[i] = ass[s[i]] + '0';
		}
		if (cur == -1) cur = 2;
		long long calc = 0;
		for (int i = 0; i < res.size(); i++) calc = calc * cur + (res[i] - '0');
		out << "Case #" << x + 1 << ": " << calc << endl;
	}

	return 0;
}

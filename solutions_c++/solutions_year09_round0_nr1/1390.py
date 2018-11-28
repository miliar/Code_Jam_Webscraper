using namespace std;
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define GETS(s) getline(cin, s);
#define GETDS(s, d) getline(cin, s, d);
#define GETI(i) { string _s; getline(cin, _s); i = atoi(_s.c_str()); }
#define GETDI(i, d) { string _s; getline(cin, _s, d); i = atoi(_s.c_str()); }
#define GETF(f) { string _s; getline(cin, _s); f = atof(_s.c_str()); }
#define GETDF(f, d) { string _s; getline(cin, _s, d); f = atof(_s.c_str()); }

typedef map<char, void*> nodes;

void countw(int &result, nodes &n, string patt) {
	//cout << "(R=" << result << " P=" << patt << ")" << endl;
	string s;
	s = patt[0];
	if (s == "(") {
		s = patt.substr(1, patt.find_first_of(")") - 1);
		patt.erase(0, patt.find_first_of(")") + 1);
	} else
		patt.erase(0, 1);
	nodes::iterator iter;
	for (int i = 0; i < s.size(); i++) {
		iter = n.find(s[i]);
		if (iter != n.end()) {
			if (iter->second == NULL)
				result++;
			else
				countw(result, *(nodes*) (iter->second), patt);
		}
	}
}

//----------------------------------------------------------------------------
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int result;

	int L, D, N;
	vs dict;
	string s;
	string patt;
	nodes root, *n, *nl, *nn;
	char c;

	GETDI(L,' ');
	GETDI(D,' ');
	GETI(N);
	FOR(dictix, 0, D-1) {
		GETS(s);
		dict.push_back(s);

		n = &root;
		for (int i = 0; i < s.size(); i++) {
			c = s[i];
			nl = n;
			n = (nodes*) ((*n)[c]);
			if (n == NULL && i < s.size() - 1) {
				nn = new nodes();
				(*nl)[c] = nn;
				n = nn;
			};
		};

	}

	FOR(TestCase, 1, N) {
		result = 0;
		GETS(patt);

		// algorithm
		countw(result, root, patt);
		printf("Case #%d: %d\n", TestCase, result);
	}
	return EXIT_SUCCESS;
}

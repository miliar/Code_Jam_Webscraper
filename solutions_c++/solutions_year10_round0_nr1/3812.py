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
using namespace std;

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

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) {
	return a * a;
}

void disp_list(list<int> &tl) {
	list<int>::iterator it;
	for (it = tl.begin(); it != tl.end(); ++it) {
		cout << "(";
		cout << *it;
		//cout << (*it).from << "|" << (*it).d << "-" << (*it).at ;
		cout << ")->";
	};
	cout << "|" << endl;
}
;

void disp_map(string name, map<int, int> &m) {
	cout << name << ":";
	map<int, int>::iterator i;
	for (i = m.begin(); i != m.end(); ++i) {
		cout << "(";
		cout << (*i).first << "-" << (*i).second;
		//cout << (*it).from << "|" << (*it).d << "-" << (*it).at ;
		cout << ")->";
	};
	cout << "|" << endl;
}
;

void disp_vect(string name, vector<int> &v) {
	cout << name << ":";
	for (int i = 0; i < v.size(); i++) {
		cout << "[";
		cout << v.at(i);
		//cout << (*it).from << "|" << (*it).d << "-" << (*it).at ;
		cout << "]-";
	};
	cout << "|" << endl;
}
;

void Tokenize(const string& str, vector<string>& tokens, const string& delimiters = " ") {
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	string::size_type pos = str.find_first_of(delimiters, lastPos);
	while (string::npos != pos || string::npos != lastPos) {
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		lastPos = str.find_first_not_of(delimiters, pos);
		pos = str.find_first_of(delimiters, lastPos);
	}
}

//----------------------------------------------------------------------------
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	string result;

	int T;
	GETI(T);
	FOR (TestCase, 1, T) {
		result = "OFF";
		// load data
		int N;
		long K;
		GETDI(N,' ');
		GETI(K);
		//cout << "N=" << N << "  K=" << K << endl;
		// algorithm
		long c;
		c = 2;
		FOR (i, 2, N) {
			c *= 2;
		}

		if (K % c == (c-1)) {
			result = "ON";
		} else {
			result = "OFF";
		}

		cout << "Case #" << TestCase << ": " << result << endl;
	}
	return EXIT_SUCCESS;
}

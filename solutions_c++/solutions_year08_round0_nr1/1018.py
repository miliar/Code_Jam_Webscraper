#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <set>
#include <queue>
#include <numeric>
#include <complex>
#include <climits>

using namespace std;

template<class T> inline bool fixmin(T &a, T b) {if (a<=b) return false; a=b; return true;}
template<class T> inline bool fixmax(T &a, T b) {if (a>=b) return false; a=b; return true;}

ifstream is("A.in");
ofstream os("A.out");

void solve(int testnr) {
	int s, q;
	int ret = 0;
	char a[256];
	set<string> b;
	char c;

	is.getline(a, 200);
	istringstream(string(a)) >> s;
	cout << testnr << ": " << s << endl;
	for (int i=0; i<s; i++) {
		is.getline(a, 200);
	}
	is.getline(a, 200);
	istringstream(string(a)) >> q;
	cout << testnr << ": " << q << endl;
	for (int i=0; i<q; i++) {
		is.getline(a, 200);
		b.insert(string(a));
		cout << b.size() << ' ';
		if (b.size()==s) {
			/*for (set<string>::iterator it=b.begin(); it!=b.end(); it++) {
				cout << *it << ',';
			}*/
			b.clear();
			b.insert(string(a));
			ret++;
		}
	}
	cout << endl;
	os << ' ' << ret << endl;
}

int main () {
	int N; is >> N;
	char a[10];
	is.getline(a, 10);
	for (int i=1; i<=N; i++) {
		os << "Case #" << i << ":";
		solve(i);
	}
	return 0;
}

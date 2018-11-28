#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define SZ(a) ((int)a.size())
#define pb push_back
#define mp make_pair

vector<string> split(const string& str) {
	stringstream ss;
	ss << str;
	string s;
	vector<string> res;
	while(ss >> s) res.pb(s);
	return res;
}

string join (const vector<char>& ss, string c, char b, char e) {
	string res;
	int n = ss.size();
	if (n == 0) return "[]";
	if (b != 0) res += b;
	REP(i, n - 1) {
		res += ss[i];
		res += c;
	}
	res += ss[n - 1];
	if (e != 0) res += e;
	return res;
}

int stoi(const string& str) {
	stringstream ss;
	int res;
	ss << str;
	ss >> res;
	return res;
}

string itos(int n) {
	stringstream ss;
	string res;
	ss << n;
	ss >> res;
	return res;
}

istream& getline_int(istream& in, int& i) {
	stringstream ss;
	string s;
	getline(in, s);
	ss << s;
	ss >> i;
	return in;
}

void print_case(ostream& out, int i, const string& str) {
	out << "Case #" << i << ": " << str << endl;
}

int main() {

	freopen("B-small-attempt5.in","r",stdin);
	freopen("B-small-attempt5.out.txt","w",stdout);

	int T;
	getline_int(cin, T);
	REP(i, T) {
		string line;
		getline(cin, line);
		stringstream ss(line);
		int C, D, N;
		string cs, ds, ns;
		ss >> C;
		if (C > 0) ss >> cs;
		ss >> D;
		if (D > 0) ss >> ds;
		ss >> N >> ns;
		vector<char> res;
		int d0 = 0, d1 = 0;
		char n;
		int sz;
		REP(j, N) {
			n = ns[j];
			sz = res.size();
			if (C > 0 && sz > 0 && ((res[sz - 1] == cs[0] && n == cs[1]) || (res[sz - 1] == cs[1] && n == cs[0]))) {
				int b = res[sz - 1];
				if (D > 0 && b == ds[0]) --d0;
				if (D > 0 && b == ds[1]) --d1;
				res.pop_back();
				res.pb(cs[2]);
			} else {
				res.pb(n);
				sz = res.size();
				if (D > 0 && res[sz - 1] == ds[0]) ++d0;
				if (D > 0 && res[sz - 1] == ds[1]) ++d1;
				if ((d0 > 0) && (d1 > 0)) {
					res.clear();
					d0 = d1 = 0;
				}
			}
		}
		print_case(cout, i + 1, join(res, ", ", '[', ']'));
	}

	return 0;
}

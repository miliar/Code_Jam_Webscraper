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

string join (const vector<string>& ss, char c = ' ') {
	string res;
	int n = ss.size();
	REP(i, n - 1) res += (ss[i] + c);
	res += ss[n - 1];
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

//	/*
	freopen("A-large.in","r",stdin);
	freopen("A-large.out.txt","w",stdout);
//	*/

	int T;
	getline_int(cin, T);
	REP(i, T) {
		string line;
		getline(cin, line);
		stringstream ss(line);
		int N;
		ss >> N;
		int res = 0;
		vector<char> btns;
		vector<int> opts;
		vector<int> bpts;
		REP(j, N) {
			char c;
			int p;
			ss >> c >> p;
			btns.pb(c);
			if (c == 'O') opts.pb(p);
			else bpts.pb(p);
		}
		int ON = opts.size();
		int BN = bpts.size();
		int op = 1;
		int bp = 1;
		int oi = 0;
		int bi = 0;
		int next = 0;
		while(next < N) {
			++res;
			if (btns[next] == 'O') {
				if (op != opts[oi]) {
					op += (opts[oi] - op) / abs(opts[oi] - op);
				} else {
					++next;
					++oi;
				}
				if (bi < BN && bp != bpts[bi]) {
					bp += (bpts[bi] - bp) / abs(bpts[bi] - bp);
				}
			} else {
				if (bp != bpts[bi]) {
					bp += (bpts[bi] - bp) / abs(bpts[bi] - bp);
				} else {
					++next;
					++bi;
				}
				if (oi < ON && op != opts[oi]) {
					op += (opts[oi] - op) / abs(opts[oi] - op);
				}
			}
		}
		print_case(cout, i + 1, itos(res));
	}

	return 0;
}

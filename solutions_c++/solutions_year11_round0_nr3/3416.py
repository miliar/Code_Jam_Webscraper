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

vector<int> split_to_int(const string& str) {
	stringstream ss(str);
	int i;
	vector<int> res;
	while(ss >> i) res.pb(i);
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

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out.txt","w",stdout);

	int n;
	getline_int(cin, n);
	REP(i, n) {
		int N;
		getline_int(cin, N);
		string line;
		getline(cin, line);
		vector<int> a = split_to_int(line);
		long long res = -1;
		long long s, p, s_b, p_b;
		FOR(j, 1, (1 << N) - 1) {
			s = 0;
			p = 0;
			s_b = 0;
			p_b = 0;
			REP(k, N) {
				if (j >> k & 1) {
					s += a[k];
					if (s_b == 0) s_b = a[k];
					else s_b ^= a[k];
				} else {
					p += a[k];
					if (p_b == 0) p_b = a[k];
					else p_b ^= a[k];
				}
			}
			if (s_b == p_b) res = max(res, s);
		}
		if (res != -1) print_case(cout, i + 1, itos(res));
		else print_case(cout, i + 1, "NO");
	}

	return 0;
}

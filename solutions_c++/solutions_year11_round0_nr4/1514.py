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

vector<int> split_to_int(const string& str) {
	stringstream ss(str);
	int i;
	vector<int> res;
	while(ss >> i) res.pb(i);
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

void print_case(ostream& out, int i, double str) {
	cout << "Case #" << i << ": " << str << endl;
}

const int MAX_N = 10000;

int bit[MAX_N + 1];

int bit_sum(int i) {
	int s = 0;
	while (i > 0) {
		s += bit[i];
		i -= i & -i;
	}
	return s;
}

void bit_add(int i, int x, int n) {
	while (i <= n) {
		bit[i] += x;
		i += i & -i;
	}
}

bool used[100];

int fuc (int n) {
	if (n <= 1) return 1;
	return n * fuc (n - 1);
}

int main() {


	freopen("D-small-attempt5.in","r",stdin);
	freopen("D-small-attempt5.out.txt","w",stdout);


	int T;
	getline_int(cin, T);
	REP(i, T) {
		int N;
		getline_int(cin, N);
		vector<int> as;
		string line;
		getline(cin, line);
		as = split_to_int(line);
		double res = 0.0;
		memset(used, 0, sizeof(used));
		REP(j, N) if (as[j] == (j + 1)) used[j] = true;
		FOR(j, 2, N) {
			int comb = (1 << j) - 1;
			while (comb < 1 << N) {
				bool flag = false;
				bool temp[N];
				memset(temp, 0, sizeof(temp));
				REP(k, N) {
					if (comb >> k & 1) {
						flag |= used[k];
						temp[as[k] - 1] = true;
					}
				}
				bool flag2 = true;
				REP(k, N) {
					if (comb >> k & 1) {
						flag2 &= temp[k];
					}
				}
				if (!flag && flag2) {
					res += j;
					REP(k, N) {
						if (comb >> k & 1) {
							used[as[k] - 1] = true;
						}
					}
				}
				int x = comb & -comb, y = comb + x;
				comb = ((comb & ~y) / x >> 1) | y;
			}
		}
		int r = 0;
		REP(j, N) if (!used[j]) ++r;
		res += r;
		printf("Case #%d: %.6f\n", i + 1, res);
	}

	return 0;
}

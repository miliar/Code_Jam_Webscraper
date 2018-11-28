#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define FR(i,a,b) for (int i = a; i <= b; ++i)
#define FRC(i,a,b,cond) for (int i = a; i <= b && (cond); ++i)
#define FRB(i,a,b) for (int i = a; i >= b; --i)
#define FRBC(i,a,b,cond) for (int i = a; i >= b && (cond); --i)
#define SZ(a) ((int) a.size())
#define PB push_back
#define SORT(x) sort(x.begin(), x.end())
#define SORTARR(x,n) sort(x, x+n)

typedef long long LL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<long long> VLL;
typedef vector<VI> VVI;

// split string into vector of string
VS split(const string& s, const string& delim=" ") {VS res;string t;FR(i,0,SZ(s)-1)if (delim.find(s[i]) != string::npos)if (!t.empty()) {res.PB(t);t = "";}else;else t += s[i];if (!t.empty()) {res.PB(t);}return res;}
// split string into vector of int
VI splitInt(const string& s, const string& delim=" ") {VS tok = split(s,delim);VI res;FR(i,0,SZ(tok)-1)res.PB(atoi(tok[i].c_str()));return res;}
// split string into vector of double
VD splitDouble(const string& s, const string& delim =" ") {VS tok = split(s,delim);VD res;FR(i,0,SZ(tok)-1)res.PB(atof(tok[i].c_str()));return res;}

// convert any value into a string
template<class T> string valueToString (T x) {ostringstream outs;outs << x;return outs.str ();}

int _x, _X;
string S;
int K;
void processInput() {
	cin >> K >> S;
}

string appl (vector<int> T) {
	string res = S;
	FR(i,0,(S.length()/K)-1) {
		FR(j,0,K-1) {
			res [i * K + j] = S [i * K -1 + T [j]];
		}
	}
	return res;
}

int len (string X) {
	int res = 0;
	FR(i,0,X.length()-1) {
		if (i==0) ++res;
		else if (X [i] != X [i-1]) ++res;
	}
	return res;
}

int res;
void solve() {
	vector<int> T;
	FR(i,1,K) T.push_back (i);
	res = S.length ();
	do {
		string X = appl (T);
		res <?= len (X);
	} while (next_permutation(T.begin(), T.end()));
}

void processOutput() {
	cout << "Case #" << _x << ": " << res << endl;
}

int main () {
	cin >> _X;
	for (_x = 1; _x <= _X; ++_x) {
		processInput ();
		solve();
		processOutput ();
	}
}

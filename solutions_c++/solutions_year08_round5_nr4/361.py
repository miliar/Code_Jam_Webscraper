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
#define MOD 10007
int _x, _X;
int D [200][200];
int H, W, R;
int X [200][200];
void processInput() {
	cin >> H >> W >> R;
	memset (X,0,sizeof (X));
	memset (D,0,sizeof (D));
	FR(i,0,R-1) {
		int r, c;
		cin >> r >> c;
		X [r][c] = 1;
	}
	FR(i,0,H)
	    FR(j,0,W) D [i][j] = -1;
}

long long getAnswer(int r, int c) {
	if (D [r][c] >= 0) return D [r][c];
	if (X [r][c]) return (D [r][c] = 0);
	long long res = 0;
	if (r - 1 >= 1 && c - 2 >= 1) res += getAnswer (r - 1, c - 2);
	if (r - 2 >= 1 && c - 1 >= 1) res += getAnswer (r - 2, c - 1);
	return (D [r][c] = res % MOD);
}

long long res;
void solve() {
	D [1][1] = 1;
	res = getAnswer(H,W);
	if (res < 0) res = 0;
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

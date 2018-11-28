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
int R, C;
string B[16];
int burned;
int r, c;
void processInput() {
	burned = 0;
	cin >> R >> C;
	FR(i,0,R-1) {
		cin >> B [i];
		FR(j,0,C-1) {
			if (B [i][j] != '.') burned |= (1 << (i * C + j));
			if (B [i][j] == 'K') r = i, c = j;
		}		
	}
	/*
	FR(i,0,R-1) {
		FR(j,0,C-1) if (burned & (1 << (i * C + j))) cout << 'B'; else cout << ' ';
		cout << endl;
	}
	cout << burned << endl;
	cout << r << " " << c << endl;
	cout << (burned & (1 << (r * C + c))) << endl;
	*/
}

int win [16][1<<16];

int canWin (int m, int idx){
	//cout << m << " " << idx << endl;
	if (win [idx][m] >= 0)  return win [idx][m];
	int x, y;
	x = idx / C;
	y = idx % C;
	FR(i,-1,1)
	FR(j,-1,1)
	if ((i || j) && x + i >= 0 && x + i < R && y + j >= 0 && y + j < C) {
		int next = (x + i) * C + (y + j);
		if (m & (1 << next)) continue;
		if (!canWin (m | (1 << next), next)) return (win [idx][m] = 1);
	}
	return win [idx][m] = 0;
}
void solve() {
	memset (win, 0xff, sizeof(win));
	canWin (burned, r * C + c);
}

void processOutput() {
	cout << "Case #" << _x << ": " << (canWin (burned, r * C + c) ? "A" : "B") << endl;
}

int main () {
	cin >> _X;
	for (_x = 1; _x <= _X; ++_x) {
		processInput ();
		solve();
		processOutput ();
	}
}

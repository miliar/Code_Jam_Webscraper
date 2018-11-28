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
int D [10][(1 << 10)];
int X [10];
int M, N;
void processInput() {
	cin >> M >> N;
	FR(i,0,M-1) {
		string s;
		cin >> s;
		int m = 0;
		FR(k,0,N-1) {
			m <<=1;
		    if (s [k] == 'x') m += 1;
		}
		X [i] = m;
	}
	memset(D,0xff,sizeof(D));
}

int valid(int m) {
	int cnt = 0;
	FR(i,0,N-2)
	if ((m & (1 << i)) && (m & (1 << (i+1)))) return -1;
	FR(i,0,N-1)
	    if (m &(1<<i)) ++cnt;
	return cnt;
}
int valid(int m1,int m2) {
	if (valid(m1) < 0 || valid(m2) < 0) return 0;
	int cnt = 0;
	FR(i,0,N-2)
	if ((m1 & (1 << i)) && (m2 & (1 << (i+1)))) return 0;
	FR(i,0,N-2)
	if ((m2 & (1 << i)) && (m1 & (1 << (i+1)))) return 0;
	return 1;
}
int mcnt(int m) {
	int cnt = 0;
	FR(i,0,N-1)
	    if (m &(1<<i)) ++cnt;
	return cnt;
}
int res = 0;
void solve() {
	res = 0;
	FR(m,0,(1 << N)-1) {
		if ((m & (X [0])) == 0) {
			res >?= D [0][m] = valid(m);
		} else D [0][m] = -1;
	}
	FR(i,1,M-1) {
		FR(m1,0,(1<<N)-1)
		if ((m1 & X [i]) == 0) {
			int cnt = mcnt(m1);
			FR(m2,0,(1<<N)-1)
			if ((m2 & X [i-1]) == 0)
			    if (valid(m1,m2)) {
					if (D [i][m1] < 0 || D [i][m1] < D [i-1][m2] + cnt)
					    res>?= (D [i][m1] = D [i-1][m2] + cnt);
				}
		}
	}
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

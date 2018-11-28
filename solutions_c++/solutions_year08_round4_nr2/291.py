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
long long N, M, A;
void processInput() {
	cin >> N >> M >> A;
}

int h, w, x, y;
void solve() {
	h = -1, w = -1, x = -1, y = -1;
	for (long long i = 1; i <= N; ++i)
	    for (long long j = M; j >= 0 && i * j >= A; --j) {
			long long r = i * j- A;
			if (r == 0) {
				h = i, w = j, x = 0, y = 0;
				return;
			}
			for (long long k = 1; k <= i; ++k)
			    if (r % k == 0 && r/ k <= j) {
					h = i, w = j, x = k, y = r / k;
					return;
				}
		}
}

long long area (long long x1,long long y1,long long x2, long long y2, long long x3,long long y3) {
	long long res = 0;
	res += (x2 - x1) * (y2 + y1);
	res += (x3 - x2) * (y3 + y2);
	res += (x1 - x3) * (y1 + y3);
	return abs(res);
}

void processOutput() {
	cout << "Case #" << _x << ": ";
	if (h == -1) cout << "IMPOSSIBLE";
	else {
		cout << "0 0 " <<x << " " << w << " " << h << " " << y;
	}
//	cout << "( " << area(0,0,x,w,h,y) << ")";
	cout << endl;
}

int main () {
	cin >> _X;
	for (_x = 1; _x <= _X; ++_x) {
		processInput ();
		solve();
		processOutput ();
	}
}

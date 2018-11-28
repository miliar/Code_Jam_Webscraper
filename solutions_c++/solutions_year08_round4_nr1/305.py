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
int D [60010][2];
int I [60010];
int C [60010];
int G [60010];
int M, V;
void processInput() {
	cin >> M >> V;
	FR(i,1,(M-1)/2) {
	    cin >> G [i] >> C [i];
	    I [i] = -1;
	    D [i][0] = D [i][1] = -2;
	}
	FR(j,1,(M+1)/2) {
	    cin >> I [(M-1)/2 + j];
	    int v =I [(M-1)/2 + j];
	    D [(M-1)/2 +j][v] = 0;
	    D [(M-1)/2 +j][1 - v] = -1;
	}
}

int res;
int getRes (int t, int c1, int c2) {
	if (t == 1) return c1 && c2;
	return c1 || c2;
}
int getType (int o, int t) {
}
int DP (int x, int v) {
	if (x > (M-1)/2) return D [x][v];
	if (D [x][v] > -2) return D [x][v];
	D [x][v] = -1;
	FR(t,0,1)
	if (t <= C [x]) {
		FR(v1,0,1) {
			int r1 = DP(x*2,v1);
			if (r1 > -1)
		    	FR(v2,0,1) {
					int r2 = DP((x*2)+1,v2);
					int cr = getRes ((G [x] + t)%2, v1, v2);
					if (r2 > -1 && cr == v) {
						int re = r1 + r2 + t;
						if (D [x][v] < 0 || D [x][v] > re) D [x][v] = re;
					}
				}
		}
	}
	return D [x][v];
}

void solve() {
	res = DP(1,V);
}

void processOutput() {
	cout << "Case #" << _x << ": ";
	if (res == -1) cout << "IMPOSSIBLE";
	else cout << res;
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

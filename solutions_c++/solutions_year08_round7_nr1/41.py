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
int N;
map<string, vector<string> > inp;
vector<int> C;
map<string, int> cost;
map<string, int> leaves;
string wanted;
void processInput() {
	cin >> N;
	inp.clear ();
	C.clear ();
	cost.clear ();
	FR(i,0,N-1) {
		string name;
		vector<string> ing;
		cin >> name;
		if (i == 0) wanted = name;
		int k;
		cin >> k;
		
		int L = 0;
		FR(j,0,k-1) {
			string t;
			cin >> t;
			if (t [0] >= 'a' && t [0] <= 'z') ++L;
			//else
			ing.PB(t);
		}
		leaves [name] = L;
		inp [name] = ing;
	}
}

int getVal(string name) {
	if (cost.find (name) != cost.end()) return cost [name];
	int res = 0;
	vector<string> c = inp [name];
	
	if (c.size() == 0) return (cost [name] = 1);
	if (c.size() == 1) {
		if (leaves [name] > 0) return 1;
		//if (c [0][0] >= 'a' && c [0][0] <= 'z') return 1;
		return (cost [name] = getVal (c [0]));
	}
	
	vector<int> d;
	FR(i,0,SZ(c)-1) if (c [i][0] >= 'A' && c [i][0] <= 'Z') {
		d.push_back (getVal(c [i]));
	}
	
	
	if (d.size() == 0) {
		return (cost [name] = 1);
	}
	sort(d.begin(),d.end());
	int sub = d [SZ(d)-1];
	int emp = sub - 1;
	FRB(i,SZ(d)-2,0) {
		if (emp >= d [i]) {
			--emp;
		} else {
			sub = sub - emp + d [i];
			emp = d [i] - 1;
		}
	}
	if (emp == 0) emp = 1; else emp = 0;
	return cost [name] = sub + emp;
}

void solve() {
	
}

void processOutput() {
	cout << "Case #" << _x << ": " << getVal(wanted) << endl;
}

int main () {
	cin >> _X;
	for (_x = 1; _x <= _X; ++_x) {
		processInput ();
		solve();
		processOutput ();
	}
}

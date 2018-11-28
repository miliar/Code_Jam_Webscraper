#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>

using namespace std; 

#define BUG(x) if (DEBUG) cout << __LINE__ << ": " << #x << " = " << x << endl; 
#define LET(x, a) __typeof(a) x = a
#define FOREACH(it, v) for(LET(it, (v).begin()); it != (v).end(); ++it) 

typedef long long LL; 

template <class T> inline int size(const T& c) {return (int) c.size();} 
inline LL two(int x) {return (1LL << (x));}
int readInt() {int N = -1; scanf("%d", &N); return N;}
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

struct Solver
{
	vector <string> v;
	bool diag(int sx, int sy, int dx, int dy, char ch) {
		for (int i = 0; i < 4; ++i) {
			if (v[sx][sy] != 'T' && v[sx][sy] != ch)
				return false;
			sx += dx;
			sy += dy;
		}
		return true;
	}
	bool col(int c, char ch) {
		for (int r = 0; r < 4; ++r)
			if (v[r][c] != 'T' && v[r][c] != ch)
				return false;
		return true;
	}
	bool row(int r, char ch) {
		for (int c = 0; c < 4; ++c)
			if (v[r][c] != 'T' && v[r][c] != ch)
				return false;
		return true;
	}
	bool won(char ch) {
		bool chWon = row(0, ch) | row(1, ch) | row(2, ch) | row(3, ch) |
					 col(0, ch) | col(1, ch) | col(2, ch) | col(3, ch) |
					 diag(0, 0, 1, 1, ch) | diag(0, 3, 1, -1, ch);
		return chWon;
	}
	bool dot() {
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (v[i][j] == '.')
					return true;
		return false;
	}
	string solve(vector <string>& v) {
		this -> v = v;
		bool xWon = false;
		bool oWon = false;
		char ch = 'X';
		xWon = won('X');
		oWon = won('O');
		if (xWon) return "X won";
		if (oWon) return "O won";
		if (dot()) return "Game has not completed";
		return "Draw";
	}
};

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		vector <string> v;
		for (int i = 0; i < 4; ++i)
			v.push_back(readString());
		Solver solver;
		string result = solver.solve(v);
		printf("Case #%d: %s\n", test, result.c_str());
	}
	return 0;
}

// Powered by PhoenixAI

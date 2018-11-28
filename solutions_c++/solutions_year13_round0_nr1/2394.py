/*
LANG: C++
ID: he.andr1
PROG: A
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<cassert>
#include<stack>
#include<list>
#include<cstdio>
#include<numeric>
#include<complex>
#include<string>
#include<map>

using namespace std;

#define DEBUG 1

#ifdef DEBUG
	#define ERR cerr
#else
	#define ERR if(true); else cerr
#endif

#define ITER(v, i) for(__typeof(v.begin()) i = v.begin(); i != v.end(); i++) 
#define X real()
#define Y imag()
#define A first
#define B second

typedef pair<int, int> pii;
typedef complex<int> pt;
typedef long long ll;

template <class T> T cross(complex<T> a, complex<T> b) { return imag(a * conj(b)); }

template <class T> T min(T a, T b, T c) { return min(a, min(b, c)); }

template <class T> T max(T a, T b, T c) { return max(a, max(b, c)); }

template <class T> void setmin(T &a, T b) { if(b < a) a = b; }

template <class T> void setmax(T &a, T b) { if(b > a) a = b; }

const int N = 4;
const char WILD = 'T', EMP = '.';

char board[N + 1][N + 1];

int T;

bool won(char c[]) {
	bool good = true;
	for(int i = 0; i < N; i++) {
		good = true;
		for(int j = 0; good && j < N; j++) {
			good = strchr(c, board[i][j]) != NULL;
		}
		if(good) return true;
	}
	for(int i = 0; i < N; i++) {
		good = true;
		for(int j = 0; good && j < N; j++) {
			good = strchr(c, board[j][i]) != NULL;
		}
		if(good) return true;
	}
	good = true;
	for(int j = 0; good && j < N; j++) {
		good = strchr(c, board[j][j]) != NULL;
	}
	if(good) return true;
	good = true;
	for(int j = 0; good && j < N; j++) {
		good = strchr(c, board[j][N - 1 - j]) != NULL;
	}
	if(good) return true;
	return false;
}

void io(istream &in, ostream &out) {
	in >> T;
	for(int i = 0; i < T; i++) {
		for(int j = 0; j < N; j++) {
			in >> board[j];
		}
		out << "Case #" << i + 1 << ": ";
		if(won("XT")) out << "X won";
		else if(won("OT")) out << "O won";
		else {
			bool done = true;
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					if(board[i][j] == '.') done = false;
				}
			}
			if(done) out << "Draw";
			else out << "Game has not completed";
		}
		out << '\n';
	}
}

int main() {
	ifstream fin ("A-large.in");
	if(fin.good()) {
		ofstream fout ("A-large.out");
		io(fin, fout);
		fin.close();
		fout.close();
	} else 
		io(cin, cout);
	return 0;
}
